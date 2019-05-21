import json
import pkg_resources

DICTIONARY_JSON_PATH = "data/jyutping_dictionary.json"

toned = {}
toneless = {}


def _load_data(path):
    with open(path, "r") as file:
        table = json.load(file)
        for code, jyutping in table.items():
            jyutping = jyutping.split(" ")[0]  # Uses the first pronunciation
            toned[int(code, 16)] = " " + jyutping + " "
            toneless[int(code, 16)] = " " + jyutping[:-1] + " "


_path = pkg_resources.resource_filename("pyjyutping", DICTIONARY_JSON_PATH)
_load_data(_path)
