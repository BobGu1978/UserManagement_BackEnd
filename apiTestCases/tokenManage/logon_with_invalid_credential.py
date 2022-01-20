import sys
sys.path.append(".")
sys.path.append("..")
from libs.callapi import call_api
from libs.utils import *
import json
import libs.header

def api_test_method(data, expect=[]):

    base_folder = data["folder"] + libs.header.LOGON_FOLDER
    headers = {}
    headers['Content-Type'] = 'application/json'
    ret = []
    code = []
    test_data = load_data_from_json_file(base_folder+"\\invalid_credential.json")
    dt = {}
    for credential in test_data:
        dt["username"] = credential["username"]
        dt["password"] = credential["password"]
        payload =json.dumps(dt)
        response, sc = call_api(data["url"]+ ":" + data["port"] + "/auth/login",headers, payload)
        if response == {}:
            print_warning("api login is not reachable.")
            ret.append(False)
            code.append(sc)
        else:
            if sc != 200:
                print_warning("api login fails, the status code is {code}".format(code=sc))
            else:
                if response['code'] == 500:
                    print_info("user can't logon with invalid credential, case succeed.")
                    ret.append(True)
                else:
                    print_warning("unexpected code {code} returns".format(code=response['code']))
                    ret.append(False)
                code.append(response['code'])
    return not False in ret, code

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dt = {}
    dt["url"] = "http://121.229.41.2"
    dt["port"] = "1000"
    dt["folder"] = root_dir() + "\\.."
    print(api_test_method(dt))