import json
import requests
import urllib3

# Create a PoolManager instance


from django.http import JsonResponse

def getData(request):
    http = urllib3.PoolManager()
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
        print("ROW DATA",response.json())
        print("DATA",response.data)
        return JsonResponse(response.data, safe=False)
     
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)

