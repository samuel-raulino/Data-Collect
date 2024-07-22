import SimpleFile as SF

def criar_cadastro(lines,arquivo):
    nome = input()
    idade = int(input())
    linha1 = ""
    linha2 = "----Identificação----"
    linha3 = "nome: "+str(nome)
    linha4 = "idade: "+str(idade)

    for x in range(arquivo.line_numbers()):
        linha = arquivo.read_line(x).strip()
        if linha3 in linha:
            raise ValueError("Erro: Cadastro duplicado.")
        
    arquivo.append(linha1)
    arquivo.append(linha2)
    arquivo.append(linha3)
    arquivo.append(linha4)
    
arquivo = SF.File("dados")
arquivo.create()
lines = arquivo.line_numbers()

criar_cadastro(lines,arquivo)
lines = arquivo.line_numbers()
cont = -1


for x in range(lines):
    
    if arquivo.read_line(x) == arquivo.read_line(2):
        cont+=1
print("quantidade de pessoas: ",cont)
print("fim")