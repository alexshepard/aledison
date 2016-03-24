#!/usr/bin/python

import yaml
config = yaml.safe_load(open("config.yml"))

from notes import Notes
notebook = Notes()

import sys

if len(sys.argv) < 2:
  print("usage: delete_note.py <number>")
  sys.exit()

script_name = sys.argv.pop(0)
note_index = int(sys.argv.pop(0))

if note_index == 0:
  print "No note #0 found. Start counting with 1 like a normal person."
elif note_index < 0:
  print "Please try to stay positive."
elif note_index > len(notebook.get_notes()):
  print "You fell off the edge. There aren't that many notes."
else:
  notebook.delete_note(int(note_index) - 1)