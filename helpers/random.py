import random
import string

def gerar_caracteres_aleatorios(comprimento):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(comprimento))
