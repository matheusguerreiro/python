# Aula 11 (Cores no Terminal)

# \033[style:text:backm
#        0    30   40    standard   white
#        1    31   41    bold       red
#        4    32   42    underline  green
#        7    33   43    negative   yellow

print('\033[0:32mMatheus\033[m \033[0:33mGuerreiro\033[m \033[0:31mFerreira\033[m')

# Outra forma

nome = str(input('Nome: '))
print('{}{}{}'.format('\033[0:31m', nome, '\033[m'))

# Outra forma

cores = {'limpa':'\033[m', 'red':'\033[31m', 'green':'\033[32m', 'yellow':'\033[33m'}
print('{}{}{}'.format(cores['yellow'], nome, cores['limpa']))
