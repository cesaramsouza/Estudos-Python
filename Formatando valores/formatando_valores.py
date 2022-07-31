"""""
Formatando valores com modificadores

:s - string
:d - int
:f - float
:.'numero de casas decimais'f - quantidade de casas decimais(float)
:'caractere de preenchimento''> ou < ou ^''quantidade' 'tipo - s,d ou f'

> - esquerda
< - direita
^ - Centro

"""""

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0^10}')

num_3 = 1150
print(f'{num_2:0>10.2f}')