from rest_framework import serializers
from Usermanage.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['firstName', 'lastName','userName' ,'description', 'Roles'] 