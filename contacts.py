#!/usr/bin/python

import os.path
import pickle
import yaml
config = yaml.safe_load(open("config.yml"))
contacts_filename = config["contacts"]["filename"]

class Contacts:
  """An address book, with entries for people."""

  def get_contacts(self):
    if (os.path.isfile(contacts_filename)):
      return pickle.load(open(contacts_filename, "rb"))
    else:
      return []

  def save_contacts(self, contacts):
    pickle.dump(contacts, open(contacts_filename, "wb"))

  def add_contact(self, contact):
    contacts = self.get_contacts()
    contacts.append(contact)
    self.save_contacts(contacts)

  def delete_contact(self, contact):
    contacts = self.get_contacts()
    for candidate in contacts:
      if candidate.name == contact.name and candidate.number == contact.number:
        contacts.remove(candidate)
        self.save_contacts(contacts)
        return True
    return False

  def find_contact_by_number(self, number):
    for contact in self.get_contacts():
      if contact.number == number:
        return contact
    return None

  def find_contact_by_name(self, name):
    for contact in self.get_contacts():
      if contact.name == name:
        return contact
    return None

class Contact:
  """ A data structure encapsulating a person. """

  # default data
  name = "Nobody"
  number = "+19856552500"     # rickroll

  def __init__(self, name, number):
    self.name = name
    self.number = number
    