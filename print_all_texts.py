#!/usr/bin/python

import yaml
from pytz import timezone
import pytz

config = yaml.safe_load(open("config.yml"))

my_timezone = timezone(config["global"]["timezone"])
utc = pytz.utc
dt_format = config["global"]["dt_format"]

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
for message in reversed(twilio_client.messages.list()):
  print("From: " + name_or_number(message.from_.encode("utf-8")))
  print("To: " + name_or_number(message.to.encode("utf-8")))
  # twilio messages are naive utc dates
  utc_date_sent = utc.localize(message.date_sent)
  local_date_sent = utc_date_sent.astimezone(my_timezone)
  print("Date: " + local_date_sent.strftime(dt_format))
  print("Body: " + message.body.encode("utf-8"))
  print

