import json
import logger_config

DATA = "soldiers.json"

def load_json():
    try:
        with open(DATA, "r", encoding="utf-8") as soldiers_file:
            data = json.load(soldiers_file)
            logger_config.logger.info("Successfully loaded data from JSON")
            return data
    except FileNotFoundError:
        logger_config.logger.error("Could not find soldiers.json file!")
        return []
        
def save_json(soldiers):
    try:
        with open(DATA ,"w" ,encoding="utf-8") as soldiers_file:
            json.dump(soldiers ,soldiers_file ,indent=4)
            logger_config.logger.info("Save soldiers list to JSON")
    except FileNotFoundError:
        logger_config.logger.error("Could not find soldiers.json file!")


