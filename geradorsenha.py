import random
import string

digits = string.ascii_lowercase + string.ascii_uppercase + string.digits
simb = ['@','!','$']

passwordRandom = (''.join(random.sample(digits, 9)))


print (''.join('%s%s' % (x,random.choice(simb) if random.random() > 0.8 else '') for x in passwordRandom))