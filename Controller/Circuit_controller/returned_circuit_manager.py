import threading
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

    def __repr__(self):
        return f"Reterned_Circuit(id={self.id!r})"
        

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

    def Filter_Pure_Itinerary(self) -> list[Itinerary_Model] :
        value:list[Itinerary_Model] = []
        for element in self.itinerary:
            value.append(element)
        return value
    
    def Insert_into_Itinerary(self,itinerarire:list[Itinerary_Model]):
        for params_element in itinerarire:
            for element  in self.include_in_price:
                if element.id == params_element.id:
                    return 0
            if self.itinerary.index(element) == (len(self.itinerary) - 1) and element.id != params_element.id:
                self.itinerary.append(params_element)
                return 1
        
    def Filter_Pure_Equipement(self):
        value:list[Equipement_Model] = []
        for element in self.equipment:
            value.append(element)
        return value
    def Insert_into_Equipement(self,itinerarire:Equipement_Model):
        for params_element in itinerarire:
            for element  in self.include_in_price:
                if element.id == params_element.id:
                    return 0
            if self.equipment.index(element) == (len(self.equipment) - 1) and element.id != params_element.id:
                self.equipment.append(params_element)
                return 1
    def Filter_Pure_Included(self):
        value:list[Included_task_in_Price_Model] = []
        for element in self.include_in_price:
            value.append(element)
        return value
    def Insert_into_Included(self,itinerarire:list[Included_task_in_Price_Model]):
        for params_element in itinerarire:
            for element  in self.include_in_price:
                if element.id == params_element.id:
                    return 0
            if self.include_in_price.index(element) == (len(self.include_in_price) - 1) and element.id != params_element.id:
                self.include_in_price.append(params_element)
                return 1
            
def Group_element_to_simpllify_render(i:list[Reterned_Circuit]) -> list[Reterned_Circuit]:
    value:list[Reterned_Circuit] = []
    for params_element in i:
        if 1 > len(value):
            value.append(params_element)
        else:
            for params_value in value:
                print(value.index(params_value))
                if params_value.id == params_element.id:
                    params_value.Insert_into_Equipement(params_element.equipment)
                    params_value.Insert_into_Itinerary(params_element.itinerary)
                    params_value.Insert_into_Included(params_element.include_in_price)
                if value.index(params_value) == len(value - 1) and params_value.id != params_element.id:
                    value.append(params_element)

    return value
    

