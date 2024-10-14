import random
from random import randint
import string


digits = string.ascii_lowercase + string.ascii_uppercase + string.digits
simb = ['@','!','$']

position = randint(4, 16)
passwordRandom = (''.join(random.sample(digits, position)))


passwordComplete = (''.join('%s%s' % (x,random.choice(simb) if random.random() > 0.8 else '') for x in passwordRandom))


def passwordLevels():
    qtd = len(passwordComplete)

    if qtd < 8:
        return "low"
    elif qtd < 12:
        return "medium"
    else: qtd < 16 
    return "high"  

level = passwordLevels()

print(passwordComplete)
print(f'Password level: {level} ')