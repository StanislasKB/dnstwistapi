import requests
import dns.resolver
import dnstwist


domain = 'modernetsoft.com'
nameservers = dns.resolver.resolve(domain,'NS')
data = dnstwist.run(domain=domain, registered=True, format='null')
temp_list=[]
for i in data:
    temp_dict={}
    temp_dict['fuzzer']=i.get('fuzzer')         
    temp_dict['domain']=i.get('domain')         
    temp_dict['dns_ns']=i.get('dns_ns')         
    temp_dict['dns_a']=i.get('dns_a')         
    temp_dict['dns_mx']=i.get('dns_mx')   
    temp_list.append(i)
print(temp_list, '\n\n')

#api_url = 'http://127.0.0.1:8002/api/twist?domain_name={}'.format(domain)
#response = requests.get(api_url, headers={'X-Api-Key': 'MWrUl8kr.8YJlIZe8ZBuCkfJVXRI66ey2dPFsjFpY'}).json()
#print(response)