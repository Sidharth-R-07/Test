import json
import requests
import urllib3

# Create a PoolManager instance
http = urllib3.PoolManager()

from django.http import JsonResponse

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
        response = http.request('GET', 'http://www.example.com')  
        if response.status_code == 200:
            print("DATA",str(response.content.decode('iso-8859-1')))
            print("ROW DATA",response.raw)
            print(type(response.raw))
            return JsonResponse(response.content, safe=False)
        else:
            print("Error:", response.status_code)
            return JsonResponse({"error": response.status_code}, status=response.status_code)
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)

