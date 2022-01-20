import sys
sys.path.append(".")
sys.path.append("..")
from libs.callapi import call_api
from libs.utils import *
import libs.header

def api_test_method(data,*kwargs):
    """ when write data into json file, do remember to use encoding='utf-8' """
    base_folder = data["folder"] + libs.header.ORG_FOLDER + "\\newOrg"
    dest_folder = data["folder"] + libs.header.ORG_FOLDER+ "\\allOrg"
    force_remove_dir(dest_folder)
    create_folder(dest_folder)
    url = format_url(data["url"], data["port"], "/server/org/insertOrg")
    headers = {}
    headers['Authorization'] = data["header"]["Authorization"]
    headers['Content-Type'] = 'application/json'
    ret = []
    code = []
    test_data = load_data_from_json_file(base_folder+"\\data.json")
    for newOrg in test_data:
        payload = newOrg["input"]
        if payload:
            payload["created"] = now_to_string()
            payload["createdby"] = data["username"]
            libs.header.maxOrgId = libs.header.maxOrgId + 1
            payload["orgId"] =  libs.header.maxOrgId
            response, sc = call_api(url, headers, json.dumps(payload))
            rt = check_status_code(sc, 200)
            code.append(sc)
            ret.append(rt)
            """what does the response look like"""
            if rt:
                libs.header.orgIDList.append(payload["orgId"])
                dump_json_2_file(dest_folder + "\\" + payload["orgId"] + ".json", json.dumps(payload))
                logging.info("adding new organization succeeds")
            else:
                logging.warning("adding organization fails.")
                libs.header.maxOrgId = libs.header.maxOrgId -1
        else:
            logging.warning("fail to get data for new organization")
            ret.append(False)
            code.append(-1)
    return not False in ret, code
