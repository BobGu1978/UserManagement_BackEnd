import sys
sys.path.append(".")
sys.path.append("..")
from libs.callapi import call_api
from libs.utils import *
import json
import libs.header


def api_test_method(data, expect=[]):
    dt = {}
    dt["username"] = data["username"]
    dt["password"] = data["password"]
    payload =json.dumps(dt)
    headers = {
        'Content-Type': 'application/json'
    }
    response, sc = call_api(data["url"]+ ":" + data["port"] + "/auth/login",headers, payload)
    if response == {}:
        print_warning("api login is not reachable.")
        return {}, sc
    else:
        if sc != 200:
            print_warning("api login fails, the status code is {code}".format(code=sc))
        else:
            print_info("login succeeds")
            check_value(response["data"], "expires_in", 720)
    return response, sc

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dt = {}
    dt["url"] = "http://121.229.41.2"
    dt["port"] = "1000"
    dt["username"] = "cloud3d_admin"
    dt["password"] = "123456"
    dt["folder"] = root_dir() + "\\.."
    print(api_test_method(dt))
