from typing import TypedDict

class Person(TypedDict):

    name : str
    age : int

new_person: Person = {'name':'Aditya', 'age': 21}

print(new_person)

# But even if you give value differently, still it will work and won't throw error
new_person: Person = {'name':'Aditya', 'age': '21'}

print(new_person)
