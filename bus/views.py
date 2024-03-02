import requests

def getData(request):
    # API endpoint
    api_url = "http://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus"
    external_auth='RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    header={
        "externalauth" : external_auth
    }
    
    try:
        response = requests.get(api_url,headers = header)
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

