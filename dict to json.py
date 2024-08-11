import json

Dict = {
    1: 'one',
    2: 'two',
    3: 'three'
}

with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(Dict, json_file, indent=4, ensure_ascii=False)