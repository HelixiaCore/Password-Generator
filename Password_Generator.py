# My Project is Password Generator since 9/8/2026

import random

numbers = '0123456789'
capital_charectors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minimal_charectors = 'abcdefghijklmnopqrstuvwxyz'
symboles = '#$%_&@'

all_charectors = numbers + capital_charectors + minimal_charectors + symboles

lenght_password = int(input("please enter lenght Password: "))

pasword=""
for i in range(lenght_password):
    pasword += random.choice(all_charectors)

print(f"\nThank you :) The password is: {pasword}")