from sqlalchemy import ForeignKey, Integer, String
from models.circuits_models_database.circuit import Base
from sqlalchemy.orm import Mapped,mapped_column, relationship


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
