from dataclasses import field
from datetime import datetime
from pydantic import BaseModel, ValidationError, field_validator, model_validator
from typing import Dict


class Student(BaseModel):
    name: str
    age : int

try:
    student = Student(name="wwww", age="12")
except ValidationError as error:
    print(error.json())

class Item(BaseModel):
    item_name: str
    description: str
    unit: str
    quantity: int

class Invoice(BaseModel):
    invoice_no : str
    invoice_date: str
    items : Dict[str, Item]

    @field_validator('invoice_date')
    def validate_invoice_date(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError('invoice_date must be in DD-MM-YYYY format')
        return value

    @field_validator("items", mode="before")
    def validate_items(cls, values):
        values['name'] = values.get('name', '').strip().title()
        return values

try:
    invoice = Invoice(invoice_no = "JD-1234", invoice_date = "2025-10-21", items= {})
except ValidationError as error:
    print(error.json(indent=4))
