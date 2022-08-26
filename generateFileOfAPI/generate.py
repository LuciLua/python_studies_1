from genericpath import exists, isdir
import json
import os
import requests

api_link = input("API Link here: ")
final_format_file = input("Final format of your file: ")
# link_exemple: https://servicodados.ibge.gov.br/api/v3/agregados

github = requests.get(api_link)
jsongh = github.json()
data_dict = json.dumps(jsongh)

directory = "Result"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)

if os.path.isdir(path):
    print("Already exists")
else:
    os.makedirs(path)
    print("Directory '%s' created" %directory)

name_of_file = input("What is the name of the file: ")
complete_name = os.path.join(path, name_of_file + "." + final_format_file)

file = open(complete_name, "w")
file.write(data_dict)

file.close()
    