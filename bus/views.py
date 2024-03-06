import json
import requests
from google.transit import gtfs_realtime_pb2
from google.transit import gtfs_realtime_pb2
# Create a PoolManager instance
from rest_framework.decorators import api_view

from django.http import JsonResponse

@api_view(['GET'])
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
       
        return JsonResponse(data, safe=False)
     
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)



@api_view(['POST'])
def getBusDetailsFromId(request):
    print("------------GET BUS DETAILS CALLED----------------")
    try:
        # Get the vehicleId from the request body
        data = json.loads(request.body)
        vehicle_id = data.get('vehicleId')

        if vehicle_id is None:
            return JsonResponse({"error": "vehicleId is missing in request body"}, status=400)

        # Your existing code to fetch bus details using vehicleId
        api_url = f"https://external.chalo.com/dashboard/enterprise/v1/vehicle/sessionData/thiruvananthapuram/ksrtc?vehicleId={vehicle_id}"
        externalauth = 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
        headers = {
            "externalauth": externalauth
        }
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({"error": "Failed to fetch data"}, status=response.status_code)
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)
       
