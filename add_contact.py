#!/usr/bin/python

import yaml
config = yaml.safe_load(open("config.yml"))

from contacts import Contacts, Contact
c = Contacts()

# syntax: add_contact.py <name> <number>
import sys

if len(sys.argv) < 2:
	print("usage: add_contact.py <name> <number>")
	sys.exit()
script_name = sys.argv.pop(0)
name = sys.argv.pop(0)
number = sys.argv.pop(0)

if len(number) < 11:
	print("number must be in the format 12062551028 or +12062551028")
	sys.exit()

if number[0] != "+":
	number = "+" + number

contact = c.find_contact_by_name(name)
if contact:
	print("already have a contact named " + name)
	sys.exit()
else:
	new_contact = Contact(name, number)
	c.add_contact(new_contact)

