from typing import Union

import dotenv
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine

from Controller.Circuit_controller.returned_circuit_manager import Group_element_to_simpllify_render, Reterned_Circuit
from models.circuits_models_for_endpoint.Get_all_circuits import Get_all_Circuit
from models.circuits_models_for_endpoint.transverse_models import Result_model_function

#configuration 
dotenv.load_dotenv()
import os
engine = create_engine(f"mysql+pymysql://{os.getenv("USER")}:{os.getenv("PASS")}@{os.getenv("HOST")}:3306/{os.getenv("DATABASE")}")
app = FastAPI()


@app.get("/")
def read_root():   
    try:
        data_from_database:list[Reterned_Circuit] = []
        def callback(x:Result_model_function):
            if x.code:
                for element_to_append in Group_element_to_simpllify_render([data for data in x.data]):
                    data_from_database.append(element_to_append)
                    print(element_to_append)
            elif x.code == 0:
                print(x.error)
        Get_all_Circuit(engine,callback)
        return data_from_database
    except HTTPException as Err:
        print(Err)
        raise HTTPException(status_code=500,detail=Err)
@app.get("/get_one/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
