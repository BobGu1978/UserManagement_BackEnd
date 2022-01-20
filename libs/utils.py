import os
import glob
import logging
import json
from shutil import rmtree
import datetime

def now_to_string():
    dt = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds")
    return str(dt)

def root_dir():
    return os.path.abspath(os.curdir)

def my_encode_filename(file_name):
    return file_name.replace("/", "-")

def force_remove_dir(folder_name):
    if os.path.exists(folder_name):
        rmtree(folder_name)

def get_file_size(file_name):
    return os.path.getsize(file_name)

def remove_dir(folder_name):
    try:
        os.rmdir(folder_name)
    except Exception as e:
        logging.debug("the folder {folder_name} is not empty, unable to remove".format(folder_name = folder_name))

def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

def all_subfolders(folder_name):
    return next(os.walk(folder_name))[1]

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def dump_json_2_file(file_name, data):
    with open(file_name,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False)

def compare_list(my_list=[], returned={}, expected={}, result=[]):
    for item in my_list:
        result.append(check_value(returned, item, expected[item]))

def find_all_data_files(dir_name,file_type = "*.json"):
    print(dir_name)
    os.chdir(dir_name)
    ret = []
    for file in glob.glob(file_type):
        ret.append(file)
    return ret

def load_data_from_json_file(file_name):
    try:
        with open(file_name,"r",encoding="utf-8") as source:
            js = json.load(source)
        return js
    except Exception as e:
        print(e)
        return None

def check_status_code(s_code, expected_value):
    logging.info("the expected code is %d, the actual status code is %d", expected_value, s_code)
    if s_code == expected_value:
        logging.info("the result matches")
        return True
    else:
        logging.warning("the result doesn't match")
        return False

def check_value(data, attr_name, expected_value, ret = None):
    if type(expected_value) == type(1):
        logging.info("the expected value is {exp}, the actual value of {attr} is {real}".format(exp =  str(expected_value), attr = attr_name, real = str(data[attr_name])))
    else:
        logging.info("the expected value is {exp}, the actual value of {attr} is {real}".format(exp =  expected_value, attr = attr_name, real = data[attr_name]))
    if data[attr_name] == expected_value:
        logging.info("the result matches.")
        if ret != None:
            ret.append(True)
        return True
    else:
        logging.warning("the result doesn't match.")
        if ret != None:
            ret.append(False)
        return False

def check_length_list(data, attr_name, expect_value):
    logging.info("the expected value is {exp}, the actual length of {attr} is {real}".format(exp =  str(expect_value), attr = attr_name, real = str(len(data[attr_name]))))
    if len(data[attr_name]) == expect_value:
        logging.info("the result matches.")
        return True
    else:
        logging.warning("the result does'nt match.")
        return False

def format_url(url, port, api_name):
    return "{url}:{port}{api_name}".format(url = url , port = port, api_name = api_name)

def print_info(str,info=True):
    if info:
        logging.info(str)
    else:
        logging.warning(str)

def print_warning(str):
    print_info(str, False)