class Grafo:
    """
    Classe Grafo, contem o numero maximo de Vertices e Arestas(ambos INT)
    Comtem também 2 listas, que vai conter todos os vertices e outra
    que vai conter todas as arestas
    """
    def __init__(self,numVertice = 0,numAresta = 0,vertices=list(),arestas=list(),direcionado = bool()):
        self.numVertice = int(numVertice)
        self.numAresta = int(numAresta)
        self.vertices = list(vertices)
        self.arestas = list(arestas)
        self.direcionado = bool(direcionado)

#0
def GGcriaGrafo(v,a):
    """
    Essa função cria um grafo com um numero 'v' de vertices
    e 'a' de atastas, e retorna esse grafo
    """
    grafo = Grafo(v,a)

    print(f'Grafo G[{grafo.numVertice},{grafo.numAresta}] criado com sucesso!\n')
    return grafo

#3
def GGdestroiGrafo(grafo):
    """
    Essa função esvazia todas as listas, faznedo com que novas arestas e novos vertices possam ser alocados.
    """
    grafo.vertices.clear()
    grafo.arestas.clear()
    
    print(f'Grafo excluido com sucesso, podem ser criado {grafo.numVertice} vertices e {grafo.numAresta} arestas')
    return grafo

#1
def GVcriaVertice(grafo):
    """
    Essa função adiciona um vertice na lista 'vertices' do objeto grafo.
    """
    if len(grafo.vertices) >= grafo.numVertice:
        print('Não é possivel acrescentar mais vertices!!!')
    else:
        print('Uma pequena instrução antes de proseguir, o nome do vertice é uma string, então mesmo queseja coloca um numero'
        ' ele sera tratado como uma string!!!\nDICA: PARA FACILITAR SUAS CONSULTAS, É RECOMENTAVEL COLOCAR SÓ UM CARACTER NUMERICO:  1, 2 ou 3.\n')

        vertice = str(input(f'Digite o {len(grafo.vertices)+1}º elemento a ser inserido: '))

        for i in grafo.vertices:
            if i == vertice:
                print('Vertice já existe!!!')
                return
        
        grafo.vertices.append(vertice)
        print('\nVertice adicionado com sucesso,confira a lista de vertices: ')
        print(f'{grafo.vertices}\n')

        return grafo

#2
def GVcriaAresta(grafo):
    """
    Essa função cria uma aresta com o auxilio de um dicionario com os itens de 'origem' e 'destino', depois adiciona os dados dessa aresta na
    lista arestas. Se a aresta for direcionada é adicionado só um item ta lista, porem se não for ele adiciona também a aresta de volta.
    Ex.: se tivermos uma aresta não direcionada A-->B, vai ser adicionado na lista [A,B] e [B,A]
    """
    if len(grafo.vertices) <= 0:
        print('É necessario adicionar pelo menos um vertice.')
    elif len(grafo.arestas) >= grafo.numAresta:
        print('Não é possivel acrescentar mais arestas!!!')
    else:
        aresta = dict()
        aux = 0

        origem = destino = ' '

        while True:
            aresta.clear()
            aux = 0
            menu = ' '

            origem = str(input('Diga o Vertice de origem: '))
            for i in grafo.vertices:
                if i == origem:
                    aux = 1
                    break
            if aux == 0:
                print('Valor não encontrado, digite novamente!!!')
                continue
            else:
                aresta['origem'] = origem
                print('Vertice de origem cadastrado com sucesso.')
                break
        

        while True:
            aux = 0

            destino = str(input('Diga o Vertice de destino: '))
            for i in grafo.vertices:
                if i == destino:
                    aux = 1
                    break
            if aux == 0:
                print('Valor não encontrado, digite novamente!!!')
                continue
            else:
                aresta['destino'] = destino
                print('Vertice de destinho cadastrado com sucesso.')
                break
        
        for i in grafo.arestas:
            if i == aresta:
                print('Aresta já existe!!!')
                return
            
        
        grafo.arestas.append(aresta.copy())

        print('Aresta criada com sucesso, confira as arestas existentes:')
        print(f'{grafo.arestas}\n')

        return grafo

#4
def GBexisteVertice(grafo, vertice):
    """
    Verifica se a a variavel 'vertice' existe na lista de vertices do objeto grafo
    """
    for i in grafo.vertices:
        if i == vertice:
            return True
    
    return False

#5
def GBexisteArestaDir(grafo,aresta):
    """
    Verifica se a Aresta direcionada existe, percorrendo a lista de arestas do objeto grafo.
    """
    for i in grafo.arestas:
        if i == aresta:
            return True
    
    return False

#6
def GBexisteAresta(grafo,aresta):
    '''
    Verifica se a Aresta existe, percorrendo a lista de arestas do objeto grafo.
    '''
    for i in grafo.arestas:
        if i == aresta:
            return True
    
    return False


#7
def GApegaArestaDir(grafo, aresta):
    """
    Seleciona a aresta pedida pelo usuario e a retorna, caso não seja encontrada retorna 0
    """
    for i in grafo.arestas:
        if i == aresta:
            return aresta
    
    return 0
    

#8
def GApegaAresta(grafo,aresta):
    """
    Seleciona a aresta pedida pelo ususario e a retorna caso existir, como essa aresta não é
    direcionada, ele vai retornar  a aresta de ida e de volta
    """
    for i in grafo.arestas:
        if i == aresta:
            return aresta
    
    return 0

#9
def GVprimeiroVertice(grafo):
    """
    Pega o priemeiro Vertice que foi criado, e o denomina como ponto de partida.
    """
    primeiroVertice = grafo.vertices[0]

    return primeiroVertice

#10
def GVproximoVertice(grafo,verticeAtual,arestasLidas):
    """
    Pega o proximo vertice de acordo com as arestas, a lista arestas lidas, o elemento
    aux e o dicionario ArestaContraria fazem uma verficação para que as arestas não fiquem
    indo e voltando para o mesmo lugar
    """
    arestaContraria = dict()
    aux = 0
    for i in grafo.arestas:
        for j in arestasLidas:
            if j == i:
                aux += 1

        if i['origem'] == verticeAtual and aux == 0:
            arestasLidas.append(i)
            arestaContraria['origem'] = i['destino']
            arestaContraria['destino'] = i['origem']
            arestasLidas.append(arestaContraria)
            verticeAtual = i['destino']
            break
        aux = 0
        arestaContraria.clear()
    
    return verticeAtual

#11
def GAprimeiraAresta(grafo):
    """
    Devolve a primeira aresta criada no grafo
    """
    primeiraAresta = grafo.arestas[0]

    return primeiraAresta

#12
def GAproximaAresta(grafo,arestaAtual):
    """
    Pega a segunda aresta criada, se chamar a função novamente devolve a 3ª
    e assim por diante
    """
    for i in range(len(grafo.arestas)):
        if grafo.arestas[i] == arestaAtual:
            if i == len(grafo.arestas)-1:
                arestaAtual = grafo.arestas[i]
            else:
                arestaAtual = grafo.arestas[i+1]
                break
            
    return arestaAtual

#13
def GInumeroVertices(grafo):
    """
    Devolve o nuemro de vertices já criados.
    """
    return len(grafo.vertices)

#14
def GInumeroVerticesMax(grafo):
    """
    Devolve o numero maximo de vertices que podem ser criados
    """
    return grafo.numVertice

#15
def GInumeroArestas(grafo):
    """
    Devolve o numero de arestas criadas.
    """
    return len(grafo.arestas)

#16
def GInumeroArestasMax(grafo):
    """
    Devolve o numero maximo de arestas
    """
    return grafo.numAresta

#0 'linha 18'
def GGcarregaGrafo(nomeDoArquivo):
    """
    Essa função tem o objetico de carregar os dados persentes em um determinado arquivo texto, como o nome guardado na variavel 'nomeDoArquivo'
    """
    dados = list()
    try:
        a = open(nomeDoArquivo,'rt')
    except:
        print('Erro na abertura do arquivo!')
        return 0
    else:
    # pega os dados do arquivo e guarda na lista dados
        for linha in a:
            dado = linha.split(' ')
            for i in dado:
                dados.append(int(i))

    #chama a função GGcriaGrafo e aloca o numero maximo de variaveis e de arestas
    grafo = GGcriaGrafo(dados[0],dados[1])
    aux = 0


    #cria os vertices ques estão
    for i in range(2,len(dados)):
        for j in grafo.vertices:
            if j == str(dados[i]):
                aux += 1
        if aux == 0:
            grafo.vertices.append(str(dados[i]))
        else:
            aux = 0

    print(f'O Grafo possui os vertices: {grafo.vertices}')


    #Confere se o grafo é direcionado
    resp = ' '
    while True:
        resp = str(input('O grafo é Direcionado:\n\tS - sim\tN - não\n')).upper()[0]
        if resp == 'S':
            grafo.direcionado  = True
            break
        elif resp == 'N':
            grafo.direcionado = False
            break
        else:
            print('Opção invalida!!!')

    aresta = dict()

    #cria as arestas do grafo direcionado
    for i in range(2,len(dados),2):
        aresta['origem'] = str(dados[i])
        aresta['destino'] = str(dados[i+1])

        grafo.arestas.append(aresta.copy())

    print(f'O grafo possui as seguintes Arestas:\n{grafo.arestas}')

    a.close()
    return grafo

#17.1
def arquivoExiste(nomeArquivo):
    try:
        a = open(nomeArquivo,'rt')
        a.close
    except FileNotFoundError:
        return True
    else:

        return False

#17
def GBsalvaGrafo(grafo,nomeArquivo):
    verificaArquivo = arquivoExiste(nomeArquivo)
    if verificaArquivo == False:
        print('Arquivo já existe!')
        return False
    else:
        a = open(nomeArquivo,'wt+')
        a.write(f'{grafo.numVertice} {grafo.numAresta}\n')
        for i in grafo.arestas:
            a.write(f'{i["origem"]} {i["destino"]}\n')
        a.close()
        return True

#18
def GIpegaGrau(grafo,vertice):
    grau = 0
    for i in grafo.arestas:
        if i['origem'] == vertice or i['destino'] == vertice:
            grau+=1
    return grau


#funçaõ auxiliar da Caminho
def posicaoVertice(grafo,vertice):
    for i in range(0,len(grafo.vertices)):
        if vertice == grafo.vertices[i]:
            return i

#linha 272
def GFdefinePesos(grafo,resposta):
    """
    Essa função tem o objetivo de definir o peso de cada aresta presente no grafo
    """
    pesos = list()

    if resposta:
        for i in grafo.arestas:
            pesos.append(float(input(f'Digite o peso da aresta {i}: ')))
    else:
        for i in grafo.arestas:
            pesos.append(0)

    return pesos

#auxilia a função caminho
def retornaVizinhos(escolhido,grafo):
    """
    Retorna todos os vertices que a aresta faz ligação
    """
    vizinhos = list()
    for i in grafo.arestas:
        if i['origem'] == escolhido:
            vizinhos.append(i['destino'])
    return vizinhos

#auxilia a função caminho
def posicaoAresta(grafo,aresta):
    """
    Pega a posição da aresta na lista de arestas do grafo
    """
    for i in range(0,len(grafo.arestas)):
        if grafo.arestas[i] == aresta:
            return i
            
#auxilia a função caminho
def proxEscolhido(grafo,interacao,mat,elementosLidos,posVerticeEscolhido):
    """
    Escolhe o proximo vertice a ser lido na matriz
    """
    menor = 1000
    end = 0
    
    for i  in range(0,len(grafo.vertices)):
        if type(mat[interacao][i]) != int:
            if grafo.vertices[i] not in elementosLidos:
                if mat[interacao][i]['p'] < menor and i != posVerticeEscolhido:
                    menor = mat[interacao][i]['p']
                    end = i
    
    return end

#auxilia a função caminho
def valoresImutaveis(grafo,mat,valor,escolhido,interacao):
    """
    coloca o valor da coluna toda com o valor imutavel do elemento escolhido
    """
    for i in range(interacao,len(grafo.vertices)):
        mat[i][posicaoVertice(grafo,escolhido)] = valor
    
    return mat

#auxilia a função caminho
def duplicaValor(grafo,mat,valor,elemento,interacao):
    """
    duplica o valor da linha de cima em determinda coluno
    """
    mat[interacao][posicaoVertice(grafo,elemento)] = valor

    return mat

#auxilia a função caminho
def Gcaminho(grafo,pesos,partida,chegada):
    """
    Enconra o menor caminho de um vertice A até um vertice B
    """
    elemento = dict()
    elementoslidos = list()
    lista = list()
    mat = list()
    aresta = dict()
    interacao = 0
    copiar = True
    caminho = list()

    for i in range(0,len(grafo.vertices)):
        lista.append(-1)
    
    for i in range(0,len(grafo.vertices)):
        mat.append(lista[:])
    

    for i in range(0,len(grafo.vertices)): # coloca caminho 0 para o vertice ir ate ele mesmo
        if grafo.vertices[i] == partida:
            for j in range(0,len(grafo.vertices)):
                elemento['p'] = 0
                elemento['v'] = partida
                mat[j][posicaoVertice(grafo,partida)] = elemento.copy()
                
                elemento.clear()

    escolhido = partida
    while interacao < len(grafo.vertices):
        elementoslidos.append(escolhido)
        print(elementoslidos)       

        vizinhos = retornaVizinhos(escolhido,grafo)
        if interacao != 0:
            valoresImutaveis(grafo,mat,mat[interacao-1][posicaoVertice(grafo,escolhido)],escolhido,interacao)
        for i in range(0,len(grafo.vertices)):
            if grafo.vertices[i] in vizinhos:
                if interacao == 0:
                    aresta['origem'] = escolhido
                    aresta['destino'] = grafo.vertices[i]
                    elemento['p'] = pesos[posicaoAresta(grafo,aresta)]
                    elemento['v'] = escolhido
                    mat[interacao][posicaoVertice(grafo,grafo.vertices[i])] = elemento.copy()
                    elemento.clear()
                    aresta.clear()
                else:
                    aresta['origem'] = escolhido
                    aresta['destino'] = grafo.vertices[i]
                    if type(mat[interacao-1][i]) != int:
                        if mat[interacao-1][i]['p'] < pesos[posicaoAresta(grafo,aresta)] + mat[interacao-1][posicaoVertice(grafo,escolhido)]['p']:
                            duplicaValor(grafo,mat,mat[interacao-1][posicaoVertice(grafo,grafo.vertices[i])],grafo.vertices[i],interacao)
                            copiar = False
                        else:
                            elemento['p'] = pesos[posicaoAresta(grafo,aresta)] + mat[interacao-1][posicaoVertice(grafo,escolhido)]['p']
                            elemento['v'] = escolhido
                    else:
                        elemento['p'] = pesos[posicaoAresta(grafo,aresta)] + mat[interacao-1][posicaoVertice(grafo,escolhido)]['p']
                        elemento['v'] = escolhido
                    
                    if copiar == True:
                        mat[interacao][posicaoVertice(grafo,grafo.vertices[i])] = elemento.copy()
                    copiar = True
                    elemento.clear()
                    aresta.clear()


        escolhido = grafo.vertices[proxEscolhido(grafo,interacao,mat,elementoslidos,posicaoVertice(grafo,escolhido))]
        interacao+=1

    print('FINAL')
    for i in range(0,len(grafo.vertices)):
        for j in range(0,len(grafo.vertices)):
            print(f'{mat[i][j]} ',end='')
        print('')
    print('---'*20)
    cont = 0
    while chegada != partida:
        caminho.append(chegada)
        chegada = mat[len(grafo.vertices)-1][posicaoVertice(grafo,chegada)]['v']
        cont+=1
        if cont == len(grafo.vertices):
            break

    caminho.append(partida)
    
    if cont != len (grafo.vertices):
        for i in range(len(caminho)-1,-1,-1):
            if i != 0:
                print(f' {caminho[i]} ->',end='')
            else:
                print(f' {caminho[i]}')
    else:
        print('Caminho não existe')