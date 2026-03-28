from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated # to use in pydantic

# a field is not provided by user but can be computed from those fields

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    contact_details: Dict[str, str]
    weight: float #kg
    height: float #mtr

    # we compute bmi of user 
    @computed_field
    @property
    def calculated_bmi(self) -> float: # self is instance of pydantic model 
        bmi = round((self.weight/(self.height)**2), 2) 
        return bmi


    

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.calculated_bmi)
    print("Updated")


patient_info = {'name': 'nitish', 'age': '30', 'weight': 75.2, 'height':1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'email': 'abc@gmail.com', 'phone': '2353462'}}

patient1 = Patient(**patient_info) # at this step validation is perform and type coercion

insert_patient_data(patient1)