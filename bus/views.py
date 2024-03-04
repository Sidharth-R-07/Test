import chardet
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
        if response.status_code == 200:
            encoding = chardet.detect(response.content)['encoding']
            if encoding is None:
                encoding = 'utf-8'  # Set to the default encoding you want to use
            decoded_data = response.content.decode(encoding)
            print(decoded_data)
            print("-----------DATA:::"+decoded_data)
            return JsonResponse(response.content, safe=False)
        else:
            print("Error:", response.status_code)
            return JsonResponse({"error": response.status_code}, status=response.status_code)
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)

