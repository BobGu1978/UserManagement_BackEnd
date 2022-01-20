import sys
sys.path.append(".")
sys.path.append("..")
from libs.callapi import call_api
from libs.utils import *


def api_test_method(data, expect=[]):
    headers = {}
    headers['Authorization'] = data["header"]["Authorization"]
    response, sc = call_api(data["url"] + ":" + data["port"] + "/auth/logout", headers,data={}, file = "",method = "GET")
    if response == {}:
        print_warning("api logout is not reachable.")
        return False, sc
    else:
        if sc != 200:
            print_warning("api logout fails, the status code is {code}".format(code=sc))
            return False, sc
        else:
            if response["code"] == 200:
                print_info("logout succeeds")
                return True, sc
            else:
                print_warning("logout fails")
                return False, sc

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dt = {}
    dt["url"] = "http://121.229.41.2"
    dt["port"] = "1000"
    dt["folder"] = root_dir() + "\\.."
    dt[
        'token'] = "eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxMDAsInVzZXJfa2V5IjoiYjc3ZjM5OGMtM2FlZC00ZDRhLWJkNGMtZjRmM2Q4OWZhOTIyIiwidXNlcm5hbWUiOiJjbG91ZDNkX2FkbWluIn0.7Bk4gLANc8gjzARyaBebJEZC0Pjbacpcty76t9ZBTrVq35PQqiycwoSN26DzVr6I3MzlseziFn4SSmSsl2DvaA"
    dt["header"] = {
        'Authorization': 'Bearer {token}'.format(token=dt["token"])
    }
    print(api_test_method(dt))
