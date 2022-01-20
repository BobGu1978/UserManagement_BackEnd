import requests

def call_api(url, headers, data={}, file = "",method = "POST"):
    """call_api return None if there is any exception happening, or it returns one json object from the response which includes the status code"""
    try:
        if file == "":
            response = requests.request(method, url, headers=headers, data=data)
        else:
            response = requests.request(method, url, headers=headers, data=data, files= file)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(errh)
        return {},-1
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        return {},-2
    except requests.exceptions.Timeout as errt:
        print(errt)
        return {},-3
    except requests.exceptions.RequestException as err:
        print(err)
        return {},-4
#    except Exception as err:
#        print(err)
    try:
        ret = response.json()
    except:
        ret ={}
        ret["return value"] = response.text
    return ret , response.status_code

def check_url_reabable(url):
    try:
        get = requests.get(url)
        if get.status_code == 200:
            ret = True
    except:
        ret = False
    return ret