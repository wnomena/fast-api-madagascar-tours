from sqlalchemy import select
from sqlalchemy.orm import Session

from models.circuits_models_database.circuit import Circuit
def Get_all_Circuit(engine,callback):
    with Session(engine) as session:
        try:
            data_joined = select(Circuit).join(Circuit.itinerary).join(Circuit.equipment).join(Circuit.include_in_price).where(Circuit.id == id)
            callback({
                "data" :  [element for element in session.scalars(data_joined)],
                "code" : 1,
                "error" : ""
            })
        except Exception as Error:
            callback({
                "data" : [],
                "code" : 0,
                "error" : Error
            })