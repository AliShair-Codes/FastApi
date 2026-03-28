# how to export pydantic model object as python dict or as a json

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str 

class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}
address1 = Address(**address_dict)
patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}
patient1 = Patient(**patient_dict)

# temp = patient1.model_dump() # convert pydantic object to python dict
# temp = patient1.model_dump(include=['name', 'gender']) # only export name and gender
# temp = patient1.model_dump(
#     exclude={ # to exclude field it exclude state and age
#         'age': True,
#         'address': {'state': True}
#     }
# ) 
# temp = patient1.model_dump_json() # convert pydantic object to json

temp = patient1.model_dump(exclude_unset=True) # patient_dict obj banatay waqt jo cheezain set naahi ki gai han wo export nahi ho gi
print(patient1)
print(type(patient1))
print(temp)
print(type(temp))

