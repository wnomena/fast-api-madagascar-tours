from sqlalchemy.orm import Session
from sqlalchemy import insert

from models.Contact_models import Contact
#people want to be contacted for all and anithing there are any circuit specified and any specified client information
def set_contact_Lambda(engine,contact:Contact,callback):
    with Session(engine) as session:
        try:
            insert_into = insert(Contact).values(contact)
            session.execute(insert_into)    
            callback({
                "code" : 0,
                "data" : [],
                "error" : ""
            })  
        except Exception as Error:
            callback({
                "code" : 0,
                "data" : [],
                "error" : Error
            })


#people have already put all asked information and want be contacted to finalise his horder
def set_full_contact(engine,contact:Contact,callback):
    with Session(engine) as session:
        try:
            insert_into = insert(Contact).values(contact)
            session.execute(insert_into)    
            callback({
                "code" : 0,
                "data" : [],
                "error" : ""
            })  
        except Exception as Error:
            callback({
                "code" : 0,
                "data" : [],
                "error" : Error
            })
