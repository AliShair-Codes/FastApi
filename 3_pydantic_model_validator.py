from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated # to use in pydantic

# using model validator we can set validation on two or more fields 
# using field validator we can set validation only on one field

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    contact_details: Dict[str, str]
    #  agar patient ki age 60 se ziada ha to uskay contact details me ik emergency phone number hona chaheya
    # warna hum patient create hi nahi karay gay 

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model): # model is a pydantic model
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model


    

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")


patient_info = {'name': 'nitish', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'email': 'abc@gmail.com', 'phone': '2353462'}}

patient1 = Patient(**patient_info) # at this step validation is perform and type coercion

insert_patient_data(patient1)