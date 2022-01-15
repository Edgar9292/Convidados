
numero_convidados = input('Coloque o numero de convidados: ')
lista_convidados = []

i = 1
while i <= int(numero_convidados):
    nome_convidado = input('Coloque o nome do convidado #{}: '.format(str(i)))
    lista_convidados.append((nome_convidado))
    i +=1
print('Serão convidados {} pessoas'.format(numero_convidados))
print('\n LISTA DE CONVIDADOS')
for convidado in lista_convidados:
    print(convidado)

