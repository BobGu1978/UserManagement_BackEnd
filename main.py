import importlib
import csv
import sys
sys.path.append(".")
sys.path.append("..")
from libs.init_connection import initialize_connecton
from libs.utils import *
import logging

logging.basicConfig(filename='test_result.log', encoding='utf-8', level=logging.INFO)


login_data ={}
(login_data["url"],login_data["port"], login_data["username"], login_data["password"]) = initialize_connecton(root_dir() + "\\connection.json")

"""
from api_test_cases.login.login import api_test_method
print("--------start to call login api--------")
ret,sc =  api_test_method(login_data)
print("--------call login api end--------")
if ret =={} or sc!=200:
    print("the login fails, we must quit all the rest tests.")
    exit(1)
login_data['token'] = ret["data"]["access_token"]
"""
"""here is for debug"""
login_data['token'] = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI0Njk4OCIsInJvbGUiOiJST0xFX1VTRVIiLCJpc3MiOiJjYWZ5eWFuZyIsImV4cCI6MTYzNjQwMDkzNywiaWF0IjoxNjM1Nzk2MTM3LCJ1c2VybmFtZSI6IkFCQ0RFREZHIn0.G97jSv7QldsHlC_WPi7IYSKpjl0D2OwLOSaGEDuqSVtJIbhXm-t3FkwzG0nuEnXFp9mb8RVhxdJaVz2VsLMFvg"
login_data["header"] = {
    'Authorization': 'Bearer {token}'.format(token = login_data["token"])
  }

i = 0
with open("apitestcases.csv",newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if i == 0:
            i= i+1
            continue
        folder_name = row[0]
        filename = row[1]
        md = importlib.import_module("api_test_cases.{folder}.{filename}".format(folder=folder_name,filename=filename))
        fn = getattr(md, "api_test_method")
        login_data["folder"] =  root_dir()+ "/api_test_cases/" + folder_name+ "/" + filename
        print_info("--------start to call {fn} api--------".format(fn = filename))
        if len(row)==3:
            arr = row[2].split(";")
            ret, sc = fn(login_data,arr)
        else:
            ret, sc = fn(login_data)
        print_info("--------call {fn} api end--------".format(fn=filename))
