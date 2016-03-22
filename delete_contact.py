#!/usr/bin/python

import yaml
config = yaml.safe_load(open("config.yml"))

from contacts import Contacts, Contact
c = Contacts()

# syntax: add_contact.py <name> <number>
import sys

if len(sys.argv) < 2:
  print("usage: delete_contact.py <name>")
  sys.exit()

script_name = sys.argv.pop(0)
name = sys.argv.pop(0)

contact = c.find_contact_by_name(name)
if contact:
  c.delete_contact(contact)
else:
  print("no contact named " + name)
  sys.exit()
