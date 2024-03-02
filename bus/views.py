import requests

def getData(request):
    # API endpoint
    print("------------GET DATA CALLED----------------")
    api_url = "https://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus"
    headers = {
        "Content-Type": "application/json",
        "externalauth":"RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9"
    }
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

