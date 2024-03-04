import generated_pb2  # Import the generated Python code from your compiled Protobuf schema
import json
import base64
import requests
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
        response = requests.get(api_url,headers=headers,timeout=10)
        print("STATUS CODE:"+str(response.status_code))        
        if response.status_code == 200:
            binary_data = base64.b64decode(response.content)
            protobuf_message = generated_pb2.YourMessage()
            protobuf_message.ParseFromString(binary_data)
            print("protobuf_message:::"+protobuf_message)
            json_data = protobuf_json.pb2json(protobuf_message)
            print(json_data)
            data = str(response.content)
            print(data)
            return JsonResponse(data, safe=False)
        else:
            print("Error:", response.status_code)
            return JsonResponse({"error": response.status_code}, status=response.status_code)
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)

