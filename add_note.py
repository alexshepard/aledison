#!/usr/bin/python

import yaml
config = yaml.safe_load(open("config.yml"))

from notes import Notes, Note
notebook = Notes()

import sys

if len(sys.argv) < 1:
	print("usage: add_note.py <text>")
	sys.exit()
filename = sys.argv.pop(0)
note_text = " ".join([str(x) for x in sys.argv])

if note_text != "":
  notebook.add_note(note_text)