import json
import requests
import urllib3
from django.http import JsonResponse

# Create a PoolManager instance
http = urllib3.PoolManager()

def getData(request):
    # API endpoint
    print("------------GET DATA CALLED----------------")
    api_url = "https://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus"
    headers = {
        "externalauth": 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    }
    try:
        response = http.request('GET', api_url, headers=headers)
        json_data = json.loads(response.data.decode('utf-8'))
        print("JSON DATA", json_data)

        return JsonResponse(json_data, safe=False)
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)
