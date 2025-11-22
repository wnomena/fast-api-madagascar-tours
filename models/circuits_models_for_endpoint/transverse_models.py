from Controller.Circuit_controller.returned_circuit_manager import Reterned_Circuit
class Result_model_function:
    def __init__(self,code:int,data:list[Reterned_Circuit],error:str):
        self.code = code
        self.data = data
        self.error = error
