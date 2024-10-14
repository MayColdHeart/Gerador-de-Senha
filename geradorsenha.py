import random
import string
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

random.seed 

combinacao_1 = random.randint(0, 100)
combinacao_2 = random.randrange(101, 150)
combinacao_3 = random.randint(200, 300)
combinacao_4 = random.randint(400, 540)
combinacao_5 = random.choice(string.ascii_letters)
combinacao_6 = random.choice(string.ascii_letters)
combinacao_7 = random.choice(string.ascii_letters)

print("\n")
print(f'Senha adquirida: {combinacao_2}{combinacao_6}{combinacao_7}{combinacao_4}{combinacao_3}{combinacao_1}{combinacao_5}')