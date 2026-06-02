import json
import logger_config

DATA = "soldiers.json"

    

def get_soldiers():
    with open(DATA , "r",encoding="utf-8") as soldiers:
        return json.load(soldiers)

def get_a_soldier(id :int):
    soldiers = get_soldiers()
    for s in soldiers:
        if s["id"] == id:
            return s

def create_new_soldier(id :int,full_name:str ,rank:str):
    soldiers = get_soldiers()
    new_soldier = {"id":id ,"full_name":full_name ,"rank":rank}
    is_soldier = False
    for s in soldiers:
        if s["id"] == id:
            is_soldier = True
    if is_soldier:
        return 409
    soldiers.append(new_soldier)

    with open(DATA ,"w" ,encoding="utf-8") as soldiers_file:
        json.dump(soldiers ,soldiers_file ,indent=4)
    return 201

def update_soldier(id:int ,full_name:str ,rask:str):
    soldiers = get_soldiers()
    is_soldier = False
    us = None
    for s in soldiers:
        if s["id"] == id:
            s["full_name"] = full_name
            s["rask"] = rask
            is_soldier = True
            break
    if not is_soldier:
        return 404
    with open(DATA ,"w" ,encoding="utf-8") as soldiers_file:
        json.dump(soldiers ,soldiers_file ,indent=4)
        return 200
    
def delete_soldier(id:int):
    soldiers = get_soldiers()
    is_soldier = False
    for s in soldiers:
        if s["id"] == id:
            soldiers.remove(s)
            is_soldier = True
            break
    if not is_soldier:
        return 404
    with open(DATA ,"w" ,encoding="utf-8") as soldiers_file:
        json.dump(soldiers ,soldiers_file ,indent=4)
        return 200
        



