from typing import Annotated, Union
from pydantic import BaseModel
import dotenv
from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine


from Controller.Circuit_controller.returned_circuit_manager import Group_element_to_simpllify_render, Reterned_Circuit
from models.circuits_models_database.circuit import Contact, Contact_Model
from models.circuits_models_for_endpoint.Get_all_circuits import Get_all_Circuit
from models.circuits_models_for_endpoint.Set_contact import set_full_contact
from models.circuits_models_for_endpoint.transverse_models import Result_model_function

#configuration 
dotenv.load_dotenv()
import os
engine = create_engine(f"mysql+pymysql://{os.getenv("USER")}:{os.getenv("PASS")}@{os.getenv("HOST")}:3306/{os.getenv("DATABASE")}")
app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():   
    try:
        data_from_database:list[Reterned_Circuit] = []
        def callback(x:Result_model_function):
            if x.code:
                for element_to_append in Group_element_to_simpllify_render([data for data in x.data]):
                    data_from_database.append(element_to_append)
            elif x.code == 0:
                raise Exception("Erreur lors des traitements de controlleur surement")
        Get_all_Circuit(engine,callback)
        return {
            "code" : 0,
            "data" : data_from_database,
            "error" : ""
        }
    except HTTPException as Err:
        raise HTTPException(status_code=500,detail={
            "code" : 1,
            "data" : [],
            "error" : Err
        })

@app.post("/")
def set_contact(Form:Annotated[Contact_Model,Form()]):
    try:
        result:Result_model_function = set_full_contact(engine,Form=Form)
        if result.code:
            return result
        else :
            raise HTTPException(status_code=500,detail=result.error)
    except Exception as err:
        raise HTTPException(status_code=500,detail={
            "error" : err,
            "data" : [],
            "code" : 1
        })