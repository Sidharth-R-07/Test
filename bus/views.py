import requests

def getData(request):
    # API endpoint
    print("------------GET DATA CALLED----------------")
    api_url = "https://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus"
    external_auth = 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    headers = {
        "Content-Type": "application/json",
        "externalauth": external_auth
    }
    
    try:
        response = requests.get(api_url,headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

