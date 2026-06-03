from pydantic import BaseModel

class Note(BaseModel):
    title: str
    desc: str
    important: bool = None

'''
Pydantic is the most widely used data validation and serialization library 
for Python. It leverages Python type hints to enforce data structures at runtime,
ensuring that data conforms to specific formats before it is proccessed by an application. 
'''




