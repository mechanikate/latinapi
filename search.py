import json, re
from rapidfuzz import process, fuzz, utils
from collections import OrderedDict
dbs, keynames = {}, {}
db_paths = [
    ("lewis", "dbs/lewis/compiled-database.json"),
    ("whitaker", "dbs/whitaker/compiled-database.json")
]
for name, path in db_paths:
    with open(path, "r") as f:
        dbs[name] = json.load(f)
        keynames[name] = list(dbs[name].keys())

def search_dictionary(query="", limit=25, db_name="lewis"):
    return list(OrderedDict.fromkeys([re.sub("[0-9]+$", "", res[0]).lower() for res in process.extract(query, keynames[db_name], scorer=fuzz.QRatio, limit=limit*2, processor=utils.default_process)]))[:25]

def search_dictionary_pos(query="", limit=25, db_name="lewis", pos="V"):
    keynames_fil = list([key for key,val in dbs[name].items() if val["pos"] == pos])
    return list(OrderedDict.fromkeys([re.sub("[0-9]+$", "", res[0]).lower() for res in process.extract(query, keynames_fil, scorer=fuzz.QRatio, limit=limit*2, processor=utils.default_process)]))[:25]
