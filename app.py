import random
import string

def auto():
	keygen = (string.ascii_letters + string.digits)
	randomator = [("".join(random.choice(keygen))) for i in range(8)]
	return ("".join(randomator))

print(auto())