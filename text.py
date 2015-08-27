#!/usr/bin/python

import yaml
config = yaml.safe_load(open("config.yml"))

twilio_account_sid = config["twilio"]["account_sid"]
twilio_auth_token = config["twilio"]["auth_token"]
twilio_from_number = config["twilio"]["from_number"]

from twilio.rest import TwilioRestClient
twilio_client = TwilioRestClient(twilio_account_sid, twilio_auth_token)

from contacts import Contacts, Contact
c = Contacts()

# syntax: text.py <contact> <message>
import sys
script_name = sys.argv.pop(0)
name = sys.argv.pop(0)
msg = " ".join([str(x) for x in sys.argv])

contact = c.find_contact_by_name(name)
if contact:
	print("from " + str(twilio_from_number))
	message = twilio_client.messages.create(
		body=msg, 
		from_=twilio_from_number,
		to=contact.number 
	)

	print("message is " + message.sid)
else:
	print("couldn't find contact '" + name + "'")


