from fastapi import FastAPI
from utils import io
import logger_config

app = FastAPI()

@app.get("/soldiers")
def getsoldiers():
    logger_config.logger.info("fatching soldier listfrom datebaes")
    return io.get_soldiers()

@app.get("/soldiers/{id}")
def get_soldier(id):
    return io.get_a_soldier(id)

@app.post("/soldiers")
def add_soldier(id:int ,full_name:str ,rank:str):
    return io.create_new_soldier(id,full_name,rank)

@app.put("/soldiers/{id}")
def update_soldier(id:int ,full_name:str ,rask:str):
    return io.update_soldier(id ,full_name ,rask)

@app.delete("/soldiers{id}")
def del_soldier(id:int):
    return io.delete_soldier(id)






