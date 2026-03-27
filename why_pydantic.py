# why pydantic
# data validation and for datatypes

def insert_patient_data(name: str, age: int): # the str and int from python for type hunting it shows parameters datatypes of functions while calling
    if type(name) == str and type(age) == int:
         if age < 0:
            raise ValueError("Age can't be negative")
         else:
            print(name) 
            print(age)
            print("Inserted into DB")
    else:
        raise TypeError("Incorrect datatype")

insert_patient_data("usman", 40)


def update_patient_data(name: str, age: int): # the str and int from python for type hunting it shows parameters datatypes of functions while calling
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative")
        else:
            print(name) 
            print(age)
            print("Updated into DB")
    else:
        raise TypeError("Incorrect datatype")
    
# we have checked the type using type guards in python but it is not scalable method we are repeating the validation and the values may be more than 2 
# and also if we we want to convert age datatype from int to str we have to change it in every function
    
# one more problem --> data validation like age can't be -ve


# In pydantic we create model and define its schema like name is string age is int and > 0
# we have a dictionary we pass it to pydantic to get pydantic validated obj 
# then we pass obj to our function 

from pydantic import BaseModel

class Patient(BaseModel):
    name: str 
    age: int 
    

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")


patient_info = {'name': 'nitish', 'age': 30}

patient1 = Patient(**patient_info) # ** is to unpack dictionary

insert_patient(patient1)