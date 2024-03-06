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
        print("Data", feed.entity)
        type(feed.entity)
        return JsonResponse(data, safe=False)
     
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)


def getBusDetailsFromId(request):
    print("------------GET BUS DETAILS CALLED----------------")
    # API endpoint
    api_url = f"http://external.chalo.com/dashboard/enterprise/v1/vehicle/sessionData/thiruvananthapuram/ksrtc?vehicleId=KS3132"
    externalauth = 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    headers = {
        "externalauth": externalauth
    }
    try:
        response = requests.get(api_url, headers=headers)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the JSON data
            print("data", data)
            return JsonResponse(data, safe=False)
        else:
            # Return an error response if the request was unsuccessful
            return JsonResponse({"error": "Failed to fetch data"}, status=response.status_code)
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)
