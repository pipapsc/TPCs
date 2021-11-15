print("""Menu:
        (1) Criar Polinomio
        (2) Calcular Polinomio
        (3) Calcular Tabela
        (4) Simplificar Polinomio
        (5) Derivar Polinomio
        (0) Sair""")

def sair():
    print("That's all folks :)))")

def criarTermo():
    coeficiente = int(input("Introduza o coeficiente: "))
    expoente = int(input("Introduza o expoente: "))
    t = (coeficiente, expoente)
    return t

def criarPolinomio():
    n = int(input("Insira o comprimento do polinómio: "))
    pol = []
    i = 0
    while i < n:
        pol.append(criarTermo())
        i += 1
    return pol

def verTermo(t):
    c, e = t
    return str(c)+'x^'+str(e)

def verPolinomio(p):
    res = ""
    for t in p:
        if res == "":
            res = verTermo(t)
        else:
            res = res + " + " + verTermo(t)
    print(res)
    
def calcularTermo(t, x):  
    c, e = t
    res = c*(x**e)
    return res

def calculaPolinomio(p, x):
    resFinal = 0
    for t in p:
        polRes = calcularTermo(t, x)
        resFinal += polRes
    print(resFinal)
    
def calculaTabela(p, nLinhas):
    for i in range(nLinhas + 1):
        print(str(i) + " .... " + str(calculaPolinomio(p, i)))

def ordenaPolinomio(p):
    i = 0
    c, e = p[i]
    for t in p:
        if p[i+1][1] > p[i][1] :
            a = p[i+1]
            p[i+1] = p[i]
            p[i] = a
        
    return p

def simplificaPolinomio(p):
    i = 0
    c, e = p[i]
    novaLista = []
    for t in p:
        if p[i+1][1] == p[i][1]:
            termoSomado = (p[i + 1][0] + p[i][0], p[i][1])
            novaLista.append(termoSomado)
        else:
            novaLista.append(p[i])
    return novaLista
            
def derivarPolinomio(p):
    res = []
    for (c,e) in p:
        if e > 1:
            res.append((c*e, e-1))
    return res
        
def opcao():
    op = str(input("Insira um dos comandos do menu: "))
    while op != '0':
        if op == '1':
            polinomio = criarPolinomio()
            verPolinomio(polinomio)
        elif op == '2':
            x = int(input("Insira o valor de X: "))
            calculaPolinomio(polinomio, x)
        elif op == '3':
            numeroLinhas = int(input("Insira o numero de Linhas: "))
            calculaTabela(polinomio, numeroLinhas)
        elif op == '4':
            polinomioOrdenado = ordenaPolinomio(polinomio)
            polinomioSimplificado = simplificaPolinomio(polinomioOrdenado)
            verPolinomio(polinomioOrdenado)
            verPolinomio(polinomioSimplificado)
        elif op == '5':
            novoPolinomio = derivarPolinomio(polinomio)
            verPolinomio(novoPolinomio)
        else:
            print("Este número não está nas alternativas, tente novamente :D.\n")
        op = str(input("Insira um dos comandos do menu: "))
    if op == '0':
        sair()
opcao()