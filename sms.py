#!/usr/bin/env python
# Sample script to show how to send SMS

from __future__ import print_function
import gammu
import sys

# Create object for talking with phone
state_machine = gammu.StateMachine()

# Load config file
state_machine.ReadConfig()

# Connect to the phone
state_machine.Init()

# Prepare message data
# We tell that we want to use first SMSC number stored in phone
message = {
    'Text': 'python-gammu testing message',
    'SMSC': {'Location': 1},
    'Number': '18195708580',
}

# Actually send the message
#state_machine.SendSMS(message)

while True:
	test = state_machine.GetNextSMS(1, 0, 1)
	
	if test:
		print(test)
		state_machine.DeleteSMS(0)
	
	
