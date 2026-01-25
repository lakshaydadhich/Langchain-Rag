from typing import TypedDict
class Person(TypedDict):
    name:str
    age:int

#new_person: Person={'name':'lakshay','age':12}
new_person=Person({'name':'lakshay','age':12})
print(new_person)