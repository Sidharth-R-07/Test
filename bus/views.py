import json
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
                encodings = ['utf-8', 'iso-8859-1']  # Try decoding using common encodings
        for encoding in encodings:
            try:
                data = response.content.decode(encoding)
                print(data)
                return JsonResponse(data, safe=False)
            except UnicodeDecodeError:
                print(f"Decoding with {encoding} failed.")
        # If all decoding attempts fail, treat the content as binary
            data = response.content
            print(data)
            return JsonResponse(data, safe=False)
        else:
            print("Error:", response.status_code)
            return JsonResponse({"error": response.status_code}, status=response.status_code)
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)

