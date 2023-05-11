from rest_framework import serializers

class DomainsSerializer(serializers.Serializer):
    fuzzer=serializers.CharField(max_length=255)
    domain=serializers.CharField(max_length=255)
    dns_ns=serializers.CharField(max_length=255)
    dns_a=serializers.CharField(max_length=255)
    dns_mx=serializers.CharField(max_length=255)
    


class KeyObtainSerializer(serializers.Serializer):
    key_name=serializers.CharField(max_length=255)
    key_value=serializers.CharField(max_length=255)