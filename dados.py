import SimpleFile as SF
import time
def input_error(conteudo,letras,separacao,maior):
    valor = ""
    while(True):
        valor = input(conteudo)
        if(separacao == "caractere"):
            palavras = list(valor)
        elif(separacao == "palavra"):
            palavras = valor.split()

        if maior == True:
            if len(palavras) <letras:
                    print("Erro, digite novamente")
            else: 
                break
        else:
            if len(palavras) >letras:
                    print("Erro, digite novamente")
            else: 
                break
    return valor

def criar_cadastro(lines,arquivo):
    nome = input_error("Digite seu nome: ",1,"palavra",True)
    idade = int(input_error("Digite sua idade: ",3,"caractere",False))
    cpf = input_error("Digite seu CPF: ",11,"caractere",True)
    rg = input_error("Digite seu RG: ",9,"caractere",True)
    linha2 = "----identicacao----"
    linha3 = "Nome: "+str(nome)
    linha4 = "Idade: "+str(idade)
    linha5 = "CPF: "+cpf 
    linha6 = "RG: "+rg

    for x in range(arquivo.line_numbers()):
        linha = arquivo.read_line(x).strip()
        if linha3 == linha:
            raise ValueError("Usuário cadastrado já existente.")
    
    arquivo.append(linha2)
    arquivo.append(linha3)
    arquivo.append(linha4)
    arquivo.append(linha5)
    arquivo.append(linha6)
    lines = arquivo.line_numbers()
    cont = lines/4
        
    print("Quantidade de pessoas: ",cont)
    print("Fim")
def verificar_pessoa(arquivo,linha,ind1,ind2):
    for x in range(linha+ind1,linha+ind2):
        print(arquivo.read_line(x))
#for x in range(2,arquivo.line_numbers(),5): -1 +4

def opcao_de_verificacao(arquivo,inicio,requisicao):
    ind1 = inicio - 1
    ind2 = 5 - inicio + 1
    pergunta = input("Qual cadastro você quer ver? ")
    ident = requisicao+pergunta 
    encontrado = False
    for x in range(inicio,arquivo.line_numbers()+5,5):
        if ident == arquivo.read_line(x).strip():
            verificar_pessoa(arquivo,x,-ind1,ind2)
            break
    deseja_continuar()
        
#----
def ver_cadastros(arquivo):
    pergunta = input("Você quer procurar por nome,idade,cpf,rg,numeração: ")
    if pergunta == "numeração":
        pergunta = input("Qual cadastro você quer ver? ")
        pergunta = int(pergunta) * 5
        print("\n")
        verificar_pessoa(arquivo,pergunta,-4,0)
    elif pergunta == "nome":
        opcao_de_verificacao(arquivo,2,"Nome: ")
    elif pergunta == "idade":
        opcao_de_verificacao(arquivo,3,"Idade: ")
    elif pergunta == "cpf":
            opcao_de_verificacao(arquivo,4,"CPF: ")
    elif pergunta == "rg":
        opcao_de_verificacao(arquivo,5,"RG: ")
    deseja_continuar()

def encontrar_chave_por_valor(dicionario, valor_procurado):
    for chave, valor in dicionario.items():
        if valor == valor_procurado:
            return chave
    return None  # Retorna None se o valor não for encontrado

def mudar_linguagem(arquivo,linguagem):
    linguagem = input("Você deseja mudar a linguagem para portugues ou ingles?")
    if linguagem == "ingles":
        linguagem = "ing"
        for x in range(len(arquivo.all_lines())):
            time.sleep(0.1)
            lista = arquivo.read_line(x)
            lista = lista.strip()
            lista = lista.split()
            palavras = traducao.keys()
            for xx in lista:
                for yy in palavras:
                    if xx == yy:
                        ind = lista.index(xx)
                        lista[ind] = traducao[yy]
                        print(lista[ind])
            lista = ' '.join(lista)
            arquivo.replace(x,lista)
    elif linguagem == "portugues":
        linguagem = "pt"
        for x in range(len(arquivo.all_lines())):
            time.sleep(0.1)
            lista = arquivo.read_line(x)
            lista = lista.strip()
            lista = lista.split()
            palavras = traducao.values()
            for xx in lista:
                for yy in palavras:
                    if xx == yy:
                        ind = lista.index(xx)
                        lista[ind] = encontrar_chave_por_valor(traducao,yy)
                        print(lista[ind])
            lista = ' '.join(lista)
            arquivo.replace(x,lista)
    deseja_continuar(linguagem)
        

def deseja_continuar(linguagem):
    pergunta = input("deseja continuar? ")
    if(pergunta in ["Sim","sim","Si","si","S","s","ss","SS"]):
        opcoes_iniciais(arquivo,linguagem)

def opcoes_iniciais(arquivo,linguagem):
    print("Quais são suas opções:\n 1 - Ver cadastros \n 2 - Fazer cadastro\n 3 - Sair\n 4 - Mudar linguagem")
    print(linguagem)
    op = input_error("Digite a numeração da opção: ",2,"caractere",False)
    if(op == "1"):
        ver_cadastros(arquivo) 
    elif(op == "2"):
        lines = arquivo.line_numbers()
        criar_cadastro(lines,arquivo)
    elif(op == "3"):
        print("fim do programa")
    elif(op == "4"):
        mudar_linguagem(arquivo,linguagem)

    

#arquivo
arquivo = SF.File("Dados")
arquivo.create()


traducao={
    "Nome:":"Name:",
    "Idade:":"Age:",
    "----identicacao----":"----identification----"
}

#calculo de pessoas
linguagem = "pt"
opcoes_iniciais(arquivo,linguagem)

#pegar uma linha com for
#armazenar as palavras numa lista
#traduzi-las
#subistitui-las no mesmo local