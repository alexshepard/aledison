#!/usr/bin/python

import yaml
config = yaml.safe_load(open("config.yml"))

from contacts import Contacts, Contact
c = Contacts()

# syntax: list_contacts.py
import sys

for contact in c.get_contacts():
  print("Name: " + contact.name)
  print("Number: " + contact.number)
  print

