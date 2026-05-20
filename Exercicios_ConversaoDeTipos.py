#Exercicios - Conversão De Tipos

# EX1
# O usuário digitou "25" como sua idade em um formulário.
# Converta para inteiro e calcule a idade que ele terá
# daqui a 5 anos.

print("\n\n")
print("======== EXERCICIO 1 ========")
print("\n\n")
idade_texto = 20
idade = int(idade_texto)
idade_futura = idade + 5
print(idade_futura)

# EX2
# Converta o número de ponto flutuante 7.999
# para inteiro e observe o resultado.

print("\n\n")
print("======== EXERCICIO 2 ========")
print("\n\n")
flutuante = float(7.999)
float_inteiro = int(flutuante)
print(float_inteiro)

# EX3
# Converta a string "-3.14" para float
# e multiplique o resultado por 2.

print("\n\n")
print("======== EXERCICIO 3 ========")
print("\n\n")
string = str(-3.14)
string_float = float(string)
resultado = string_float * 2
print(resultado)

# EX4
# Tente converter a string "cento e vinte"
# para inteiro e observe o que acontece.

#Ao tentar converter a string "cento e vinte" para inteiro em Python, ocorre um erro porque a função int() só consegue converter strings que representam números em formato numérico, como "120"

# EX5
# Converta o número 42 para string
# e concatene com a palavra " respostas".

print("\n\n")
print("======== EXERCICIO 5 ========")
print("\n\n")
numero = 42
numero_em_txt = str(numero)
resultado = numero_em_txt + " respostas"
print(resultado)

# EX6
# Use a função complex() para criar
# um número complexo com parte real 3
# e parte imaginária 5.

print("\n\n")
print("======== EXERCICIO 6 ========")
print("\n\n")
numero_complex = complex(3, 5)
print(numero_complex)


# EX7
# Converta o número 0 para booleano
# e mostre o resultado.

print("\n\n")
print("======== EXERCICIO 7 ========")
print("\n\n")
num = bool(0)
print(num)

# EX8
# Converta o número -100 para booleano
# e mostre o resultado.,

print("\n\n")
print("======== EXERCICIO 8 ========")
print("\n\n")
num = bool(-100)
print(num)

# EX9
# Converta o número 3.1415 para inteiro
# e depois para string, tudo em uma única linha.

print("\n\n")
print("======== EXERCICIO 9 ========")
print("\n\n")
resultado = str(int(3.1415))
print(resultado)
print(type(resultado))

# EX10
# Some um número inteiro (5) com um float (2.3)
# e verifique qual é o tipo do resultado.

print("\n\n")
print("======== EXERCICIO 10 ========")
print("\n\n")
resultado = 5 + 2.3
print(resultado)
print(type(resultado))