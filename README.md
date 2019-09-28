# ExercicioImplementacao2
Utilizando os algoritmos DFS ou BFS, faça:
  Exercício 1;
  Exercício 2 ou Exercício 3.  
  Cada exercício deve ser enviado em um único arquivo, separado. Ao submeter, o grupo deve compactar ambos os dois arquivos e     enviá-los em uma pasta .zip ou tar.gz.Os programas podem ser implementados em C++ ou Python.   
  Observação 1: clareza do código e eficiência do algoritmo serão fatores avaliativos.  
  Observação 2: a entrada dos dados deve ser feita através de arquivo .txt, no padrão como mostra cada exemplo.  
  Observação 3: apenas um membro do grupo deve submeter o trabalho. O nome do arquivo será: EP2_MatriculaAluno1_MatriculaAluno2_MatriculaAluno3.zip (caso o grupo seja formado por 3 pessoas).
  
  
  
  Problema 1
Considere um grafo não direcionado simples e conexo, G = (V,E).
Foi dada a você a seguinte tarefa: pintar os vértices do grafo de
preto e de branco tal que se (u,v) pertence a E, então u e v devem
ter cores distintas. Desenvolva um ​ algoritmo eficiente que
determine se é possível ou não pintar G com apenas duas cores.
Exemplo de entrada
numeroVertices
numeroArestas
verticeX verticeY
...
Exemplo 1
9
8
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
Exemplo 2
3
3
0 11 2
2 0
Exemplo 3
3
2
0 1
1 2
Saíddo Exemplo 1
SIM
Saída do Exemplo 2
NAO
Saída do Exemplo 3
SIM

Problema 2
De acordo com o Departamento de Engenharia de Tráfego de
uma cidade do sul de Minas, a maioria dos acidentes de trânsito
ocorrem em ruas de mão dupla. Para reduzir o número de
fatalidades no trânsito, um prefeito quer transformar, na medida do
possível, as ruas dessa cidade em ruas de mão única. Você foi
contratado para auxiliar nesse processo decisório, de forma que a
partir de cada intersecção (esquina), é possível para um motorista
dirigir para todas as outras intersecções (esquinas) seguindo
alguma rota.
Como informação, você possui um lista de ruas (todas de mão
dupla) da cidade. Cada rua se conecta a duas intersecções, e não
prolonga pela intersecção. No máximo quatro ruas podem se
encontrar em uma intersecção, e existe no máximo uma rua
conectando qualquer par de intersecções. Vamos assumir que é
possível para um motorista se deslocar de qualquer ponto para
qualquer outro ponto quando as ruas são de mão dupla.
Seu objetivo: indicar quais ruas podem ser remodeladas como
ruas de mão única.
Entrada do problema
numeroIntersecções numeroRuas
interseccaoX1 interseccaoY1 (Rua 1)
interseccaoX2 interseccaoY2 (Rua 2)
...
Exemplo 1
7 10
1 2
1 3
2 4
3 4
4 5
4 6
5 7
6 7
2 5
3 6
Exemplo 2
7 9
1 2
1 3
1 4
2 4
3 4
4 5
5 6
5 7
7 6
Saída do Exemplo 1
1 2
2 4
3 1
3 6
4 3
5 2
5 4
6 4
6 7
7 5
Saída do Exemplo 2
1 2
2 4
3 1
4 1
4 3
4 5
5 4
5 6
6 7
7 5
Importante: no caso em que não é possível transformar a rua “x y”
em mão única, apresentamos essa informação imprimindo “x y” e
“y x” em linhas diferentes. Veja a Saída do Exemplo 2, referente
ao par “4 5” e “5 4”.

