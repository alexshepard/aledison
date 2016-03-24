#!/usr/bin/python

from datetime import datetime
import os.path
import pickle
import yaml
config = yaml.safe_load(open("config.yml"))
notes_filename = config["notes"]["filename"]

class Notes:
  """A notebook."""

  def get_notes(self):
    if (os.path.isfile(notes_filename)):
      return pickle.load(open(notes_filename, "rb"))
    else:
      return []

  def save_notes(self, notes):
    pickle.dump(notes, open(notes_filename, "wb"))

  def add_note(self, note_text):
    note = Note(note_text)
    note.date = datetime.now()
    notes = self.get_notes()
    notes.append(note)
    self.save_notes(notes)

  def delete_note(self, note_index):
    notes = self.get_notes()
    note_to_delete = notes[note_index]
    notes.remove(note_to_delete)
    self.save_notes(notes)

class Note:
  """ A data structure encapsulating a note. """

  # default data
  text = ""

  def __init__(self, text):
    self.text = text
    