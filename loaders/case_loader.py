import json
from config.settings import DATA_DIR


def load_imported_cases():
    file_path = DATA_DIR / "importedCases.json"

    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_property_cases():
    file_path = DATA_DIR / "propertyCases.json"

    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    


