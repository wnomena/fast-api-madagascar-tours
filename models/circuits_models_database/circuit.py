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
    duration:Mapped[str] = mapped_column(String,nullable=False)
    difficulty:Mapped[int] = mapped_column(Integer,nullable=False)
    price:Mapped[int] = mapped_column(Integer,nullable=False)
    image:Mapped[str] = mapped_column(String,nullable=False)
    itinerary = relationship("Itinerary",back_populates="circuit")
    equipment = relationship("Equipement",back_populates="circuit")
    include_in_price = relationship("Included_task_in_Price",back_populates="circuit")
    contact = relationship("Contact",back_populates="circuit")

class Itinerary(Base):
    __tablename__= "itinerary"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    place:Mapped[str] = mapped_column(String,nullable=False)
    order_id:Mapped[int] = mapped_column(Integer,nullable=False)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"))

class Equipement(Base):
    __tablename__= "equipment_needed"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    equipment:Mapped[str] = mapped_column(String,nullable=False)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"))

class Included_task_in_Price(Base):
    __tablename__= "included_in_price"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    content:Mapped[str] = mapped_column(String,nullable=False)
    circuit_id:Mapped[int] = mapped_column(Integer,ForeignKey("circuit.id"))