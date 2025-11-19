from models.circuits_models_database.circuit import Equipement_Model, Included_task_in_Price_Model, Itinerary_Model


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
        

    def Filter_Pure_Circuit(self):
        return {
        "id" : self.id,
        "title": self.title,
        "subtitle" : self.subtitle,
        "duration" : self.duration,
        "description" : self.description ,
        "difficulty": self.difficulty,
        "price" : self.price,
        "image": self.image,
        }
    
    def Filter_Pure_Itinerary(self):
        value:list[Itinerary_Model] = []
        for element in self.itinerary:
            value.append({
                
            })