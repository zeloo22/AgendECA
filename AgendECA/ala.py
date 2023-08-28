txt = open("arquivo.txt", "r")
linha = txt.readlines()
nome = 'caio'
numero = '123123'
nomet = "twolala"
numerot = "707070"
cont= 0
for i in linha:
    if i.strip('\n') == f"nome: {nome}, telefone: {numero}":
        linha[cont] = f"nome: {nomet}, telefone: {numerot}\n"
    cont+= 1
txw = open("arquivo.txt", "w")
for i in linha:
    txw.write(i)
print("alterado")