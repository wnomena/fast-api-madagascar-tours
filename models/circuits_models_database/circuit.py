from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
class Base(DeclarativeBase):
    pass

#creation de toutes les classes de models avant de faire une relation depuis sqlalchemy
class Circuit(Base):
    __tablename__ = "circuit"
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(50),nullable=False)
    subtitle:Mapped[str] = mapped_column(String(250),nullable=False)
    description:Mapped[str] = mapped_column(String,nullable=False)
    duration:Mapped[str] = mapped_column(String,nullable=False)
    difficulty:Mapped[int] = mapped_column(Integer,nullable=False)
    price:Mapped[int] = mapped_column(Integer,nullable=False)
    image:Mapped[str] = mapped_column(String,nullable=False)
    itinerary = relationship("Itinerary",back_populates="circuit")
    equipment_needed = relationship("Equipement",back_populates="circuit")
    included_in_price = relationship("Included_task_in_Price",back_populates="circuit")
    contact = relationship("Contact",back_populates="circuit")

class Circuit_Model:
    def __init__(self,id:int,
        title:str,
        subtitle:str,
        description:str,
        duration:str,
        difficulty:int,
        price:int,
        image:str):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.duration = duration
        self.description = description
        self.difficulty = difficulty
        self.price = price
        self.image = image


    

class Itinerary(Base):
    __tablename__= "itinerary"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    place:Mapped[str] = mapped_column(String,nullable=False)
    order_id:Mapped[int] = mapped_column(Integer,nullable=False)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"))
    circuit = relationship("Circuit",back_populates="itinerary")

class Itinerary_Model:
    def __init__(self,id:int,
    place:str,
    order_id:int,
    circuit_id:int):
        self.id = id
        self.place = place
        self.order_id = order_id
        self.circuit_id = circuit_id


class Equipement(Base):
    __tablename__= "equipment_needed"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    equipment:Mapped[str] = mapped_column(String,nullable=False)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"))
    circuit = relationship("Circuit",back_populates="equipment_needed")

class Equipement_Model:
    def __init__(self,id:int,
    equipment:str,
    circuit_id:int):
        self.id = id
        self.equipement = equipment
        self.circuit_id = circuit_id

class Included_task_in_Price(Base):
    __tablename__= "included_in_price"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    content:Mapped[str] = mapped_column(String,nullable=False)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"))
    circuit = relationship("Circuit",back_populates="included_in_price")

class Included_task_in_Price_Model:
    def __init__(self,id:int,
    content:str,
    circuit_id:int):
        self.id = id
        self.content = content
        self.circuit_id = circuit_id


class Contact(Base):
    __tablename__ = "contact"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String,nullable=False)
    subject:Mapped[str] = mapped_column(String,nullable=False)
    body:Mapped[str] = mapped_column(String,nullable=False)
    number:Mapped[str] = mapped_column(String,nullable=True)
    begining:Mapped[str] = mapped_column(String,nullable=True)
    number_of_person:Mapped[int] = mapped_column(Integer,nullable=True)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"),nullable=True) 
    circuit = relationship("Circuit",back_populates="contact")
#class for rendering contact to client

class Reterned_Circuit:
    def __init__(self,id:int,
    title:str,
    subtitle:str,
    duration:str,
    description:str,
    difficulty:int,
    price:int,
    image:str,
    itinerary:list[Itinerary_Model],
    equipment:list[Equipement_Model],
    include_in_price:list[Included_task_in_Price_Model]):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.duration = duration
        self.description = description
        self.difficulty = difficulty
        self.price = price
        self.image = image
        self.itinerary = itinerary
        self.equipment = equipment
        self.include_in_price = include_in_price
        
        
    