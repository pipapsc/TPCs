def convInt(s):
    return int(s)

def getAtleta(texto): 
    # _id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado
    campos = texto.split((","))
    atleta = []
    atleta.append(campos[0]) # id
    atleta.append(campos[1]) # index
    atleta.append(campos[2]) # dataEMD
    atleta.append(campos[3]) # 1o nome
    atleta.append(campos[4]) # ultimo nome
    atleta.append(campos[5]) # idade
    atleta.append(campos[6]) # genero
    atleta.append(campos[7]) # morada
    atleta.append(campos[8]) # modalidade
    atleta.append(campos[9]) # clube
    atleta.append(campos[10]) # email
    atleta.append(campos[11]) # federado
    atleta.append(campos[12]) # resultado
    return atleta

def carregar():
    texto = open ("emd.csv")
    bd = []
    texto.readline()
    for linha in texto:
        bd.append(getAtleta(linha))
    return bd   

def contadorBD():
    contador = 0
    baseDados = []
    baseDados = carregar()
    for elemento in baseDados:
        contador += 1
    return contador
    
def listarDataset():
    BD = carregar()
    print("dataEMD   nome/primeiro   nome/último   idade   género   morada   modalidade   clube   email   federado   resultado")
    print("-------------------------------------------------------------------------------------------------------------------")
    for e in BD:
        print(e[2] + "|" + e[3] + e[4] + " | " + e[5] + " | " + e[6] + " | " + e[7] + " | " + e[8] + " | " + e[9] + " | " + e[10] + " | " + e[11] + " | " + e[12])


def modalidades():
    BD = carregar()
    listaModalidades = []
    for e in BD:
        modalidade = e[8]
        if modalidade not in listaModalidades:
            listaModalidades.append(modalidade)
    return listaModalidades

import matplotlib.pyplot as plt

def porModalidade():
    bd = carregar()
    distribuicaoModalidade = {}
    for a in bd:
        modalidade = a[8]
        if modalidade in distribuicaoModalidade.keys():
            distribuicaoModalidade[modalidade] = distribuicaoModalidade[modalidade] + 1
        else:
            distribuicaoModalidade[modalidade] = 1
    return distribuicaoModalidade  # {modalidade : numero de atletas}

def porAno():
    bd = carregar()
    distribuicaoAno = {}
    for a in bd:
        ano = a[5]
        if ano in distribuicaoAno.keys():
            distribuicaoAno[ano] = distribuicaoAno[ano] + 1
        else:
            distribuicaoAno[ano] = 1
    return distribuicaoAno  # {ano : numero de atletas}


def porClube():
    bd = carregar()
    distribuicaoClube = {}
    for a in bd:
        clube = a[9]
        if clube in distribuicaoClube.keys():
            distribuicaoClube[clube] = distribuicaoClube[clube] + 1
        else:
            distribuicaoClube[clube] = 1
    return distribuicaoClube     # {clube : numero de atletas}

def plotPorModalidade():
    distribuicao = porModalidade()
    # heights of bars
    modalidade = distribuicao.keys()
    height = []
    for m in modalidade :
        height.append(m) 
    # labels for bars
    numero_emd = distribuicao.values() #retorna lista com as chaves, nomne dos cursos
    x = []
    i = 1
    tick_label = []
    for emd in numero_emd:
        tick_label.append(emd)
        x.append(i)
        i = i+1
 
    # plotting a bar chart
    plt.bar(x,height, tick_label = tick_label, width = 0.8)
    # naming the x-axis
    plt.xlabel('Numero emd')
    # naming the y-axis
    plt.ylabel('Modalidades')
    # plot title
    plt.title('Distribuição por Modalidade')
    plt.show() 
 
def plotPorAno():
    distribuicao = porAno()
    # heights of bars
    ano = distribuicao.keys()
    height = []
    for a in ano :
        height.append(a) 
    # labels for bars
    numero_emd = distribuicao.values() #retorna lista com as chaves, nomne dos cursos
    x = []
    i = 1
    tick_label = []
    for emd in numero_emd:
        tick_label.append(emd)
        x.append(i)
        i = i+1
 
    # plotting a bar chart
    plt.bar(x,height, tick_label = tick_label, width = 0.8)
    # naming the x-axis
    plt.xlabel('Numero emd')
    # naming the y-axis
    plt.ylabel('Idade')
    # plot title
    plt.title('Distribuição por Idade')
    plt.show() 

def plotPorClube():
    distribuicao = porClube()
    # heights of bars
    clube = distribuicao.keys()
    height = []
    for c in clube :
        height.append(c) 
    # labels for bars
    numero_emd = distribuicao.values() #retorna lista com as chaves, nomne dos cursos
    x = []
    i = 1
    tick_label = []
    for emd in numero_emd:
        tick_label.append(emd)
        x.append(i)
        i = i+1
 
    # plotting a bar chart
    plt.bar(x,height, tick_label = tick_label, width = 0.8)
    # naming the x-axis
    plt.xlabel('Numero emd')
    # naming the y-axis
    plt.ylabel('Clube')
    # plot title
    plt.title('Distribuição por Clube')
    plt.show() 

