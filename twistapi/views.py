from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_api_key.models import APIKey
from twistapi.serializers import DomainsSerializer, KeyObtainSerializer
from rest_framework_api_key.permissions import HasAPIKey
import dnstwist
import requests

class DomainsView(ReadOnlyModelViewSet):
    
    #permission_classes=[HasAPIKey]
    serializer_class=DomainsSerializer
    def get_queryset(self):
        domain_name=self.request.GET['domain_name']
        data = dnstwist.run(domain=domain_name, registered=True, format='null')
        temp_list=[]
        for i in data: 
            temp_dict={}
            temp_dict['fuzzer']=i.get('fuzzer')         
            temp_dict['domain']=i.get('domain')         
            #temp_dict['dns_ns']=i.get('dns_ns')         
            temp_dict['dns_a']=i.get('dns_a')         
            #temp_dict['dns_mx']=i.get('dns_mx')         
            temp_list.append(temp_dict)
        return temp_list
    


class KeyObtainView(ReadOnlyModelViewSet):
    serializer_class=KeyObtainSerializer
    def get_queryset(self):
        nom='toto'
        api_key, key=APIKey.objects.create_key(name=nom)
        data=[{'key_name':api_key,'key_value':key}]
        return data