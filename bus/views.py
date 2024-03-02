import requests

def getData():
    # API endpoint
    print("---------------getData CALLED-----------------------")
    api_url = "http://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus"
    header = {
        "externalauth": "RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9"
    }
    
    try:
        response = requests.get(api_url, headers=header, timeout=20)
        print("STATUS CODE::"+response.status_code+"-------------------")
        if response.status_code == 200:
            data = response.json()
            print(data)
            return data
        else:
            print("Error:", response.status_code)
            return {"error": response.status_code}
    except Exception as e:
        print("An error occurred:", e)
        return {"error": str(e)}
