from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    # name:str
    #settig default value
    name:str = 'Preet'
    age:Optional[int] = None
    email:EmailStr
    #gt = greaterthan, lt = lessthan
    cgpa:float = Field(gt=0 ,lt=10,default=5,description='Decimal value representing cgpa of a student')

    
    

# new_student = {'name':'Preet'}
new_student = {'age':'32','email':'abc@gmail.com'}
# new_student = {'name':32}  error aayga type should be string
student = Student(**new_student)

student_dict = dict(student)
student_json = student.model_dump_json()

print(student)