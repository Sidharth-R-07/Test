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
        print("------------RESPONSE:::"+response.status_code)
        if response.status_code == 200:
            data = response.json()
            print("-----------DATA:::"+data)
            return JsonResponse(data, safe=False)
        else:
            print("Error:", response.status_code)
            return JsonResponse({"error": response.status_code}, status=response.status_code)
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)

