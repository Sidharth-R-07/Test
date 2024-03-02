import requests

def getData(request):
    # API endpoint
    api_url = "https://fakestoreapi.com/products"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

