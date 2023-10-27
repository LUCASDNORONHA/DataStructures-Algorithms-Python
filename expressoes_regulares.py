# Expressões Regulares Revisão

import re

frase1 = 'Olá, meu número de telefone é (42)00000-0000'
frase2 = 'A placa de carro que eu anotei durante o acidente foi FRT-1998'
frase3 = 'Entre em contato, meu email é teste@teste.com'
frase4 = '(42)00000-0000 é o meu número'
frase5 = 'FRT-1998 é a placa'
frase6 = 'Olá, meu número de telefone é (42)00000-0000. O número (56)11111-1111 não é meu.'
# Função search

# Procura o padrão definido no texto, se não retorna None.
print(re.search(r'\(\d{2}\)\d{4,5}-\d{4}', frase1))
print(re.search('[A-Za-z]{3}-\d{4}', frase2))
print(re.search('\w+@\w+\.\w+', frase3))

# Função match

# Procura o padrão no inicio do texto, se não retorna None
print(re.match(r'\(\d{2}\)\d{4,5}-\d{4}', frase4))
print(re.match('[A-Z]{3}-\d{4}', frase5))
print(re.match('\w+@\w+\.\w+', frase3))

# Função findall

# Procura mais de um valor padrão.
print(re.findall(r'\(\d{2}\)\d{4,5}-\d{4}', frase6))

emails = '''
Nome: Teste 1
Email: teste1@teste.com
Mome: teste 2
Email: teste2@teste.com
Nome: teste 3
Email: teste3@teste.com.br
'''
print(re.findall('\w+@\w+\.\w+', emails))