# Grafo  e Algoritmo de Dijkstra

<h2>Explicando funções</h2>

  <h4>1 - Criar Vertice</h4>Essa função adiciona um vertice na lista 'vertices' do objeto grafo.
  
  <h4>2 - Criar Aresta</h4>Essa função cria uma aresta com o auxilio de um dicionario com os itens de 'origem' e 'destino', depois adiciona os dados dessa aresta na
  lista arestas. Se a aresta for direcionada é adicionado só um item ta lista, porem se não for ele adiciona também a aresta de volta.
  Ex.: se tivermos uma aresta não direcionada A-->B, vai ser adicionado na lista [A,B] e [B,A]
    
  <h4>3 - Destroi Grafo :(</h4>Essa função esvazia todas as listas, faznedo com que novas arestas e novos vertices possam ser alocados.
  
  <h4>4 - Existe Vertice</h4>Verifica se a a variavel 'vertice' existe na lista de vertices do objeto grafo.
  
  <h4>5 e 6 - Existe Aresta</h4>Verifica se existe a aresta.
  
  <h4>7 e 8 -Pega Aresta</h4>Seleciona a aresta pedida pelo usuario e a retorna, caso não seja encontrada retorna 0
  
  <h4>9 - Pegar 1º Vertice</h4>Pega o priemeiro Vertice que foi criado, e o denomina como ponto de partida.
  
  <h4>10 - Proximo Vertice</h4>Pega o proximo vertice de acordo com as arestas, a lista arestas lidas, o elemento
    aux e o dicionario ArestaContraria fazem uma verficação para que as arestas não fiquem
    indo e voltando para o mesmo lugar
    
 <h4>11 - Pegar 1ª Aresta</h4>Devolve a primeira aresta criada no grafo
 
 <h4>12 - Proxima Aresta</h4>Pega a segunda aresta criada, se chamar a função novamente devolve a 3ª
    e assim por diante
 
  <h4>13 - Numero de Vertices</h4>Devolve o nuemro de vertices já criados.
  
  <h4>14 - Numero Maximo de Vertices</h4>Devolve o numero maximo de vertices que podem ser criados.
  
  <h4>15 - Numero de Arestas</h4>Devolve o numero de arestas criadas.
  
  <h4>16 - Numero Maximo de Arestas</h4>Devolve o numero maximo de arestas.
  
  <h4>17 - Salvar Grafo</h4>Salva o grafo em um arquivo.
  
  <h4>18 - Grau do Vertice</h4>Recebe um vertice como entrada e retorna um numero inteiro referente ao seu grau.
  
  <h4>19 - Caminho</h4>Essa função faz a tabela de Dijkstra, e com isso ela pega o ponto de partida e encontra o caminho mais curto para todos os outros vertices.
  
 
