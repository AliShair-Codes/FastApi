# ##############################
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated # to use in pydantic

class Patient(BaseModel):
    # name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr # EmailStr builtin datatype from pydantic to validate data
    linkedin_url: AnyUrl # AnyUrl to check url formate
    age: int = Field(gt=0, lt=120)
    # weight: float = Field(gt=0) # Field function for data validation // gt lt ge
    eight: Annotated[float, Field(gt=0, strict=True)] # strict prevent typecasting like from '2' to 2
    # married: bool = False # default is false
    married: Annotated[bool, Field(default=None, description="Is the patient married or not")]
    allergies: List[str] # we dont use list cus if we use this we can only valid that the data is list but can't validate that the data is inside the list will be string
    contact_details: Dict[str, str]
    father_name: Optional[str] = None # Optional is for optional field and None is its defualt value
    hobbies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]


    

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")


patient_info = {'name': 'nitish', 'age': 30, 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'email': 'abc@gmail.com', 'phone': '2353462'}}

patient1 = Patient(**patient_info) # ** is to unpack dictionary

insert_patient_data(patient1)
