from pydantic import BaseModel
# # simple one
# class Student(BaseModel):  ### Base model is used to create pydantic objects
#     name : str

# new_student  = {'name' : 'Aditya'} ## now if yo will try to give name as any other data type, it will throw an error.

# student = Student(**new_student)

# print(student)

#-------------------------------------------------------------------------------
# # with Default values
# class Student(BaseModel):  ### Base model is used to create pydantic objects
#     name : str = 'Sirish'

# new_student  = {} ## now it will give default Values

# student = Student(**new_student)

# print(student)

#-------------------------------------------------------------------------------
# # with optional values
# from typing import Optional

# class Student(BaseModel):  ### Base model is used to create pydantic objects
#     name : str = 'Sirish'
#     age : Optional[int] = None
# new_student  = {'name' : 'Aditya', 'age' : 21} ## now it will give default Values

# student = Student(**new_student)

# print(student)


#-------------------------------------------------------------------------------
# # Pydantic is smart and it will implicitly convert types when required
# from typing import Optional

# class Student(BaseModel):  ### Base model is used to create pydantic objects
#     name : str = 'Sirish'
#     age : Optional[int] = None
# new_student  = {'age' : '34'} ## now it will typeconvert to integer Value

# student = Student(**new_student)

# print(student)

#-------------------------------------------------------------------------------
# # Builtin Validation :  Pydantic also have a built in email datatype which validate emails
# from pydantic import BaseModel, EmailStr
# from typing import Optional

# class Student(BaseModel):  ### Base model is used to create pydantic objects
#     name : str = 'Sirish'
#     age : Optional[int] = None
#     email : EmailStr 

# new_student  = {'age' : '34', 'email':'abc@gmail.com'} ## now it have email address as well

# student = Student(**new_student)

# print(student)

# #-------------------------------------------------------------------------------
# # Field Function : with this we can set default values, constraints, give description, and use regex expressions
# from pydantic import BaseModel, EmailStr, Field
# from typing import Optional

# class Student(BaseModel):  ### Base model is used to create pydantic objects
#     name : str = 'Sirish'
#     age : Optional[int] = None
#     email : EmailStr 
#     cgpa  : float = Field(gt= 0, lt= 10, default=5, description="Represents the overall Cgpa of Student") ## Gt-Greater than, lt-lesser than, we can define any of these parameter or all the parameters

# new_student  = {'age' : '34', 'email':'abc@gmail.com', 'cgpa' : 8.9} 

# student = Student(**new_student)

# print(student)

#-------------------------------------------------------------------------------
# We can also type convert the pydantic object to dictionary or json format
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):  ### Base model is used to create pydantic objects
    name : str = 'Sirish'
    age : Optional[int] = None
    email : EmailStr 
    cgpa  : float = Field(gt= 0, lt= 10, default=5, description="Represents the overall Cgpa of Student") 

new_student  = {'age' : '34', 'email':'abc@gmail.com', 'cgpa' : 8.9} 

student = Student(**new_student)

dict_stud = dict(student)

print(dict_stud['age'])

json_stud = student.model_dump_json()
print(json_stud)
