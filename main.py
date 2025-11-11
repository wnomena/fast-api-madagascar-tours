from typing import Union

import dotenv
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine

from models.circuits_models_for_endpoint.Get_all_circuits import Get_all_Circuit
from models.circuits_models_for_endpoint.transverse_models import Result_model_function

#configuration 
dotenv.load_dotenv()
import os
engine = create_engine(f"mysql+pymysql://{os.getenv("USER")}:{os.getenv("PASS")}@{os.getenv("HOST")}:3306/{os.getenv("DATABASE")}")
app = FastAPI()


@app.get("/")
async def read_root():   
    data_from_database:list = []
    def callback(x:Result_model_function):
        if x.code:
            [data_from_database.append(element) for element in x.data]
        else:
            raise HTTPException(status_code=500,detail="Something went wrong in database") 
        Get_all_Circuit(engine,callback)
        #il faut encore gerer les données quand il y en aura
        return {"Hello": "World"}


@app.get("/get_one/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#contact
@app.post("/contact")
async def contact():
    return