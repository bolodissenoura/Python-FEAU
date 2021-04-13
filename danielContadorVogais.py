print("================================================")
print("Contador de VOGAIS e CONSOANTES - Daniel Alves Lima e Silva. 02010686")
print("================================================")

while True:
    try:
        x = int(input('Quantas letras terá?:  '))
    except ValueError:
        print("Por favor, coloque uma resposta em números.")
    else:
        break

lista0 = []
lista1 = []
lista2 = []
consoant = []

i = 1

lista0 = []
lista1 = []
lista2 = []
consoant = []
for n in range (0, 10):
    lista1.append(str(input(f'Coloque a {n+1}º letra: '.lower())))
    if lista1[n] == 'a' or lista1[n] == 'A':
        lista2.append(lista1[n].lower())
    elif lista1[n] == 'e' or lista1[n] == 'E':
        lista2.append(lista1[n].lower())
    elif lista1[n] == 'i' or lista1[n] == 'I':
        lista2.append(lista1[n].lower())
    elif lista1[n] == 'o' or lista1[n] == 'O':
        lista2.append(lista1[n].lower())
    elif lista1[n] == 'u' or lista1[n] == 'U':
        lista2.append(lista1[n].lower())
    else:
        consoant.append(lista1[n].lower())
for n in range (0, 10):
   lista0.append(lista1[n].lower())
print("================================================")
print(f'As letras digitadas foram : {lista0} ')
print(f"O total de letras digitadas foram: {len(lista0)} ")
print("================================================")
print(f'As consoantes foram: {consoant}')
print(f"O total de CONSOANTES foram: {len(consoant)} ")
print("================================================")
print(f'As vogais foram: {lista2}')
print(f"O total de VOGAIS foram: {len(lista2)} ")
print("================================================")

input()
        
