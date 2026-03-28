from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated # to use in pydantic

# field validator operates in two modes before mode and after mode
# 

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        # yaha humey age ki value '30' string milay gi 30 int nahi to comparison kay waqt err aa jai ga to isey bachnay ka leya mode kay andar after set kar do
        if 0 < value < 100:
            return value
        else: 
            raise ValueError('Age should be i between 0 and 100')

    @field_validator('email')
    @classmethod # it is always a class method
    def email_validator(cls, value): # cls is our class
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value 
    
    @field_validator('name') #mode='after' is default means agar after ha to apko yaha value type coercion honay kay bad milay gi lekin agar type before kar dia to apko value milay gi vo type coercion kay pahlay ki value milay gi
    @classmethod
    def transform_name(cls, value):
        return value.upper()



    

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