from sqlalchemy.orm import Session
from sqlalchemy import insert

from models.circuits_models_database.circuit import Contact, Contact_Model
from models.circuits_models_for_endpoint.transverse_models import Result_model_function
#people have already put all asked information and want be contacted to finalise his horder
def set_full_contact(engine,Form:Contact_Model) -> Result_model_function:
    with Session(engine) as session:
        try:
            session.add(Contact(name=Form.name,subject=Form.subject,body=Form.body,number=Form.number,begining=Form.begining,number_of_person=Form.number_of_person,mail=Form.mail,total_price=Form.total_price))
            session.commit()  
            return Result_model_function(code=1,error="",data=[])
        except Exception as Error:
            print(Error)
            return Result_model_function(code=0,error=Error,data=[])
