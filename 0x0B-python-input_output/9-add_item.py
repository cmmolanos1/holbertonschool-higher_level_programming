#!/usr/bin/python3

import sys

save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

try:
    list_file = load_from_json_file("add_item.json")
except:
    list_file = []

arguments_list = sys.argv[1:]
for arg in arguments_list:
    list_file.append(arg)

save_to_json_file(list_file, "add_item.json")
