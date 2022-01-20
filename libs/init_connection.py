import sys
sys.path.append(".")
sys.path.append("..")
from libs.utils import load_data_from_json_file

def initialize_connecton(data_json_file):
  connection_data = load_data_from_json_file(data_json_file)
#  print(connection_data)
#  url = "{url}:{port}".format(url = connection_data["url"], port = connection_data["port"])
  return (connection_data["url"], connection_data["port"],connection_data["username"] , connection_data["password"])

if __name__== "__main__":
  url,port, dt,dd = initialize_connecton("C:\\Users\\Administrator\\PycharmProjects\\Cloud3DPrint_APITest\\connection.json")
  print(url)
  print(dt)
  print(dd)
