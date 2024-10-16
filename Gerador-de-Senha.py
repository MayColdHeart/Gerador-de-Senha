import random
from random import randint
import string

text = input('Choice a name: ')


digits = string.ascii_lowercase + string.ascii_uppercase + string.digits + text
simb = ['@','!','$']

position = randint(4,8)
passwordRandom = (''.join(random.sample(digits, position)))


passwordPrimary = (''.join('%s%s' % (x,random.choice(simb) if random.random() > 0.8 else '') for x in passwordRandom))
passwordComplete = (''.join('%s%s' % (y, random.choice(text) if random.random()> 0.8 else '') for y in passwordPrimary))


def PasswordQtdLevels():
    qtd = len(passwordComplete)
    if qtd < 8:
        return "Small"
    elif qtd < 12:
        return "Medium"
    else: qtd < 16 
    return "Big"  
size = PasswordQtdLevels()

def security():
    key = passwordComplete
    simbol = '@!$'
    for special in key:
        if special in simbol:
            return "Safe"
    return "Weak"
sec = security()


print("-------------------------------------------------------------------------------------------------")
print(f'Your new password: {passwordComplete}')
print(f'Password size: {size} ')
print(f'password: {sec}')