import json
import requests
from google.transit import gtfs_realtime_pb2
# Create a PoolManager instance


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
        feed = gtfs_realtime_pb2.FeedMessage()
        response = requests.get(api_url, headers=headers)
        data =  feed.ParseFromString(response.content)
        print("Data", data)
        return JsonResponse(data, safe=False)
     
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)


