from rest_framework.serializers import ModelSerializer
 

from products.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','name','address','pincode','mobile')