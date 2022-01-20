import sys
sys.path.append(".")
sys.path.append("..")
from libs.callapi import call_api
from libs.utils import *
import libs.header

def api_test_method(data,*kwargs):
    base_folder = data["folder"] + libs.header.MATERIAL_FOLDER + "\\add_material"
    source_folder = data["folder"] + libs.header.MATERIAL_FOLDER + "\\physical profile"
    dest_folder = data["folder"] + libs.header.MATERIAL_FOLDER + "\\favorite"
    force_remove_dir(dest_folder)
    create_folder(dest_folder)
    url = format_url(data["url"], "8443", "/physicalProperties/custom/add")
    headers = {}
    headers['Authorization'] = data["header"]["Authorization"]
    headers['Content-Type'] = 'application/json'
    ret = []
    code = []
    my_list = [
      "materialSubCategory",
      "maxTemp",
      "minTemp",
      "idealTemp",
      "maxBedTemp",
      "minBedTemp",
      "adhesionSurface",
      "materialDescription",
      "heatedChamberNeeded",
      "density",
      "tensileStrength",
      "impactStrength",
      "surface",
      "transparency",
      "processability",
      "fillDensity",
      "layerHeight",
      "printSpeed",
      "retractionSpeed",
      "idealBedTemp",
      "idealNozzleTemp"
    ]
    test_data = load_data_from_json_file(base_folder+"\\data.json")
    for id in [libs.header.groupId, libs.header.privategroupId]:
        for name in test_data:
            mat_folder =  source_folder + "\\" + name["material"]
            sc_filename = name["subCategory"] + ".json"
            payload = load_data_from_json_file(mat_folder + "\\" + sc_filename)
            if payload:
                payload["materialName"] = name["subCategory"]
                payload["groupId"] = id
                payload["picture"] ="cp-materials-" + name["material"].lower()