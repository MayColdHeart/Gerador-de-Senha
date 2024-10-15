import random
from random import randint
import string

text = input('any name: ')

digits = string.ascii_lowercase + string.ascii_uppercase + string.digits + text
simb = ['@','!','$']

position = randint(4, 12)
passwordRandom = (''.join(random.sample(digits, position)))


passwordPrimary = (''.join('%s%s' % (x,random.choice(simb) if random.random() > 0.5 else '') for x in passwordRandom))
passwordComplete = (''.join('%s%s' % (y, random.choice(text) if random.random()> 0.8 else '') for y in passwordPrimary))


def passwordLevels():
    qtd = len(passwordComplete)

    if qtd < 8:
        return "low"
    elif qtd < 12:
        return "medium"
    else: qtd < 16 
    return "high"  

level = passwordLevels()

print(f'Your new password: {passwordComplete}')
print(f'Password level: {level} ')