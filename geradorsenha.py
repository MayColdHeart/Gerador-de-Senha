import random
import string

digits = string.ascii_lowercase + string.ascii_uppercase + string.digits


print(''.join(random.sample(digits, 16)))
