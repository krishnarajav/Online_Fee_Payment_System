from rest_framework import serializers
from .models import login as logindb


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = logindb
        fields = '__all__'

    def validate(self, data):
        db_data = logindb.objects.all().values()
        if data['email'] != db_data[0]['email'] or data['password'] != db_data[0]['password']:
            raise serializers.ValidationError("Invalid Username or Password.")
        return data
