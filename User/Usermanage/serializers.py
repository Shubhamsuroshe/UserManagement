from rest_framework import serializers
from Usermanage.models import UserProfile, Roles

#UserSerializer class
class UserSerializer(serializers.ModelSerializer):
   # Roles = serializers.StringRelatedField(many=True)
    class Meta:
        model = UserProfile
        fields = ['firstName', 'lastName','userName' ,'description', 'Roles'] 

# class RoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         models = Roles
#         fields = ['roleName', 'description']