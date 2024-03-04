import json
import requests
import urllib3
import base64
from django.http import JsonResponse
# Create a PoolManager instance
http = urllib3.PoolManager()


def getData(request):
    # API endpoint
    print("------------GET DATA CALLED----------------")
    api_url = "https://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus"
    # externalauth = 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    headers = {
        "externalauth": 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    }
    try:
        # response = requests.get(api_url,headers=headers,timeout=10)   
        response = http.request('GET', api_url, headers=headers)  
       
        # print("DATA",str(response.content.decode('iso-8859-1')))
        print("ROW DATA",response.data)
        # print(type(response.raw))
        return JsonResponse(response.data, safe=False)
       
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)



