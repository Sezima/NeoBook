from rest_framework import serializers

class GoogleAuthSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    code = serializers.CharField()
    id_token = serializers.CharField()
    scope = serializers.CharField()
    expires_in = serializers.IntegerField()
    token_type = serializers.CharField()