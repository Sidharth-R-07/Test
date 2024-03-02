import requests

def getData():
    # API endpoint
    print("getData CALLED-----------------------")
    api_url = "https://external.chalo.com/dashboard/enterprise/v1/vehicle/sessionData/thiruvananthapuram/ksrtc?vehicleId=KS3132"
    external_auth = 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    header = {
        "externalauth": external_auth
    }
    
    try:
        response = requests.get(api_url, headers=header, timeout=15)
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




