# ExercicioImplementacao2
Utilizando os algoritmos DFS ou BFS, faça:
  Exercício 1;
  Exercício 2 ou Exercício 3.  
  Cada exercício deve ser enviado em um único arquivo, separado. Ao submeter, o grupo deve compactar ambos os dois arquivos e     enviá-los em uma pasta .zip ou tar.gz.Os programas podem ser implementados em C++ ou Python.   
  Observação 1: clareza do código e eficiência do algoritmo serão fatores avaliativos.  
  Observação 2: a entrada dos dados deve ser feita através de arquivo .txt, no padrão como mostra cada exemplo.  
  Observação 3: apenas um membro do grupo deve submeter o trabalho. O nome do arquivo será: EP2_MatriculaAluno1_MatriculaAluno2_MatriculaAluno3.zip (caso o grupo seja formado por 3 pessoas).
  
  
  
 <h1> Problema 1</h1></br>
Considere um grafo não direcionado simples e conexo, G = (V,E).</br>
Foi dada a você a seguinte tarefa: pintar os vértices do grafo de</br>
preto e de branco tal que se (u,v) pertence a E, então u e v devem</br>
ter cores distintas. Desenvolva um ​ algoritmo eficiente que</br>
determine se é possível ou não pintar G com apenas duas cores.</br>
Exemplo de entrada</br>
numeroVertices</br>
numeroArestas</br>
verticeX verticeY</br>
...</br>
<h2>Exemplo 1</h2></br>
9</br>
8</br>
0 1</br>
0 2</br>
0 3</br>
0 4</br>
0 5</br>
0 6</br>
0 7</br>
0 8</br>
<h2>Exemplo 2</h2></br>
3</br>
3</br>
0 11 2</br>
2 0</br>
<h2>Exemplo 3</h2></br>
3</br>
2</br>
0 1</br>
1 2</br>
Saída do Exemplo 1</br>
SIM</br>
Saída do Exemplo 2</br>
NAO</br>
Saída do Exemplo 3</br>
SIM</br>

<h1>Problema 2</h1></br>
De acordo com o Departamento de Engenharia de Tráfego de</br>
uma cidade do sul de Minas, a maioria dos acidentes de trânsito</br>
ocorrem em ruas de mão dupla. Para reduzir o número de</br>
fatalidades no trânsito, um prefeito quer transformar, na medida do</br>
possível, as ruas dessa cidade em ruas de mão única. Você foi</br>
contratado para auxiliar nesse processo decisório, de forma que a</br>
partir de cada intersecção (esquina), é possível para um motorista</br>
dirigir para todas as outras intersecções (esquinas) seguindo</br>
alguma rota.</br>
Como informação, você possui um lista de ruas (todas de mão</br>
dupla) da cidade. Cada rua se conecta a duas intersecções, e não</br>
prolonga pela intersecção. No máximo quatro ruas podem se</br>
encontrar em uma intersecção, e existe no máximo uma rua</br>
conectando qualquer par de intersecções. Vamos assumir que é</br>
possível para um motorista se deslocar de qualquer ponto para</br>
qualquer outro ponto quando as ruas são de mão dupla.</br>
Seu objetivo: indicar quais ruas podem ser remodeladas como</br>
ruas de mão única.</br>
Entrada do problema</br>
numeroIntersecções numeroRuas</br>
interseccaoX1 interseccaoY1 (Rua 1)</br>
interseccaoX2 interseccaoY2 (Rua 2)</br>
...</br>
<h2>Exemplo 1</h2></br>
7 10</br>
1 2</br>
1 3</br>
2 4</br>
3 4</br>
4 5</br>
4 6</br>
5 7</br>
6 7</br>
2 5</br>
3 6</br>
<h2>Exemplo 2</h2></br>
7 9</br>
1 2</br>
1 3</br>
1 4</br>
2 4</br>
3 4</br>
4 5</br>
5 6</br>
5 7</br>
7 6</br>
Saída do Exemplo 1</br>
1 2</br>
2 4</br>
3 1</br>
3 6</br>
4 3</br>
5 2</br>
5 4</br>
6 4</br>
6 7</br>
7 5</br>
Saída do Exemplo 2</br>
1 2</br>
2 4</br>
3 1</br>
4 1</br>
4 3</br>
4 5</br>
5 4</br>
5 6</br>
6 7</br>
7 5</br>
<strong>Importante:</strong> no caso em que não é possível transformar a rua “x y”</br>
em mão única, apresentamos essa informação imprimindo “x y” e</br>
“y x” em linhas diferentes. Veja a Saída do Exemplo 2, referente</br>
ao par “4 5” e “5 4”.</br>

