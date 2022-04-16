import json
import environ
import razorpay
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from products.models import Order,Cart,Product
from django.contrib.auth.models import User
from .serializers import OrderSerializer


env = environ.Env()

environ.Env.read_env()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_payment(request):
    if not request.data['name'] or not request.data['address'] or not request.data['pincode'] or not request.data['mobile']:
        response_data = {
            "status_code" : 6001,
            "message" : "Please fill all the fields"
        }
    else:
        if request.data['amount'] == 0:
            response_data = {
            "status_code" : 6001,
            "message" : "Can not do the transaction due to the amount is zero!"
        }
        else:
            amount = request.data['amount']
            userId = request.data['userId']
            name = request.data['name']
            address = request.data['address']
            pincode = request.data['pincode']
            mobile = request.data['mobile']
            carts = request.data['carts']

            email = User.objects.get(id=userId).email
            
            
            # setup razorpay client this is the client to whome user is paying money that's you
            client = razorpay.Client(auth=(env('PUBLIC_KEY'), env('SECRET_KEY')))

            # create razorpay order
            # the amount will come in 'paise' that means if we pass 50 amount will become
            # 0.5 rupees that means 50 paise so we have to convert it in rupees. So, we will 
            # mumtiply it by 100 so it will be 50 rupees.
            payment = client.order.create({"amount": float(amount) * 100, 
                                        "currency": "INR", 
                                        "payment_capture": "1"})

            # we are saving an order with isPaid=False because we've just initialized the order
            # we haven't received the money we will handle the payment succes in next 
            # function
            for cart in carts:
                product = cart.get('product')
                product_title = Product.objects.get(id=product).title
                quantity = cart.get('quantity')
                product_amount = (Product.objects.get(id=product).price) * quantity
                order = Order.objects.create(user = userId,
                                            name = name,
                                            address = address,
                                            pincode = pincode,
                                            mobile = mobile,
                                            email = email,
                                            product_title = product_title, 
                                            product_id = product,
                                            product_amount = product_amount,
                                            quantity = quantity,
                                            order_amount = amount, 
                                            order_payment_id = payment['id'],                                   
                                            )

                serializer = OrderSerializer(order)


            response_data = {
                "status_code" : 6000,
                "payment": payment,
                "order": serializer.data,
                "email" :email
            }
    return Response(response_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def handle_payment_success(request):
    
    res = json.loads(request.data["response"])

    ord_id = ""
    raz_pay_id = ""
    raz_signature = ""

    # res.keys() will give us list of keys in res
    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]

    # get order by payment_id which we've created earlier with isPaid=False
    order = Order.objects.filter(order_payment_id=ord_id)

    # we will pass this whole data in razorpay client to verify the payment
    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }
    
    client = razorpay.Client(auth=(env('PUBLIC_KEY'), env('SECRET_KEY')))
    
    try:
        status = client.utility.verify_payment_signature(data)
        
        for order in order:
            order.isPaid = True
            order.status = "Ordered"
            order.save()

        Cart.objects.filter(is_ordered=False).update(is_ordered=True)

        return Response({'message': 'Payment Received Successfully!'})
    
    except:
        print("Redirect to error url or error page")
        return Response({'message': 'Something went wrong'})

