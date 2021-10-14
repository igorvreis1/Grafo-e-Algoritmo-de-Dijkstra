import funcoes
menu = 100
verticeAtual = ' '
arestaAtual = ' '
aresta = dict()
direcionado = bool()
arestasLidas = list()
grafoArquivo = bool()


print('Trabalho para criação/manipulação de grafos utilizando python\n')

while True:
    resp = str(input('Você deseja carregar um grafo já existente em um arquivo:\n\tS - sim\tN - não\n')).upper()[0]
    if resp == 'S':
        nomeArquivo = input('digite o nome do aquivo, não esqueça do ".txt" no final: ')
        grafo = funcoes.GGcarregaGrafo(nomeArquivo)
        if grafo == 0:
            continue
        else:
            grafoArquivo = True
            break
    elif resp == 'N':
        grafoArquivo = False
        break
    else:
        print('Opção invalida!!!')


if grafoArquivo == False:
    while True:
        resp = str(input('O grafo é Direcionado:\n\tS - sim\tN - não\n')).upper()[0]
        if resp == 'S':
            direcionado  = True
            break
        elif resp == 'N':
            direcionado = False
            break
        else:
            print('Opção invalida!!!')

    print('Primeiramente vamos estabelecer o numero de vertices e de arestas que vão compor o grafo.')
    vert = ares = -1

    while vert <= 0:
        vert = int(input('Digite o nuemro de Vertices: '))
        if vert <= 0:
            print('Valor invalido, DIGITE NOVAMENTE')

    while ares <= 0:
        ares = int(input('Digite o nuemro de Arestas: '))
        if ares <= 0:
            print('Valor invalido, DIGITE NOVAMENTE')

    grafo = funcoes.GGcriaGrafo(vert,ares)
    grafo.direcionado = direcionado

while menu != 0:
    menu = 1000
    menu = int(input('Digite a opção desejada:\n'
        '\t1 - Criar Vertice\n'
        '\t2 - Criar Aresta\n'
        '\t3 - Destroi Grafo :(\n'
        '\t4 - Existe Vertice\n'
        '\t5 - Existe Aresta Direcionada\n'
        '\t6 - Existe Aresta\n'
        '\t7 - Pega Aresta Direcionada\n'
        '\t8 - Pega Aresta\n'
        '\t9 - Pegar 1º Vertice\n'
        '\t10 - Proximo Vertice\n'
        '\t11 - Pegar 1ª Aresta\n'
        '\t12 - Proxima Aresta\n'
        '\t13 - Numero de Vertices\n'
        '\t14 - Numero Maximo de Vertices\n'
        '\t15 - Numero de Arestas\n'
        '\t16 - Numero Maximo de Arestas\n'
        '\t17 - Salvar Grafo\n'
        '\t18 - Grau do Vertice\n'
        '\t19 - Caminho\n'
        '\t0 - SAIR\n'))

    if menu == 1:
        if grafoArquivo == False or grafo.numVertice <= len(grafo.vertices):
            funcoes.GVcriaVertice(grafo)
        else:
            print('Essa função não está disponivel.')
            continue

    elif menu == 2:
        if grafoArquivo == False or grafo.numAresta <= len(grafo.arestas):
            funcoes.GVcriaAresta(grafo)
        else:
            print('Essa função não esta disponivel.')
            continue

    elif menu == 3:
        if grafoArquivo == False:
            funcoes.GGdestroiGrafo(grafo)
        else:
            print('Essa função não esta disponivel.')
            continue
        

    elif menu == 4:
        verificaVertice = str(input('Digite o vertice para conferir a existencia: '))
        verificacaoVert = funcoes.GBexisteVertice(grafo,verificaVertice)
        if verificacaoVert == True:
            print('O vertice existe.\n')
        else:
            print('Esse vertice não existe!\n')
            continue

    elif menu == 5:
        if grafo.direcionado == True:
            aresta['origem'] = str(input('Digite o vertice de Origem da Aresta: '))
            aresta['destino'] = str(input('Digite o vertice de Destino da Aresta: '))

            veriArestaDir = funcoes.GBexisteArestaDir(grafo,aresta)
            if veriArestaDir == True:
                print('A aresta existe.\n')
            else:
                print('A aresta não existe.\n')
            aresta.clear()
        else:
            print('O grafo não é direcionado!!! Logo essa função não é permitida')
            continue

    elif menu == 6:
        if grafo.direcionado == False:
            aresta['origem'] = str(input('Digite o vertice de Origem da Aresta: '))
            aresta['destino'] = str(input('Digite o vertice de Destino da Aresta: '))

            veriAresta = funcoes.GBexisteAresta(grafo,aresta)
            if veriAresta == True:
                print('A aresta existe.\n')
            else:
                print('A aresta não existe.\n')
            aresta.clear()
        else:
            print('O grafo é direcionado!!! Logo essa função não é permitida')
            continue

    elif menu == 7:
        if grafo.direcionado == True:
            aresta['origem'] = str(input('Digite o vertice de Origem da Aresta que deseja pegar: '))
            aresta['destino'] = str(input('Digite o vertice de Destino da Aresta que deseja pegar: '))

            pegaArestaDir = funcoes.GApegaArestaDir(grafo,aresta)
            
            aresta.clear()
            if pegaArestaDir == 0:
                print('Aresta não existe!!!\n')
            else:
                print(f'A aresta {pegaArestaDir} foi pega com sucesso!\n')

        else:
            print('O grafo não é direcionado!!! Logo essa função não é permitida\n')

    elif menu == 8:
        if grafo.direcionado == False:
            aresta['origem'] = str(input('Digite o vertice de Origem da Aresta que deseja pegar: '))
            aresta['destino'] = str(input('Digite o vertice de Destino da Aresta que deseja pegar: '))

            pegaAresta = funcoes.GApegaAresta(grafo,aresta)

            aresta.clear()
            if pegaAresta == 0:
                print('Aresta não existe!!!\n')
            else:
                print(f'A aresta {pegaAresta} foi pega com sucesso!\n')
        else:
            print('O grafo não é direcionado!!! Logo essa função não é permitida\n')

    elif menu == 9:
        if len(grafo.vertices) == 0:
           print('É necessatio criar um vertice antes!!!')
           continue
        else: 
            verticeAtual = funcoes.GVprimeiroVertice(grafo)

            print(f'Priemiro vertice pego com sucesso!!!\nO priemeiro vertice é "{verticeAtual}"\n')
    
    elif menu == 10:
        if len(grafo.vertices) == 0 or verticeAtual == ' ':
            print('ERRO!!! É necessario criar um vertice ou chamar a função "Pegar 1º Vertice"')
            continue
        else:
            verticeAtual = funcoes.GVproximoVertice(grafo,verticeAtual,arestasLidas)

            print(f'O proximo vertice é "{verticeAtual}"!!\n')

    elif menu == 11:
        if len(grafo.arestas) == 0:
           print('É necessatio criar uma aresta antes!!!')
           continue
        else:
            arestaAtual = funcoes.GAprimeiraAresta(grafo)
            print(f'A primeira aresta é {arestaAtual}!!')

    elif menu == 12:
        if len(grafo.arestas) == 0 or arestaAtual == ' ':
              print('ERRO!!! É necessario criar uma Aresta ou chamar a função "Pegar 1ª Aresta"') 
              continue
        else:
            arestaAtual = funcoes.GAproximaAresta(grafo,arestaAtual)
            print(f'O proxima aresta é "{arestaAtual}"!!\n')
    
    elif menu == 13:
        numVertices = funcoes.GInumeroVertices(grafo)
        print(f'O grafo possui {numVertices} vertices')
    
    elif menu == 14:
        numVerticesMax = funcoes.GInumeroVerticesMax(grafo)
        print(f'O grafo possui uma capacidade de {numVerticesMax} vertices')
    
    elif menu == 15:
        numArestasDir = funcoes.GInumeroArestas(grafo)
        print(f'O numero de Arestas criada é {numArestasDir}')

    elif menu == 16:
        numArestasMax = funcoes.GInumeroArestasMax(grafo)
        print(f'O numero maximo de arestas é {numArestasMax:.0f}')

    elif menu == 17:
        if grafoArquivo == False:
            nomeArquivo = str(input('Digite o nome do arquivo que sera gerado (não esqueça do ".txt" no final): '))

            deuCertoArquivo = funcoes.GBsalvaGrafo(grafo,nomeArquivo)

            if deuCertoArquivo == True:
                print('Arquivo criado com sucesso')
            else:
                print('Ocorreu algum erro na criação do Arquivo!')
        else:
            print('Essa função não esta disponivel!!!')
            continue
    
    elif menu == 18:
        verificaVertice = str(input('Digite o vertice que você quer saber o grau: '))
        verificacaoVert = funcoes.GBexisteVertice(grafo,verificaVertice)
        if verificacaoVert == True:
            grauVertice = funcoes.GIpegaGrau(grafo,verificaVertice)
            print(f'O grau do vertice {verificaVertice} é {grauVertice}!!!')
        else:
            print('Vertice não existe!')
            continue

    
    elif menu == 19:
        partida = str(input('Digite o ver de partida: '))
        chegada = str(input('Digite o vertice de chegada: '))
        pesos = list()
        
        if funcoes.GBexisteVertice(grafo,partida) and funcoes.GBexisteVertice(grafo,chegada):   
            while True:
                resp = str(input('Você deseja colocar pesos nas arestas?(se a resposta for não elas terão todas o mesmo peso)\n\tS - sim\tN - não\n')).upper()[0]
                if resp == 'S':
                    pesos = funcoes.GFdefinePesos(grafo,True)
                    break
                elif resp == 'N':
                    pesos = funcoes.GFdefinePesos(grafo,False)
                    break
                else:
                    print('Opção invalida!!!')

            funcoes.Gcaminho(grafo,pesos,partida,chegada)
        else:
            print('Erro vertices não encontrados!!!')

    elif menu == 0:
        print('Programa encerrado!!!')
    else:
        print('Erro valor não encontrado!!!')
        continue