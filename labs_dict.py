from data_main import get_home
import os
import json


def get_labs():
    current_dir = get_home()
    json_file = os.path.join(current_dir,'lab_names.json')

    with open(json_file) as data_file:
        json_data = json.load(data_file)
        labs = json_data["labs"]
        return labs
