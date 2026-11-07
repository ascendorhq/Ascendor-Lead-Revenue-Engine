"""
Ascendor data models.

This module defines the data structures
used by the application.
"""

class Lead:
"""Represent a business lead."""

def __init__(  
    self,  
    name,  
    email,  
    phone=None,  
    company=None,  
    source=None,  
):  
    self.name = name  
    self.email = email  
    self.phone = phone  
    self.company = company  
    self.source = source