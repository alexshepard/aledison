#!/usr/bin/python

import yaml
config = yaml.safe_load(open("config.yml"))

twilio_account_sid = config["twilio"]["account_sid"]
twilio_auth_token = config["twilio"]["auth_token"]

from twilio.rest import TwilioRestClient
twilio_client = TwilioRestClient(twilio_account_sid, twilio_auth_token)

from contacts import Contacts, Contact
c = Contacts()

def name_or_number(number):
	contact = c.find_contact_by_number(number)
	if contact:
		return contact.name
	else:
		return number

messages = twilio_client.messages.list()
for message in twilio_client.messages.list():
	print("From: " + name_or_number(message.from_.encode("utf-8")))
	print("To: " + name_or_number(message.to.encode("utf-8")))
	print("Body: " + message.body.encode("utf-8"))
	print

