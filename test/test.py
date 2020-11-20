from pushbullet import Pushbullet
import random
import string

# installare pus
# pip install pushbullet.py
# pb.device
api_key = 'o.CkIlmNVhzonrvkoaS93hiODpbUtA4Qy7'
pb = Pushbullet(api_key)

# print(pb.devices)
device = pb.devices[0]

length = 8
# put your letters in the following string
# letters_and_digits = string.ascii_letters.upper + string.digits
result_str = ''.join((random.choice(string.ascii_uppercase + string.digits) for i in range(length)))
# print("Random string is:", result_str)
# prende il cell personale
push = pb.push_sms(device, "+393516448921", "Codice adesione " + result_str)

