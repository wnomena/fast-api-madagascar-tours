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
def read_root():   
    data_from_database:list = []
    def callback(x:Result_model_function):
        if x["code"]:
            for element in x["data"]:
                if element not in data_from_database:
                    data_from_database.append(element)
        else:
            print(x["error"])
            raise HTTPException(status_code=500,detail="Something went wrong in database") 
    Get_all_Circuit(engine,callback)
    return data_from_database


@app.get("/get_one/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
