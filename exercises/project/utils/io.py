import json
import logger_config

DATA = "soldiers.json"

def load_json():
    with open(DATA , "r",encoding="utf-8") as soldiers:
        return json.load(soldiers)

        
def save_json(soldiers):
    with open(DATA ,"w" ,encoding="utf-8") as soldiers_file:
        json.dump(soldiers ,soldiers_file ,indent=4)


