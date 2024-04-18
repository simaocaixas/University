% Simao Caixas ist1109632
:- use_module(library(clpfd)). % para poder usar transpose/2
:- set_prolog_flag(answer_write_options,[max_depth(0)]). % ver listas completas
:- ['puzzlesAcampar.pl']. % Ficheiro dado. No Mooshak tera mais puzzles.

% Segue se o codigo

vizinhanca((L, C), Vizinhanca) :-
    /*      
    Funcao que eh verdade apenas se a vizinhanca eh uma lista ordenada de cima para baixo,
    da esquerda para a direita, sem elementos repetidos das posicoes imediatamente acima, ah
    esquerda, direita e abaixo da coorenada inserida. (Todas as coordenadas dos tabuleiros utilizados
    utilizam este formato (Linha, Coluna)).
    
    */

    L1 is L - 1,    % L1 e L2 correspondem a fila a cima e a baixo, respetivamente.
    L2 is L + 1,    
    C1 is C - 1,    % C1 e C2 correspondem a coluna a esqueda e a direita, respetivamente.
    C2 is C + 1,

Vizinhanca = [(L1, C), (L, C1), (L, C2), (L2, C)].

vizinhancaAlargada((L, C), VizinhancaAlargada) :-
    /*     
    Funcao que eh verdade somente se VizinhancaAlargada eh uma lista de oito cordenadas
    correspondentes as posicoes da sua vizinhaca (funcao imediatamente acima) e as posicoes
    nas diagonais da cordenada inserida (L,C).
            
    */

    L1 is L - 1,    % L1 e L2 correspondem a fila a cima e abaixo, respetivamente.
    L2 is L + 1,    
    C1 is C - 1,    % C1 e C2 correspondem a coluna a esqueda e a direita, respetivamente.
    C2 is C + 1,

VizinhancaAlargada = [(L1, C1),(L1,C),(L1,C2),(L,C1),(L,C2), (L2,C1),(L2,C),(L2,C2)].
    
todasCelulas(Tabuleiro, TodasCelulas) :- 
    /*     
    Funcao que eh verdade somente se TodasCelulas for uma lista ordenada de cima para baixo, da 
    esquerda para a direita sem elementos repetidos com todas as cordenadas do tabuleiro inserido.
    (O tabuleiro inserido eh sempre uma matriz quadrada, ou seja, o numero de linhas eh igual ao numero de colunas).
    */

    coordenadas_para_lista(Tabuleiro, 1, 1, TodasCelulas).     

coordenadas_para_lista([], _, _, []).                                          %Caso base da minha recursiva.
coordenadas_para_lista([Linha | Resto], Abcissa, Ordenada, RestodaLinha) :- 
          NovaAbcissa is Abcissa + 1,                            
          linha_para_coordenadas(Linha, Abcissa, Ordenada, Posicoesdalinha),   %A funcao linha_para_coordenadas eh verdade somente se PosicoesdaLinha eh uma lista de coordenadas da linha do nosso tabuleiro, tal como pedido.
          coordenadas_para_lista(Resto, NovaAbcissa, Ordenada, RestoPosi),     %A recursao faz o processo para todas as linhas.
          append(Posicoesdalinha, RestoPosi, RestodaLinha).                    %O append vai juntando as linhas com as posicoes correspondentes de modo a formar uma lista com todas as coordenadas.

linha_para_coordenadas([], _, _, []).                                          %Caso base da recursiva, esta recursiva transforma uma linha numa lista de coordenadas, tal como pedido.
linha_para_coordenadas([_ | Restodasposi], Abcissa, Ordenada, [(Abcissa, Ordenada) | RestoPosi]) :-
    NovaOrdenada is Ordenada + 1,                                    
    linha_para_coordenadas(Restodasposi, Abcissa, NovaOrdenada, RestoPosi).

todasCelulas(Tabuleiro, TodasCelulas, Objeto) :- 
    /*     
    Funcao que eh verdade somente se TodasCelulas for uma lista ordenada de cima para baixo, da 
    esquerda para a direita sem elementos repetidos com todas as cordenadas do tabuleiro inserido em que existem o Objeto.
    Ou seja se o Objeto for 'r' (correspondente a Relva), TodasCelulas sao todas as coordenadas que correspondem a relvas no tabuleiro.
    */

    coordenadas_para_lista(Tabuleiro, 1, 1, TodasCelulas, Objeto).                            %Ah semelhanca da funcao acima vamos iterar o tabuleiro linha por linha, a comecar na posicao (1,1).  

coordenadas_para_lista([], _, _, [], _).                                            
coordenadas_para_lista([Linha | Resto], Abcissa, Ordenada, RestodaLinha, Objeto) :-           %Clausula semenhante da funcao acima porem neste caso a nossa funcao linha_para_coordenadas considera somente os objetos iguais ao nosso Objeto.
    NovaAbcissa is Abcissa + 1,                            
    linha_para_coordenadas(Linha, Abcissa, Ordenada, Posicoesdalinha, Objeto),
    coordenadas_para_lista(Resto, NovaAbcissa, Ordenada, RestoPosi, Objeto),
    append(Posicoesdalinha, RestoPosi, RestodaLinha).      

linha_para_coordenadas([], _, _, [], _):- !.                                                  %Caso base da recursiva que vai analisar cada linha posicao a posicao e ver qual corresponde a um objeto.
linha_para_coordenadas([Posicao | Restodasposi], Abcissa, Ordenada, [(Abcissa, Ordenada) | RestoPosi], Objeto) :-
    verifica_objeto(Posicao, Objeto),
    NovaOrdenada is Ordenada + 1,
    !,
    linha_para_coordenadas(Restodasposi, Abcissa, NovaOrdenada, RestoPosi, Objeto).

linha_para_coordenadas([Posicao | Restodasposi], Abcissa, Ordenada, RestoPosi, Objeto) :-
    not(verifica_objeto(Posicao, Objeto)),
    NovaOrdenada is Ordenada + 1,
    linha_para_coordenadas(Restodasposi, Abcissa, NovaOrdenada, RestoPosi, Objeto).

verifica_objeto(Posicao, Objeto) :-                                                            %verifica_objeto eh uma funcao simples que utiliza um 'if-then-else' e eh verifica se Objeto eh uma variavel, se for entao Posicao tambem sera;
    (var(Objeto) -> var(Posicao) ; Posicao == Objeto).                                         %Se nao entao Posicao sera unificado com o Objeto.

calculaObjectosTabuleiro(Tabuleiro, CLinhas, CColunas, Objeto) :- 
    /*     
    Funcao que eh verdade se o Tabuleiro e o Objeto forem de facto tabuleiros e objetos e CLinhas e CColunas sao o numero de Objetos em cada linha e coluna,
    respetivamente. Ou seja a funcao eh util para contar o numero de objetos, introduzido na variavel Objeto, em cada linha e coluna.
    */
 
    calculalinhas(Tabuleiro, CLinhas, Objeto),                                                  %calculalinhas eh a funcao auxiliar recursiva que itera o tabuleiro e Clinhas sera a lista de objetos correspondente a Objeto em cada linha. 
    transpose(Tabuleiro, TabuleiroTransposto),                                                  %Visto que eh mais facil trabalhar com as linhas do nosso tabuleiro, a funcao auxiliar transpose eh util ao longo do projeto pois transpoe o nosso tabuleiro.
    calculalinhas(TabuleiroTransposto, CColunas, Objeto).                                

calculalinhas([],[],_).                                                                         %Caso base da recursao.
calculalinhas([Linha | RestodasLinhas], [N | Resto], Objeto) :-
    verposicoes(Linha, Objeto, N),                                                              %verposicoes eh uma funcao auxiliar recursiva que verifica o numero de Objetos na linha e N sera entao esse valor, esse valor eh colocado em Clinhas.
    calculalinhas(RestodasLinhas, Resto, Objeto).                                         

verposicoes([], _, 0).                                                                          %Caso base da recursao, verposicoes esta dividida em tres clausulas importantes.
verposicoes([Posicao | Resto], Objeto, N) :-                                                    %Primeira clausula, Objeto eh uma variavel e a Posicao nao eh uma variavel
    var(Objeto),
    not(var(Posicao)),!,                    
    (Posicao == Objeto -> N1 is 1; N1 is 0),                                                    %Como Objeto eh uma variavel e Posicao nao eh uma variavel entao utilizei == para verificar se sao equivalentes, se forem entao N1 tomarah o valor de 1 e dessa forma N2 tomara o valor que ja estava na recursao + 1.
    verposicoes(Resto, Objeto, N2),                                                             %Se por acaso nao forem equivalentes entao o N1 passa a ser 0 e nada serah somado na nossa recursao.
    N is N1 + N2.

verposicoes([Posicao | Resto], Objeto, N) :-                                                    %Tanto esta clausula como a imediatamente abaixo basea-se no mesmo principio mas nesta como tanto o Objeto como a Posicao sao variaveis entao utilizei = para verificar a equivalencia
    var(Objeto),
    var(Posicao),!,
    (Posicao = Objeto -> N1 is 1; N1 is 0),
    verposicoes(Resto, Objeto, N2),
    N is N1 + N2.

verposicoes([Posicao | Resto], Objeto, N) :-                                                    %Neste caso Objeto eh uma constante.
    (Posicao == Objeto -> N1 is 1; N1 is 0),
    verposicoes(Resto, Objeto, N2),
    N is N1 + N2.

celulaVazia(Tabuleiro, (L, C)) :-
    /*     
    Funcao que eh verdade se o Tabuleiro for de facto um tabuleiro e que nao tem nada, ou seja nao possui nenhum objeto exeto relva na posicao (L,C).
    Se por ventura (L,C) corresponder a uma posicao fora do tabuleiro a funcao nao deve de falhar.
    */

    length(Tabuleiro, NumLinhas),
    length(Tabuleiro, NumColunas),
    L =< NumLinhas,
    C =< NumColunas,
    nth1(L, Tabuleiro, Linha),                                                                 %nth1 eh uma funcao auxiliar que se adequa a muitas das funcoes deste projeto, de modo a conseguir ir ao indice L dentro da lista Tabuleiro e achar o elemento Linha.
    nth1(C, Linha, Elem),                                                                      %Jah neste nth1 consigo ir ao indice C dentro da lista Linha e achar o elemento Elem.
    Elem \== 'a',                                                                        
    Elem \== 't'.

celulaVazia(Tabuleiro, (L, C)) :-                                                              %Clausula simples que lida com as coordenadas que nao pertencem ao tabuleiro.   
    length(Tabuleiro, NumLinhas),
    length(Tabuleiro, NumColunas),
    (L > NumLinhas ; C > NumColunas).                                                          % ' ; ' Funciona como um 'Ou'. Logo eh True caso o L OU C forem valores que nao pertencem ao tabuleiro. 

insereObjectoCelula(Tabuleiro, TendaOuRelva, (L, C)) :-
    /*      
    Funcao que eh verdade se Tabuleiro eh um tabuleiro e (L,C) sera a posicao em que iremos inserir o objeto TendaOuRelva.
    */

    insereNovoTab(Tabuleiro, TendaOuRelva, (L, C), NovoTabuleiro),                             %insereNovoTab eh uma funcao auxiliar que insere na posicao (L,C) o objeto TendaOuRelva criando um novo tabuleiro, NovoTabuleiro.              
    Tabuleiro = NovoTabuleiro.

insereNovoTab(Tabuleiro, TendaOuRelva, (L, C), NovoTabuleiro) :-                         
    nth1(L, Tabuleiro, Linha),                                                  
    nth1(C, Linha, Esta_a_Ocupar),
    var(Esta_a_Ocupar),                                                                        %Com o auxilio da funcao nth1 obtenho o objeto na posicao (L,C) e caso seja uma variavel, ou seja, um espaco livre ele vai colocar entao o objeto TendaOuRelva.
    modifica(Linha, C, TendaOuRelva, Linha_Modificada),                                        %Primeiro modifico a linha do tabuleiro e de seguida modifico o tabuleiro substituindo a lista velha com a nova ja com as devidas modificacoes.
    modifica(Tabuleiro, L, Linha_Modificada, NovoTabuleiro),!.

insereNovoTab(Tabuleiro, _, (L, C), NovoTabuleiro) :-                                          %Se a posicao inserida corresponder a um espaco ocupado a funcao nao faz absolutamente nada.
    nth1(L, Tabuleiro, Linha),
    nth1(C, Linha, _),
    NovoTabuleiro = Tabuleiro,!.

modifica(Lista, Index, Elemento, NovaLista) :-                                                 %O modifica utiliza outra utilidade da funcao auxiliar nth1 que eh modificar na posicao Index, na lista Lista, o elemento que jah lah esta _ e substitui por o novo elemento Elemento. 
    nth1(Index, Lista, _, Resto),
    nth1(Index, NovaLista, Elemento, Resto).

insereObjectoEntrePosicoes(Tabuleiro, TendaOuRelva, (L, C1), (L, C2)) :-
    /*      
    Funcao que eh verdade se Tabuleiro eh um tabuleiro e (L,C1) e (L, C2) serao as coordenadas entre as quais (incluindo) 
    se irah inserir o objeto TendaOuRelva.
    */

    insereObjectoCelula(Tabuleiro,TendaOuRelva, (L, C1)),
    insereObjectoCelula(Tabuleiro,TendaOuRelva, (L, C2)),                                     %Primeiramente inserimos com recurso a funcao imediatamente acima nas posicoes (L, C1) e (L, C2) os objetos.
    insereNoNovoTab(Tabuleiro, TendaOuRelva, (L, C1),(L, C2), NovoTabuleiro),                 %insereNoNovoTab vai tratar das posicoes entre (L, C1) e (L,C2) e o NovoTabuleiro jah vai ter as devidas posicoes modificadas.     
    Tabuleiro = NovoTabuleiro,!.                                                              %inicialmente o NovoTab serah igual ao Tab inicial.

insereNoNovoTab(_,_,Cord1,Cord2,_):-                                                          %Caso terminal, onde ambas as coordenadas sao as mesmas.
    Cord1 == Cord2.
insereNoNovoTab(Tabuleiro, TendaOuRelva, (L, C1),(L, C2), NovoTabuleiro):-              
    todasCelulas(Tabuleiro,TodasCelulas),
    nextto((L,C1),Posicao,TodasCelulas),                                                      %Como TodasCelulas eh uma lista ordenada das celulas a funcao auxiliar nextto eh muito util, ela fornece a posicao a direita de (L,C1), Posicao. Quando a posicao a direita de (L,C1) for (L,C2) a recursao acaba.
    insereObjectoCelula(Tabuleiro,TendaOuRelva,Posicao),                               
    insereNoNovoTab(Tabuleiro,TendaOuRelva,Posicao,(L, C2),NovoTabuleiro).

relva(Puzzle) :-
    /*      
    Funcao que eh verdade se o Puzzle apos a aplicacao do predicado tem relva em todas as linhas e colunas cujo
    seu numero de de tendas antingiu o numero de tendas possiveis dessa mesma linha ou coluna. Ou seja, enche de relva
    todas as linhas e colunas que nao possam ter mais nenhum objeto somente relva.
    */
          
    lista_linhas(Puzzle, ListaLin),                                                          %Funcao auxiliar que entra no Puzzle e retira a lista correspondente ao numero de tendas por linha do tabuleiro.
    lista_colunas(Puzzle, Lista_tendas_Colunas),                                             %Funcao auxiliar que entra no Puzzle e retira a lista correspondente ao numero de tendas por colunas do tabuleiro.
    lista_tabuleiro(Puzzle, Tab),                                                            %Funcao auxiliar que entra no Puzzle e retira o tabuleiro.
    transpose(Tab,Tabtransposta),
    relvaAUX(Tabtransposta,Lista_tendas_Colunas, TabModificado),                             %relvaAUX eh a funcao auxiliar que vai iterar o tabuleiro, linha por linha e enche as linhas de relva tal como suposto.
    transpose(TabModificado,TabT),                                                           %Tal como eh feito nas funcoes acima a funcao transpose eh util para utilizar a funcao relvaAUX nas as colunas (que no tabuleiro transposto corresponde ahs linhas, dai a funcionar perfeitamente).
    relvaAUX(TabT,ListaLin, TabFinal),                                               
    TabFinal = Tab.

lista_linhas(Puzzle, ListaLin) :-                                                            %Como o Puzzle eh uma lista de tres listas (Tabuleiro, ListaLinhas, ListaColunas) basta ir ao index desejado para retirar cada uma delas.
    Puzzle = (_, ListaLin, _).  

lista_colunas(Puzzle,ListaCol):-
    Puzzle = (_, _,ListaCol).

lista_tabuleiro(Puzzle, Tab):-
    Puzzle = (Tab, _,_).

relvaAUX([],[], []).                                                                         %Base da recursao.
relvaAUX([Linha | Resto], [P | RestoLinhasTendas], [NovaLinha | RestodoNovo_tab]) :-         
          verificaNumeroTendas(Linha, Numero_DTendas),                                       %A funcao auxiliar verificaNumeroTendas eh verdade se Numero_DTendas eh o numero de tendas (t) da linha.
          P =:= Numero_DTendas,                                                              %Nesta clausula o numero de tendas da linha eh o numero maximo de tendas que a linha pode ter.
          coloca_Relva(Linha, NovaLinha),                                                    
          relvaAUX(Resto, RestoLinhasTendas, RestodoNovo_tab).

relvaAUX([Linha | Resto], [_ | RestoLinhasTendas], [Linha | RestodoNovo_tab]) :-
    relvaAUX(Resto, RestoLinhasTendas, RestodoNovo_tab).

relvaAUX([Linha | Resto], [_ | RestoLinhasTendas], _, [Linha | RestodoNovo_tab]) :-
    relvaAUX(Resto, RestoLinhasTendas, _, RestodoNovo_tab).

verificaNumeroTendas(Linha, NumTendas) :-
    linha_para_coordenadas(Linha, 1, 1, Tendas, t),
    length(Tendas, NumTendas).

coloca_Relva([], []).                                                                        %Base da recursao.
coloca_Relva([Posicao | RestodaLisa], [r | RestodaNovaLinha]) :-                             %coloca_Relva eh a funcao auxiliar recursiva que eh verdade somente se a nova linha tem relva em todas as posicoes livres. 
    var(Posicao),                                                                            %var(Posicao) verifica se a celula estah livre.
    coloca_Relva(RestodaLisa, RestodaNovaLinha).
coloca_Relva([Posicao | RestodaLisa], [Posicao | RestodaNovaLinha]) :-
    coloca_Relva(RestodaLisa, RestodaNovaLinha).

inacessiveis(Tab):-
    /*      
    Funcao que eh verdade se Tab eh um tabuleiro que apos o predicado tem relva em todas as posicoes inacessiveis, ou seja posicoes
    que de na sua vizinhanca nao possuem nenhuma arvore. Isto porque como cada tenda tem que estar na vizinhanca de uma arvore logo posicoes
    sem arvores na vizinhanca concerteza nao irao ter tendas. 
    */
    
    todasCelulas(Tab, TodasCelulas),
    inacessiveisAUX(Tab, TodasCelulas, ListaDeCelAModificar),                               %inacessiveisAUX eh um predicado que eh verdadeiro somente se ListaDeCelAModificar eh a lista de posicoes com todas as celulas inacessiveis.
    colocaRelvaEmPosicoes(Tab, ListaDeCelAModificar, _).                                    %Apos o inacessiveisAUX utilizo o predicado auxiliar colocaRelvaEmPosicoes para colocar relva (r) nas posicoes inacessiveis.

colocaRelvaEmPosicoes(_, [], _).                                                            %Base da recursao.
colocaRelvaEmPosicoes(Tabuleiro, [(L, C) | RestoPosicoes], NovoTabuleiro) :-                
    insereObjectoCelula(Tabuleiro, r, (L, C)),                                              %Recurso ao predicado insereObjetoCelula anteriormente feito e comentado.
    colocaRelvaEmPosicoes(Tabuleiro, RestoPosicoes, NovoTabuleiro),                         
    NovoTabuleiro = Tabuleiro,
    !.

inacessiveisAUX(_, [], []) :- !.
inacessiveisAUX(Tab, [Celula | Resto_das_Celulas], RestoDasPosiAmodificar):-
    vizinhanca(Celula, Vizinhanca),
    \+ vizinhanca_ntem_a(Tab, Vizinhanca),                                                 %Predicado que verifica se a vizinhanca da posicao Celula tem arvores (a), nesta clausula a vizinhanca tem de facto a entao a celula eh descartada
    inacessiveisAUX(Tab, Resto_das_Celulas, RestoDasPosiAmodificar),              
    !.

inacessiveisAUX(Tab, [Celula | Resto_das_Celulas], [Celula | RestoDasPosiAmodificar]):- 
    vizinhanca(Celula, Vizinhanca),                                                        
    vizinhanca_ntem_a(Tab, Vizinhanca),                                                    %Como neste caso a vizinhanca da celula nao tem arvore (a) a Posicao (Celula) eh adicionada a lista ListaDeCelAModificar. 
    inacessiveisAUX(Tab, Resto_das_Celulas, RestoDasPosiAmodificar).                          

vizinhanca_ntem_a(_,[]) :- !.                                                              %Base da Recursao.
vizinhanca_ntem_a(Tab, [Posicao | RestodaVizinhanca]) :-                                   %Primeiramente verifico com auxilio do predicado dentro_dos_limites se a Posicao encontra se dentro do tabuleiro.
    (dentro_dos_limites(Tab, Posicao) ->                                                   %Com auxilio do predicado cordenada_Para_Obj verifico se o Obj eh diferente de uma arvore (a), caso a posicao nao esteja dentro dos limites do tabuleiro a funcao retorna True para evitar erros desnecessarios.
        cordenada_Para_Obj(Tab, Posicao, Obj),
        dif(Obj, 'a'); true),
    vizinhanca_ntem_a(Tab, RestodaVizinhanca).

dentro_dos_limites(Tab, (L, C)) :-                                                         %O predicado dentro_dos_limites retorna True somente se a posicao estah dentro do Tab.
    length(Tab, NumLinhas),
    L >= 1,
    L =< NumLinhas,
    nth1(L, Tab, Linha),
    length(Linha, NumColunas),
    C >= 1,
    C =< NumColunas.

cordenada_Para_Obj(Tab, (L, C), Obj) :-                                                    %O predicado cordenada_Para_Obj eh verdade somente se o Obj eh o objeto correpondente a posicao (L, C) do tabuleiro inserido.
    nth1(L, Tab, Lin),
    nth1(C, Lin, Obj).


aproveita(Puzzle):-
    /*      
    O predicado aproveita eh verdade somente se o Puzzle eh um Puzzle que tem tendas em todas as linhas/colunas 
    que antes da aplicacao deste predicado tinha exatamente esse mesmo numero de celulas livres. Ou seja se antes do predicado
    existem 3 celulas livres e faltam colocar 3 tendas numa determinada linha/coluna entao apos o predicado aproveita esses 3 espacos 
    livres passam a ser ocupados por tendas.
    */
    
    relva(Puzzle),                                                                         
    lista_tabuleiro(Puzzle,Tab),
    lista_linhas(Puzzle, ListaLin),
    lista_colunas(Puzzle, Lista_tendas_Colunas), 

    transpose(Tab,Tabtransposta),
    tendaAUX(Tabtransposta,Lista_tendas_Colunas, TabF),                                   %O predicado tendaAUX (similar ao predicado RelvaAUX) eh verdade se TabF eh um tabuleiro na situacao descrita acima (descricao do aproveita). 
    transpose(TabF,Tab3),
    tendaAUX(Tab3,ListaLin, Tab4),                                                        %tendaAUX funciona apenas para as linhas, dai a utilizar antes e de seguida o predicado transpose.
    Tab4 = Tab.

tendaAUX([],[], []).                                                                      %Base da recursao.
tendaAUX([Linha | Resto], [P | RestoLinhasTendas], [NovaLinha | RestodoNovo_tab]) :-
    verifica_celLivres(Linha, NcelLivre),                                                 %verifica_celLivres eh verdade se NcelLivre eh o numero de celulas livres da respetiva Linha.
    P =:= NcelLivre,
    coloca_Tenda(Linha, NovaLinha),
    tendaAUX(Resto, RestoLinhasTendas, RestodoNovo_tab).

tendaAUX([Linha | Resto], [_ | RestoLinhasTendas], [Linha | RestodoNovo_tab]) :-
    tendaAUX(Resto, RestoLinhasTendas, RestodoNovo_tab).

tendaAUX([Linha | Resto], [_ | RestoLinhasTendas], _, [Linha | RestodoNovo_tab]) :-
    tendaAUX(Resto, RestoLinhasTendas, _, RestodoNovo_tab).

coloca_Tenda([], []).                                                                     %Predicado similar ao coloca_Relva.
coloca_Tenda([Posicao | RestodaLisa], [t | RestodaNovaLinha]) :-
    var(Posicao), 
    coloca_Tenda(RestodaLisa, RestodaNovaLinha).
coloca_Tenda([Posicao | RestodaLisa], [Posicao | RestodaNovaLinha]) :-
    coloca_Tenda(RestodaLisa, RestodaNovaLinha).

verifica_celLivres(Linha, Quantas) :-                                                     
    findall(CelulaLivre, (member(CelulaLivre, Linha), var(CelulaLivre)), CelulasLivres),  %O predicado findall coloca na lista CelulasLivres todas as posicoes que respeitem a condicao var(CelulaLivre), ou seja todas as posicoes que correspondam a celulas livres.
    length(CelulasLivres, Quantas).                                                       %Por fim, o numero de celulas livres serah o tamanho da lista CelulasLivres.

limpaVizinhancas(Puzzle) :-
    /*      
    O predicado limpaVizinhancas eh verdade se o Puzzle eh um puzzle que apos a aplicacao do predicado tem relva em todas as posicoes a volta das tendas, isto eh
    tem relva (r) na vizinhanca alargada de todas as tendas (t).
    */

    lista_tabuleiro(Puzzle, Tab),
    todasCelulas(Tab, TodasCelulas),
    limpaVizinhancasAUX(Tab, TodasCelulas, ListaDeCelAModificar),                         %O predicado limpaVizinhancasAUX eh verdade se ListaDeCelAModificar eh a lista de posicoes com todas as celulas vazias que devem ser subtituidas por relva.
    flatten(ListaDeCelAModificar, ListaAmodificar),                                       %O predicado flatten eh util pois a ListaDeCelAModificar eh uma lista de listas, algo do tipo [[Posicao,[Posicao,Posicao,Posicao]]] e apos a utilizacao do predicado ficamos com somente uma lista do tipo [Posicao,Posicao,Posicao,Posicao]
    colocaRelvaEmPosicoesDentroDoTab(Tab, ListaAmodificar, _).

limpaVizinhancasAUX(_, [], []) :- !.                                                      %Base da recursao.
limpaVizinhancasAUX(Tab, [Celula | Resto_das_Celulas], [VizinhancaAlargada | RestoDasPosiAmodificar]) :-
    cordenada_Para_Obj(Tab, Celula, Objeto),
    Objeto == t,                                                                          %Se o objeto for uma tenda (t) entao a sua vizinhanca alargada sera adicionada ah ListaDeCelAModificar.
    vizinhancaAlargada(Celula, VizinhancaAlargada),
    limpaVizinhancasAUX(Tab, Resto_das_Celulas, RestoDasPosiAmodificar),
    !.

limpaVizinhancasAUX(Tab, [_ | Resto_das_Celulas], RestoDasPosiAmodificar) :-
    limpaVizinhancasAUX(Tab, Resto_das_Celulas, RestoDasPosiAmodificar).

colocaRelvaEmPosicoesDentroDoTab(_, [], _).                                               %Base da recursao.
colocaRelvaEmPosicoesDentroDoTab(Tabuleiro, [(L, C) | RestoPosicoes], NovoTabuleiro) :-
    (L > 0, C > 0,                                                                        %Como a ListaDeCelAModificar possui posicoes que podem nao pertencer ao tabuleiro, entao eh necesario verificar se L > 0 e C > 0.
    insereObjectoCelula(Tabuleiro, r, (L, C)),
    colocaRelvaEmPosicoesDentroDoTab(Tabuleiro, RestoPosicoes, NovoTabuleiro);  
    colocaRelvaEmPosicoesDentroDoTab(Tabuleiro, RestoPosicoes, NovoTabuleiro)),           %Se a posicao nao pertencer ao tabuleiro entao eh ignorada.
    NovoTabuleiro = Tabuleiro.

unicaHipotese(Puzzle):-
    /*      
    O predicado unicaHipotese eh verdade somente se o Puzzle eh um puzzle que apos a aplicacao do predicado, todas as arvores que tinham apenas uma posicao livre na sua vizinhanca agora
    tem uma tenda. 
    */
          
    lista_tabuleiro(Puzzle, Tab),
    todasCelulas(Tab, TodasCelulas),
    todasCelulasArvores(Tab,TodasCelulas,CelulasDeArvores),                              %Predicado auxiliar que eh verdade somente se CelulasDeArvores eh uma lista do todas as posicoes que correspondem a arvores dentro do tabuleiro.
    arvoresAcolocarTenda(Tab,CelulasDeArvores, Arvores_a_modificar_vizinhanca),          %Predicado auxiliar que eh verdade somente se CelAmodificar eh uma lista de celulas que correspondem a arvores que possuem apenas uma posicao livre na sua vizinhanca.
    conjuntodeCElamodificar(Tab,Arvores_a_modificar_vizinhanca, CelAmodificar),          %Este predicado auxiliar eh verdade se CelAmodificar eh entao uma lista de celulas que correspondem a posicoes que devem ser colocadas tendas.
    flatten(CelAmodificar,C),
    colocaTendaEmPosicoes(Tab,C, _).

todasCelulasArvores(_,[],[]).                                                            %Base da recursao.
todasCelulasArvores(Tab, [Posicao | RestoDasPosi], [Posicao | RestodasArvores]):-
    cordenada_Para_Obj(Tab, Posicao, Objeto),
    Objeto == a,
    todasCelulasArvores(Tab, RestoDasPosi, RestodasArvores).

todasCelulasArvores(Tab,[_ | RestoDasPosi], RestodasArvores):-
    todasCelulasArvores(Tab, RestoDasPosi, RestodasArvores).

posicao_tem_variavel(Tab, (L, C)) :-                                                     %posicao_tem_variavel eh verdade somente se (L, C) eh uma posicao dentro dos limites do tabuleiro e se o objeto corresponde a essa posicao eh uma posicao vazia.
    dentro_dos_limites(Tab, (L, C)),
    cordenada_Para_Obj(Tab, (L, C), Obj),
    (var(Obj); (nonvar(Obj), Obj \= 'a', Obj \= 'r', Obj \= 't')).

exatamente_um_tem_variavel(Tab, Posicoes) :-                                             %exatamente_um_tem_variavel eh um predicado verdadeiro se dentro das Posicoes existir unicamente uma posicao que corresponda a uma posicao livre.
    include(posicao_tem_variavel(Tab), Posicoes, PosicoesComVariavel),                   %O include serve para incluir todas as posicoes dentro da lista Posicoes que correspondam a posicoes livres.
    length(PosicoesComVariavel, 1).                                                      %Retorna true se PosicoesComVariavel tem entao somente uma posicao.

vizinhanca_ntem_t(_,[]) :- !.                                                            %Similar a vizinhanca_ntem_a este predicado verfica se o objeto em todas as posicoes da Vizinhanca sao diferentes de tendas (t).
vizinhanca_ntem_t(Tab, [Posicao | RestodaVizinhanca]) :-
    (dentro_dos_limites(Tab, Posicao) ->                                                 %Para lidar com posicoes fora do limite do tabuleiro eh utilizado um if-then-else. Se a posicao estiver fora do tabuleiro, o predicado ignora a posicao.
        cordenada_Para_Obj(Tab, Posicao, Obj),
        Obj \== 't'; true),
    vizinhanca_ntem_t(Tab, RestodaVizinhanca).

arvoresAcolocarTenda(_, [], []).                                                         %Base da recursao.
arvoresAcolocarTenda(Tab, [PosiArvore | RestoDasPosi], [PosiArvore | RestodasArvores]) :-
    vizinhanca(PosiArvore, Vizinhanca),
    exatamente_um_tem_variavel(Tab, Vizinhanca),
    vizinhanca_ntem_t(Tab,Vizinhanca),                                                   %Se a arvore tem exatamente uma posicao livre na vizinhanca e nao tem tendas na sua vizinhanca entao eh uma arvore que entra na lista Arvores_a_modificar_vizinhanca.
    arvoresAcolocarTenda(Tab, RestoDasPosi, RestodasArvores).

arvoresAcolocarTenda(Tab, [_ | RestoDasPosi], RestodasArvores) :-
    arvoresAcolocarTenda(Tab, RestoDasPosi, RestodasArvores).

conjuntodeCElamodificar(_,[],[]).
conjuntodeCElamodificar(Tab,[Arvore | Resto], [VizinhancaFiltrada, RestoDasPosi]):-
    vizinhanca(Arvore, Vizinhanca),
    filtrar_posicoes_no_tabuleiro(Vizinhanca,Tab,VizinhancaFiltrada),                    %filtrar_posicoes_no_tabuleiro eh verdade se a VizinhancaFiltrada eh as posicoes da vizinhanca que pertecem ao tabuleiro (o predicado vizinhanca nao ignora posicoes fora do tabuleiro).
    conjuntodeCElamodificar(Tab, Resto, RestoDasPosi).

colocaTendaEmPosicoes(_, [], _).
colocaTendaEmPosicoes(Tabuleiro, [(L, C) | RestoPosicoes], NovoTabuleiro) :-
    insereObjectoCelula(Tabuleiro, t, (L, C)),
    colocaTendaEmPosicoes(Tabuleiro, RestoPosicoes, NovoTabuleiro),
    NovoTabuleiro = Tabuleiro,
    !.

dentro_dos_limitesaux(Tab, (L, C)) :-                                                    %Predicado similar a dentro_dos_limites.
    length(Tab, NumLinhas),
    L >= 1,
    L =< NumLinhas,
    nth1(L, Tab, Linha),
    length(Linha, NumColunas),
    C >= 1,
    C =< NumColunas.
    
filtrar_posicoes_no_tabuleiro(Posicoes, Tabuleiro, PosicoesFiltradas) :-              
    include(dentro_dos_limitesaux(Tabuleiro), Posicoes, PosicoesFiltradas).             %O predicado include inclui nas PosicoesFiltradas todas as Posicoes que respeitem o predicado dentro_dos_limitesaux.

valida(LArv, Lten):-
    /*      
    O predicado valida eh verdade se LArv e LTen sao as listas com coordenadas que existem respetivamente 
    arvores e tendas e eh verdade se for possivel estabelecer uma relacao em que existe uma unica tenda para cada arvore nas suas vizinhancas.
    */

    length(LArv,TamanhoArvores),
    length(Lten, TamanhoTenda),                   
    TamanhoArvores =:= TamanhoTenda,                                                    %Se o numero de tendas for diferente do numero de arvores entao claramente o predicado valida retorna false.           
    vizinhancaCompleta(LArv, VizinhacaCompleta),                                        %O predicado vizinhancaCompleta eh verdade se VizinhancaCompleta for uma lista de listas com todas as vizinhancas de todas as posicoes de LArv.
    flatten(VizinhacaCompleta, VizinhacaCompletaFlat),                                    
    verificaRelacao(Lten,VizinhacaCompletaFlat).                                        %O predicado verificaRelacao eh verdade se existe entao a relacao de um para um entre cada tenda e cada arvore.

vizinhancaCompleta([],[]).                                                              %Base da recursao.
vizinhancaCompleta([Posicao | RestoDasPosi],[Vizinhanca | RestoDasVizi]):-
    vizinhanca(Posicao, Vizinhanca),
    vizinhancaCompleta(RestoDasPosi,RestoDasVizi).

verificaRelacao([],_).                                                                  %Base da recursao.
verificaRelacao([Tenda | RestoDasTendas], VizinhacaCompletaFlat):-                        
    member(Tenda, VizinhacaCompletaFlat),                                               %Ou seja, a tenda faz parte da viznhanca de pelo menos uma das arvores.
    delete(VizinhacaCompletaFlat, Tenda, NovaVizinhacaCompletaFlat),                    %O predicado auxiliar delete apaga na lista VizinhacaCompletaFlat a Tenda e a lista NovaVizinhacaCompletaFlat eh a nova lista sem essa tenda, dessa forma garantimos que com o seguimento da recursao existe apenas uma arvore para cada tenda e vice versa.
    verificaRelacao(RestoDasTendas, NovaVizinhacaCompletaFlat).




resolve(Puzzle):-
    /*      
    O predicado resolve eh verdade apenas se o Puzzle eh um puzzle que apos a aplicacao do predicado eh um puzzle resolvido.
    */

    relva(Puzzle),
    lista_tabuleiro(Puzzle, Tab),
    inacessiveis(Tab),
    aproveita(Puzzle),
    relva(Puzzle),
    unicaHipotese(Puzzle),
    limpaVizinhancas(Puzzle),   
    aproveita(Puzzle),                                                                  %Primeiramente utilizo todas as estrategias disponiveis nos predicados existentes para completar ao maximo o tabuleiro.
    todasCelulas(Tab,PosiLivres,_), 
    todasCelulas(Tab,Arvores,a),
    todasCelulas(Tab,_,t),
    arvoresnaoconectadas(Tab,Arvores,ArvoresNaoconectadas),                             %Predicado que verifico quais sao as arvores que nao estao conectadas a nenhuma tenda (todas as arvores tem que estar conectadas a uma tenda) e armazeno na lista ArvoresNaoconectadas.
    posicoes_amudar(Tab,ArvoresNaoconectadas,PosiLivres,Amodificar),                    %Predicado que eh verdade se Amodifcar sao a lista de posicoes que temos que modificar para finalizar o tabuleiro.
    colocaTendaEmPosicoes(Tab,Amodificar,_).
    
arvoresnaoconectadas(_,[],[]).                                                          %Base da recursao.
arvoresnaoconectadas(Tab,[Arvore | RestoDasArvores],[Arvore | RestoDasPosi]):-
    vizinhanca(Arvore,Vizinhanca),
    vizinhanca_ntem_t(Tab,Vizinhanca),                                                  %Verifico que a vizinhanca nao tem nenhuma tenda.
    arvoresnaoconectadas(Tab,RestoDasArvores,RestoDasPosi).

arvoresnaoconectadas(Tab,[_ | RestoDasArvores],RestoDasPosi):-
    arvoresnaoconectadas(Tab,RestoDasArvores,RestoDasPosi).

posicoes_amudar(_,[],_,[]).                                                             %Base da recursao.
posicoes_amudar(Tab,[Arvore | OutrasArvores],PosiLivres,[Elemento | RestoAmodificar]):-
    vizinhanca(Arvore,Vizinhanca),
    exatamenteUmemComum(Vizinhanca,PosiLivres,Elemento),                                %Ou seja se existe somente um elemento em comum nas listas Vizinhanca e PosiLivres eh porque essa posicao tem que ter tenda.
    posicoes_amudar(Tab,OutrasArvores,PosiLivres, RestoAmodificar).

posicoes_amudar(Tab,[_ | OutrasArvores],PosiLivres,RestoAmodificar):-
    posicoes_amudar(Tab,OutrasArvores,PosiLivres, RestoAmodificar).

exatamenteUmemComum(Lista1, Lista2, Elemento) :-                                        %O predicado auxiliar exatamenteUmemComum eh verdade somente se na lista1 e na lista2 existe exatamente um elemento em comum, neste caso posicao.
    findall(Elemento, (member(Elemento, Lista1), member(Elemento, Lista2)), ElementosEmComum),
    length(ElementosEmComum, 1),
    nth0(0, ElementosEmComum, Elemento).