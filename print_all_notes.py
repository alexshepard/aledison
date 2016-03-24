#!/usr/bin/python

import yaml
config = yaml.safe_load(open("config.yml"))
dt_format = config["global"]["dt_format"]

from notes import Notes, Note
notebook = Notes()

import sys

all_notes = notebook.get_notes()

for note in all_notes:
  print("Note #" + str(all_notes.index(note) + 1))
  print("Text: " + note.text)
  print("Date: " + note.date.strftime(dt_format))
  print

