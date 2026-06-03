from utils import io


def get_soldiers():
    return io.load_json()

def get_a_soldier(id :int):
    soldiers = io.load_json()
    for s in soldiers:
        if s["id"] == id:
            return s

def create_new_soldier(id :int,full_name:str ,rank:str):
    soldiers = io.load_json()
    new_soldier = {"id":id ,"full_name":full_name ,"rank":rank}
    is_soldier = False
    for s in soldiers:
        if s["id"] == id:
            is_soldier = True
    if is_soldier:
        return 409
    soldiers.append(new_soldier)

    io.save_json(soldiers)
    return 201

def update_soldier(id:int ,full_name:str ,rask:str):
    soldiers = io.load_json()
    is_soldier = False
    for s in soldiers:
        if s["id"] == id:
            s["full_name"] = full_name
            s["rask"] = rask
            is_soldier = True
            break
    if not is_soldier:
        return 404
    
    io.save_json(soldiers)
    return 200
    
def delete_soldier(id:int):
    soldiers = io.load_json()
    is_soldier = False
    for s in soldiers:
        if s["id"] == id:
            soldiers.remove(s)
            is_soldier = True
            break
    if not is_soldier:
        return 404
    io.save_json(soldiers)
    return 200