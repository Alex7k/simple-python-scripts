import random

length = 16
symbols = list("""1234567890°+"*ç%&/()=?`§`üäö$è!£àé-.,_:;<>\\}{][~´¦@#°¬|¢qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM""") # characters typable with Swissgerman keyboard layout

password = ""
for i in range(length):
  password += random.choice(symbols) # random.choice() selects random object from the array

print("Password: " + password)