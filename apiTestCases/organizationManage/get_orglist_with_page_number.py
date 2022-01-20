#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append(".")
sys.path.append("..")
from libs.callapi import call_api
from libs.utils import *
import libs.header

def api_test_method(data,page_pare=[]):
    """pape_pare=[page numnber, page size, expected returned total]"""
    ret = []
    base_folder = data["folder"] + libs.header.ORG_FOLDER+ "\\allOrg"
    url = format_url(data["url"], data["port"], "/server/org/listPage")
    headers = {}
    headers['Authorization'] = data["header"]["Authorization"]
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    dt = {
            'pageNum': page_pare[0],
            'pageSize': page_pare[1]
        }
    expected_result = page_pare[2]
    response, sc = call_api(url , headers, dt)
    if check_status_code(sc,200):
        check_value(response,"code", 200)
        check_value(response["data"],"pageNum", page_pare[0])
        check_value(response["data"],"pageSize", page_pare[1])
        check_value(response["data"],"totalPage", 1)
        check_value(response["data"],"total", expected_result)
        check_length_list(response["data"], "list", expected_result)
        if (expected_result>0) and (response["data"]["total"] == expected_result):
            for org in response["data"]["list"]:
                orgId = org["orgId"]
                print(org)
                file_name = my_encode_filename(
                    "{folder}\\{fn}.json".format(folder=base_folder, fn=orgId))
                print(file_name)
                source = load_data_from_json_file(file_name)
                if source == None:
                    ret.append(False)
                    logging.warning("organization with id {o_id} should not be existed.".format(o_id= orgId))
                else:
                    compare_list(libs.header.ORG_PARAMETERS_LIST, org, source, ret)
            return not False in ret, sc
    else:
        logging.warning("fail to call server/org/listPage")
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
    print(api_test_method(dt,[1,10,3]))