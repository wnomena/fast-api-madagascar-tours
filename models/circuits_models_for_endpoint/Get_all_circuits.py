
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.circuits_models_database.circuit import Adrenaline, Adrenaline_Model, Circuit, Equipement, Equipement_Model, Included_task_in_Price, Included_task_in_Price_Model, Itinerary, Itinerary_Model
from Controller.Circuit_controller.returned_circuit_manager import Reterned_Circuit
from models.circuits_models_for_endpoint.transverse_models import Result_model_function
def Get_all_Circuit(engine,callback):
    with Session(engine) as session:
        try:
            data_joined = select(Circuit,Itinerary,Equipement,Included_task_in_Price,Adrenaline).outerjoin(Circuit.itinerary).outerjoin(Circuit.equipment_needed).outerjoin(Circuit.included_in_price).outerjoin(Circuit.adrenaline)
            data = session.execute(data_joined).all()
            final_value_to_return:list[Reterned_Circuit] = []
            for a,b,c,d,e in data:
                ciruit =  a.__dict__
                itinarary = b.__dict__
                equipement = c.__dict__
                included = d.__dict__
                adrenaline = e.__dict__
                final_value_to_return.append(Reterned_Circuit(id=ciruit["id"],title=ciruit["title"],subtitle=ciruit["subtitle"],description=ciruit["description"],duration=ciruit["duration"],difficulty=ciruit["difficulty"],price=ciruit["price"],image=ciruit["image"],itinerary = [Itinerary_Model(id=itinarary["id"],place=itinarary["place"],order_id=itinarary["order_id"],circuit_id=itinarary["circuit_id"])],equipment = [Equipement_Model(id=equipement["id"],equipment=equipement["equipment"],circuit_id=equipement["circuit_id"])],include_in_price = [Included_task_in_Price_Model(id=included["id"],content=included["content"],circuit_id=included["circuit_id"])],adrenaline=[Adrenaline_Model(id=adrenaline["id"],content=adrenaline["content"],circuit_id=adrenaline["circuit_id"])]))
            callback(Result_model_function(code=1,data=final_value_to_return,error=""))
        except Exception as Error:
            callback(Result_model_function(code=0,data=[],error=Error))