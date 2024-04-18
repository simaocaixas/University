##PROJETO 2 FP 2023   

#Titulo do projeto: GO

# Data: 23/10/2023
#
#                                                                                      GO - O projeto
#
#Este segundo projeto de Fundamentos da Programação consiste escrever um programa, em python que permita jogar GO. Dentro deste programa defino os tipos abstratos de dados que deverão
#ser utilizados para a execução do mesmo. Para além disso é necessario um conjunto de funções adicionais. Cada função à partida está comentada de acordo com o nivel de abstração de dados 
#da mesma e com a identificação necessaria. 
#
#                                                                                      GO - Informaões uteis - Notas
#
#O Go é um jogo de tabueliro de estrategia milenar originário da China. Os jogadores devem alternadamente colocar pedras no tabuleiro, brancas ou pretas dependendo do jogador, com o simples objetivo
#de formar territorios dentro do tabuleiro. Ganha quem antingir maior pontuação, ou seja, quem obtiver o territorio maior.
#Um tabueleiro de go, denominado tambem por goban é um tabuleiro retangular
#19 x 19, neste projeto adotamos 3 tamanhos de tabuleiros, 9 x 9, 13 x 13 e 19 x 19. Cada coluna identifica-se de A até S e cada linha de 1 até 19. A ordem de leitura das interseçõesoes do goban é sempre feita da esquerda para a direita seguida de
#baixo para cima. Duas interceções dizem-se adjacentes se estão conectadas por uma linha horizontal e vertical. Uma interseção está livre se não tem nenhuma pedra, caso contrario está ocupada.
#Uma cadeia de pedras é um conjunto de pelo menos uma ou mais pedras conectadas entre si. As liberdades de uma pedra são o conjunto de interseções adjacentes que não estão ocupadas, às interseções
#adjacentes de um territorio que estão ocupadas chamamos fronteira. As duas regras de Go que utilizamos no projeto foram as seguintes: Suicídio: a jogada de um jogador é considerada ilegal se uma ou mais pedras da cor
#daquele jogador ficarem sem liberdades apos a resolução da jogada; Repetição (ko): a jogada é considerada ilegal se tiver o efeitde criar um estado do tabuleiro que ocorreu. Para este trabalho
#é suficiente considerar a regra K.O apenas para a jogda anterior da jogda do adversario ou seja consideramos que é o tabuleiro n, então temos que comparar que o tabuleiro n+1 (que resultaria da nossa jogada) é diferente do tabuleiro n-1 
#####


#TAD UM - INTERSEÇÃO 

#Construtor
def cria_intersecao(col,lin):

    """
    Recebe um caracter e um inteiro, coluna e linha respetivamente. Deve gerar um erro com a seguinte
    mensagem caso os argumentos não sejam validos: 'cria_intersecao: argumentos invalidos'.
    Deve devolver a representação escolhida para uma interseção, neste caso um tuplo.
    
    cria_intersecao: str X int -> intersecao

    """

    if isinstance(col, dict) or isinstance(lin, dict):
        raise ValueError('cria_intersecao: argumentos invalidos')
    if type(col) != str:
        raise ValueError('cria_intersecao: argumentos invalidos')
    if len(col) != 1:
        raise ValueError('cria_intersecao: argumentos invalidos')
    if not 65 <= ord(col) <= 83:
        raise ValueError('cria_intersecao: argumentos invalidos')
    #verificação da coluna, ord(col) tem que estár entre ord('A') e ord('S') 

    if type(lin) != int:
        raise ValueError('cria_intersecao: argumentos invalidos')
    if lin <= 0:
        raise ValueError('cria_intersecao: argumentos invalidos')
    if lin > 19:
        raise ValueError('cria_intersecao: argumentos invalidos')
    #verificação da linha, 19 pois a letra S corresponde a 19 letra do alfabeto
    else:
        return [col,lin]
    #representação escolhida para a interseção -> lista

#Seletor
def obtem_col(i):

    """
    Recebe uma intersecao e devolve a coluna da interseção introduzida.

    Obtem_col: intersecao -> str

    """

    return i[0]

#Seletor
def obtem_lin(i):

    """
    Recebe uma intersecao e devolve a linha da interseção introduzida.

    Obtem_lin: intersecao -> str

    """

    return i[1]

#Reconhecedor
def eh_intersecao(arg):

    """
    Verifica a validade de acordo com a minha representação de interseção e retorna True 
    caso o arg seja uma interseção ou False caso não seja uma interseção.
    
    eh_intersecao: universal -> booleano

    """
    
    if not isinstance(arg,list):
        return False
    elif len(arg) != 2:
        return False
    elif type(obtem_col(arg)) != str:   
        return False
    elif type(obtem_lin(arg)) != int:  
        return False
    elif len(obtem_col(arg)) != 1:
        return False
    elif obtem_lin(arg) <= 0:
        return False
    elif not 65 <= ord(obtem_col(arg)) <= 83:
        return False
    #ord(col) tem que estár entre ord('A') e ord('S') 
    else:
        return True
    
#Teste
def intersecoes_iguais(i1,i2):
    
    """
    Recebe um caracter e um inteiro, coluna e linha respetivamente. Deve gerar um erro com a seguinte
    mensagem caso os argumentos não sejam validos: 'cria_intersecao: argumentos invalidos'.
    Deve devolver a representação escolhida para uma interseção, neste caso uma lista.
    
    intersecoes_iguais: str X int -> intersecao

    """

    colA = obtem_col(i1)
    colB = obtem_col(i2)

    linA = obtem_lin(i1)
    linB = obtem_lin(i2)

    if colA != colB:
        return False
    if linA != linB:
        return False
    else:
        return True
    
#Transformador
def intersecao_para_str(i):
     
    """
    Recebe uma interseção e devolve uma cadeia de caracteres que representa a nossa representação de interseção.
    
    intersecao_para_str: intersecao -> str

    """

    string = ""
    #variavel que armazena a coluna e a linha em string

    string += str(obtem_col(i))
    string += str(obtem_lin(i))
    return string

#Transformador
def str_para_intersecao(s):

    """
    Recebe uma cadeia de caracteres e devolve a representação escolhida para uma interseção

    str_para_intersecao: str -> intersecao

    """
    
    coluna = ''
    linha = 0

    for caracter in s:
        if 65 <= ord(caracter) <= 90:
            coluna += caracter
    #ord(caracter) tem que estár entre ord('A') e ord('S') 
    for caracter in s:
        if 48 <= ord(caracter) <= 57:
    #ord(caracter) tem que estár entre chr(0) e chr(9), digitos permitodos 
            linha = linha * 10 + int(caracter) 
    return [coluna,linha]



#Função de alto nível
def obtem_intersecoes_adjacentes(i,l):

    """
    Recebe duas interseções a interseção i e a interseção l, l corresponde à interseção
    superior direita do goban. Retorna todas as interseções validas adjacentes a i.

    obtem_intersecoes_adjacentes: intersecao x intersecao -> tuplo

    """

    intersec = cria_intersecao(obtem_col(i),obtem_lin(i))
    #interceção introduzida de acordo com a abstração
    tuplo_final = []

    if ord('A') <= ord(obtem_col(intersec)) <= ord(obtem_col(l)) and 1 <= obtem_lin(intersec) - 1 <= obtem_lin(l):
               tuplo_final += [cria_intersecao(chr(ord(obtem_col(intersec))),obtem_lin(intersec)-1)]
    if ord('A') <= ord(obtem_col(intersec)) - 1 <= ord(obtem_col(l)) and 0 < obtem_lin(intersec) <= obtem_lin(l):
               tuplo_final += [cria_intersecao(chr(ord(obtem_col(intersec)) - 1),obtem_lin(intersec))]
    if ord('A') <= ord(obtem_col(intersec)) + 1 <= ord(obtem_col(l)) and 0 < obtem_lin(intersec) <= obtem_lin(l):
               tuplo_final += [cria_intersecao(chr(ord(obtem_col(intersec)) + 1),obtem_lin(intersec))]
    if ord('A') <= ord(obtem_col(intersec)) <= ord(obtem_col(l)) and 1 <= obtem_lin(intersec) + 1 <= obtem_lin(l):
               tuplo_final += [cria_intersecao(chr(ord(obtem_col(intersec))),obtem_lin(intersec) + 1)]
    #vericação se a coluna é valida, ou seja se está entre a coluna A e a coluna da ultima interceção em cima à direita e se a linha está entre 1 e a linha da ultima interceção em cima à direita, ord('caracter') transforma o caracter em um numero 
    #o que permite fazer este tipo de verificação. Adiciono depois no tuplo final com a função construtora que permite manter a abastração.
    
    return tuple(tuplo_final)

#Função de alto nível
def ordena_intersecoes(t):

    """
    Recebe um tuplo com interseções e devolve um tuplo com essas mesmas interseções
    mas ordenadas de acordo com a ordem de leitura do tabueliro de GO. 
    Ordem de leitura -> baixo esquerda direita cima

    ordena_intersecoes:  tuplo -> tuplo

    """

    tuplo_a_ordenar = ()

    for interse in t:
        tuplo_a_ordenar += (cria_intersecao(obtem_col(interse),obtem_lin(interse))),
    #transforma cada interseção na minha representação de interseção

    def ordena_int(tuplo):
        """
        Função que define a ordem a ser usada para odenar o tuplo introduzido.

        ordena_int: tutplo -> tuplo

        """

        linha = obtem_lin(tuplo)
        coluna = obtem_col(tuplo)
        return (linha, coluna)
         
    ordenado = sorted(tuplo_a_ordenar, key = ordena_int)
    #ordena o tuplo de acordo com a função defenida 

    return tuple(ordenado)

#TAD DOiS - PEDRA

#Construtor
def cria_pedra_branca():
    
    """
    Não recebe nenhum argumento e devolve a representação escolhida para a pedra branca.
    Neste caso uma string.

    cria_pedra_branca: nenhum arguemento -> pedra

    """

    return 'O'

#Construtor
def cria_pedra_preta():

    """
    Não recebe nenhum argumento e devolve a representação escolhida para a pedra preta.
    Neste caso uma string.

    cria_pedra_preta: nenhum arguemento -> pedra

    """
    return 'X'

#Construtor
def cria_pedra_neutra():

    """
    Não recebe nenhum argumento e devolve a representação escolhida para a pedra neutra.
    Neste caso uma string.

    cria_pedra_neutra: nenhum arguemento -> pedra

    """
    return '.'

#Reconhecedor
def eh_pedra_branca(p):
        
    """
    Recebe um arguemento e deve retornar True se o arguemento for a representação escolhida de uma pedra branca.
    Caso contrario deve retornar False.

    eh_pedra_branca: universal -> booleano

    """

    pedra_branca = 'O'

    #verifica se de facto é a minha representação de pedra branca:
    if p != pedra_branca:
        return False
    else:
        return True

#Reconhecedor
def eh_pedra_preta(p):

    """
    Recebe um arguemento e deve retornar True se o arguemento for a representação escolhida de uma pedra preta.
    Caso contrario deve retornar False.

    eh_pedra_preta: universal -> booleano

    """
    
    pedra_preta = 'X'

    #verifica se de facto é a minha representação de pedra preta:
    if p != pedra_preta:
        return False
    else:   
        return True
    

#Função auxiliar
def eh_pedra_neutra(p):

    """
    Recebe um arguemento e deve retornar True se o arguemento for a representação escolhida de uma pedra preta.
    Caso contrario deve retornar False.

    eh_pedra_preta: universal -> booleano

    """
    
    pedra_neutra = '.'

    #verifica se de facto é a minha representação de pedra neutra:
    if p != pedra_neutra:
        return False
    else:   
        return True
    
#Reconhecedor
def eh_pedra(arg):
       
    """
    Recebe um arguemento e deve retornar True se o arguemento for a representação escolhida de umas das pedras.
    Caso contrario deve retornar False.

    eh_pedra: universal -> booleano

    """

    if type(arg) != str:
        return False
    if len(arg) != 1:
        return False
    
    #verifica se é uma das tres pedras, se for retorna True, caso contrario retorna False
    if not eh_pedra_branca(arg):
        if not eh_pedra_preta(arg):
            if not eh_pedra_neutra(arg):
                return False

    return True   
 
#Teste
def pedras_iguais(p1,p2):

    """
    Recebe duas pedras, p1 e p2 e deve retornar True apenas se p1 e p2 são pedras iguais. Retorna False
    caso contrarios

    pedras_iguais: universal x universal -> booleano

    """

    if not eh_pedra(p1):
        return False
    if not eh_pedra(p2):
        return False
    #Verifico primeiro se ambas as pedras são de factos pedras

    #Verifico se a primeira pedra é uma pedra Y e se a segunda pedra é Y então devolve True, retorna False caso contrario
    if eh_pedra_branca(p1):
        if not eh_pedra_branca(p2):
            return False
        
    if eh_pedra_preta(p1):
        if not eh_pedra_preta(p2):
            return False
    
    if not eh_pedra_preta(p1):
        if not eh_pedra_branca(p1):
            if eh_pedra_branca(p2) or eh_pedra_preta(p2):
                return False    
    return True

#Transformador
def pedra_para_str(p):

    """
    Recebe uma pedra e devolve a representação do jogador 'dono' da pedra. O jogador 'dono' da 
    pedra é o jogador branco ou o preto ou se não tiver, neutro.

    pedra_para_str: pedra -> string

    """
    
    pedra_b,pedra_p,pedra_n = 'O','X','.'
    
    #verifica se o argumento é igual a qual das minhas representações de pedras
    if pedra_b == p:
        return pedra_b
    
    if pedra_p == p:
        return pedra_p
    
    if pedra_n == p:
        return pedra_n

#Função de alto nível
def eh_pedra_jogador(p):

    """
    Recebe uma representação de uma pedra e devolve True se a pedra corresponder a uma pedra
    de um jogador. Devolve False caso contrario.

    eh_pedra_jogador: pedra -> booleano

    """

    if not eh_pedra(p):
        return False
    #se o argumento não corresponder a uma pedra então devolve False

    if not eh_pedra_branca(p):
        if not eh_pedra_preta(p):
            return False
    
    return True


#TAD TRES - PEDRA

#Construtor
def cria_goban_vazio(n):

    """
    Recebe um inteiro n que representa o numero de linhas e colunas de um tabuleiro de GO.
    Devolve um tabuleiro (n x n) sem interceções ocupadas. Esta função deve gerar um erro se
    n não for um valor valido: 'cria_goban_vazio: argumento invalido'.
    Consideramos que um goban (tabuleiro de GO) pode ser 9 x 9, 13 x 13, ou 19 x 19.

    cria_goban_vazio: inteiro -> goban

    """

    if type(n) != int:
        raise ValueError('cria_goban_vazio: argumento invalido')
    
    #verifico se n corresponde de facto a um tamanho valido de um goban
    if n != 9 and n != 13 and n != 19:
        raise ValueError('cria_goban_vazio: argumento invalido')
    goban = [[cria_pedra_neutra()] * n for int in range(n)]

    return goban

#função auxiliar
def obtem_todas_as_interceções(g):

    """
    Função auxiliar utilizada em funções basicas que recebe um goban e devolve uma lista com todas as interceções desse goban
    na forma escolhida para representar uma interseção, neste caso uma lista. Ou seja devolve uma lista com sublistas.

    obtem_todas_as_interseções: goban -> list

    """

    colunas = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S"} 
    todas_as_intercecoes = []
    contador_coluna = 1
    contador_linha = 1

    o_meugoban = cria_goban_vazio(len(g))
               
    for linha in o_meugoban:
        for intercecao in linha:
            todas_as_intercecoes += [[colunas[contador_linha],contador_coluna]]
            contador_coluna += 1
        contador_coluna = 1
        contador_linha += 1


    return todas_as_intercecoes

#Reconhecedor
def eh_intersecao_neutra(g, i):

    """
    Função auxiliar utilizada em obtem_cadeia que recebe um goban e uma interceção e retorna True
    se a interseção corresponde a uma pedra neutra. Ou seja apenas retorna True se a pedra da interceção 
    i for neutra, e retorna False caso contrario.

    eh_intersecao_neutra: goban x interseção -> booleano
    
    """

    colunas = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18} 

    coluna_indicada = colunas[obtem_col(i)]
    linha_indicada = obtem_lin(i) - 1
    #obtem_lin(i) - 1 pois a identação começa no 0          

    posição_indicada = g[coluna_indicada][linha_indicada] 

    #verifica se de facto corresponde a uma pedra neutra
    if eh_pedra_jogador(posição_indicada):
         return False 
    
    return True

#Reconhecedor
def eh_intersecao_pbranca(g, i):

    """
    Função auxiliar utilizada em obtem_cadeia que recebe um goban e uma interceção e retorna True
    se a interseção corresponde a uma pedra branca. Ou seja apenas retorna True se a pedra da interceção 
    i for branca, e retorna False caso contrario.

    eh_intersecao_pbranca: goban x interseção -> booleano
    
    """

    colunas = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18} 

    coluna_indicada = colunas[obtem_col(i)]
    linha_indicada = obtem_lin(i) - 1          

    posição_indicada = g[coluna_indicada][linha_indicada] 

    #verifica se de facto corresponde a uma pedra branca
    if posição_indicada != cria_pedra_branca():
         return False 
    else:
         return True
    
#Reconhecedor
def eh_intersecao_ppreta(g, i):
        
    """
    Função auxiliar utilizada em obtem_cadeia que recebe um goban e uma interceção e retorna True
    se a interseção corresponde a uma pedra preta. Ou seja apenas retorna True se a pedra da interceção 
    i for preta, e retorna False caso contrario.

    eh_intersecao_ppreta: goban x interseção -> booleano
    
    """

    colunas = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18} 

    coluna_indicada = colunas[obtem_col(i)]
    linha_indicada = obtem_lin(i) - 1          

    posição_indicada = g[coluna_indicada][linha_indicada] 

    #verifica se de facto corresponde a uma pedra preta
    if posição_indicada != cria_pedra_preta():
         return False 
    else:
         return True

#Construtor
def cria_goban(n,ib,ip):

    """
    Recebe um inteiro n, que corresponde ao tamanho do tabuleiro de GO, ib e ip são tuplos
    com todas as interceções brancas e pretas, respetivamente desse mesmo Goban. A função deve
    gerar um VallueError com a seguinte mensagem caso os argumentos não sejam validos: 'cria_goban: argumentos invalidos'

    cria_goban: int x tuplo x tuplo -> goban
    
    """

    ver_repetidos = []
    #lista que vai armazenar as interceções e verifica se estão duplicadas ou se estão em ambos os tuplos, ip e ib

    #Conjunto de verificações para os argumentos
    if not isinstance(n,int):
        raise ValueError('cria_goban: argumentos invalidos')
    if n != 9 and n != 13 and n != 19:
        raise ValueError('cria_goban: argumentos invalidos')
    if not isinstance(ib,tuple):
        raise ValueError('cria_goban: argumentos invalidos')
    if not isinstance(ip,tuple):
        raise ValueError('cria_goban: argumentos invalidos')
    for inters in ip:
        if inters in ver_repetidos:
            raise ValueError('cria_goban: argumentos invalidos')
        ver_repetidos += [inters]
    for inters in ib:
        if inters in ver_repetidos:
            raise ValueError('cria_goban: argumentos invalidos')
        ver_repetidos += [inters]
    for interseçao in ip:
        if not eh_intersecao(interseçao):
            raise ValueError('cria_goban: argumentos invalidos')
    for interseçao in ib:
        if not eh_intersecao(interseçao):
            raise ValueError('cria_goban: argumentos invalidos')

    #tamanho dos tres gobans possiveis com as tres ultimas colunas 
    colunas = {9:'I',13:'M',19:'S'}
    ultima_coluna = colunas[n]

    for interseçao in ip:
        if obtem_lin(interseçao) > n or obtem_lin(interseçao) < 1: 
            raise ValueError('cria_goban: argumentos invalidos')
        if ord(ultima_coluna) < ord(obtem_col(interseçao)) or ord(obtem_col(interseçao)) < 65: 
            raise ValueError('cria_goban: argumentos invalidos')
    
    for interseçao in ib:
        if obtem_lin(interseçao) > n or obtem_lin(interseçao) < 1: 
            raise ValueError('cria_goban: argumentos invalidos')
        if ord(ultima_coluna) < ord(obtem_col(interseçao)) or ord(obtem_col(interseçao)) < 65: 
            raise ValueError('cria_goban: argumentos invalidos')
    
    todas_as_intercecoes = obtem_todas_as_interceções(cria_goban_vazio(n))
    gob = []
    coluna = []
    while len(gob) != n:
        for intr in todas_as_intercecoes:
            if intr in ib:
                coluna += [cria_pedra_branca()]
            elif intr in ip:
                coluna += [cria_pedra_preta()]
            else:
                coluna += [cria_pedra_neutra()]
            if len(coluna) == n:
                gob += [coluna]
                coluna = []

    return gob

#Construtor
def cria_copia_goban(gob):
    
    """
    Recebe um goban e retorna uma copia desse goban. A copia do goban deve permanecer intacta apsar
    haver mudanças destrutivas no goban inicial. 

    cria_copia_goban: goban -> goban
    
    """

    #É necessario fazer uma deep copy ou seja uma copia que quando alteramos o goban original a copia não é alterada por isso defini a função deep_copia
    def deep_copia(gob):

        """
        Recebe um goban na representação que estou a utilizar e devolve uma copia do goban.

        deep_copia: goban -> goban

        """

        copia_do_goban = []

        for linha in gob:
            copia_do_goban.append(linha)

        return copia_do_goban
    
    copia_final = []
    for linha in gob:
        copia_final.append(deep_copia(linha))

    return copia_final

#Seletor
def obtem_ultima_intersecao(g):     
    
    """
    Recebe um goban e deve retornar uma interceção que corresponde à interseção do canto superior 
    direito desse mesmo goban. Ou seja a interceção da ultima coluna do goban com a ultima linha de goban.
        
    obtem_ultima_intersecao: goban -> interceção
    
    """
    
    interceções = obtem_todas_as_interceções(g)                          
    return interceções[-1]          
    # a ultima posição [-1] corresponde a interseção da ultima coluna com a ultima linha do tabuelreiro de Go

def obtem_pedra(g,i):
    
    """
    Recebe um goban e uma interseção, deve retornar a pedra que corresponde a interseção. Se a interseção não
    corresponder a uma pedra de um jogador deve retornar uma pedra neutra.
    
    obtem_pedra: goban x interseção -> pedra

    """

    #verifico o tipo de pedra e retorno essa mesma pedra
    if eh_intersecao_pbranca(g,i):
        return cria_pedra_branca()
    
    if eh_intersecao_ppreta(g,i):
        return cria_pedra_preta()
    
    else:
        return cria_pedra_neutra() 

def obtem_cadeia(g,i):
     
    """
    Recebe um goban e uma interceção, e deve devolver um tuplo formado pelas interceções, em ordem
    de leitura, das pedras da cadeia da interceção introduzida. Se a interceção introduzida não
    estiver ocupada então deve devolver a cadeia de posições livres, ou seja interceções que correspondam
    a pedras neutras. 
    
    obtem_cadeia: goban x interseção -> tuplo
    
    """

    cadeia_inicial = []
    cadeia_todos = []
    #cadeia_inicial vai, inicialmente ter apenas a interseção introduzida e depois vai armazenar as interseções que correspondem à pedra correspondente à interseção inicial
    #cadeia_todos vai armazenar todas as interseções

    ve_repetidos = []
    #monitora quais das interseções já foram 'visitdas'

    cadeia_inicial.append(i,)
    cadeia_final = ()
    
    #Se for uma interseção correspondente a uma pedra branca
    if eh_intersecao_pbranca(g,i):
            for peca in cadeia_inicial:
                if peca not in ve_repetidos:
                    cadeia_todos = [obtem_intersecoes_adjacentes(peca,obtem_ultima_intersecao(g))]
                    ve_repetidos.append(cadeia_todos)
                for pecas in cadeia_todos[0]:                
                    #cadeia_todos[0] porque queremos impor uma ordem na qual verificamos as interceções adjacentes
                    if eh_intersecao_pbranca(g,pecas):
                        if pecas not in cadeia_inicial:
                            cadeia_inicial += [pecas]

            for int in cadeia_inicial:
                cadeia_final += (int),

            return ordena_intersecoes(cadeia_final)
    
    #Se for uma interseção correspondente a uma pedra preta
    elif eh_intersecao_ppreta(g,i):
            for peca in cadeia_inicial:
                if peca not in ve_repetidos:
                    cadeia_todos = [obtem_intersecoes_adjacentes(peca,obtem_ultima_intersecao(g))]
                    ve_repetidos.append(cadeia_todos)
                cadeia_todos = [obtem_intersecoes_adjacentes(peca,obtem_ultima_intersecao(g))]
                for pecas in cadeia_todos[0]:                
                    #cadeia_todos[0] porque queremos impor uma ordem na qual verificamos as interceções adjacentes
                    if eh_intersecao_ppreta(g,pecas):
                        if pecas not in cadeia_inicial:
                            cadeia_inicial += [pecas]
                            
            for int in cadeia_inicial:
                cadeia_final += (int),

            return ordena_intersecoes(cadeia_final)
        
    #Se for uma interseção correspondente a uma pedra neutra
    elif eh_intersecao_neutra(g,i):
            for peca in cadeia_inicial:
                if peca not in ve_repetidos:
                    cadeia_todos = [obtem_intersecoes_adjacentes(peca,obtem_ultima_intersecao(g))]
                    ve_repetidos.append(cadeia_todos)
                cadeia_todos = [obtem_intersecoes_adjacentes(peca,obtem_ultima_intersecao(g))]
                for pecas in cadeia_todos[0]:                
                    #cadeia_todos[0] porque queremos impor uma ordem na qual verificamos as interceções adjacentes
                    if eh_intersecao_neutra(g,pecas):
                        if pecas not in cadeia_inicial:
                            cadeia_inicial += [pecas]
                            
            for int in cadeia_inicial:
                cadeia_final += (int),

            return ordena_intersecoes(cadeia_final)


def coloca_pedra(g,i,p):
     
    """
    Recebe um goban, uma interceção e uma pedra e a função deve retornar o mesmo goban
    com a pedra introduzida na interceção indicada. Deve modificar destrutivamente o goban
    introduzido.
    
    coloca_pedra: goban x interseção x pedra -> goban
    
    """

    colunas = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18} 
    coluna = colunas[obtem_col(i)]

    linha = obtem_lin(i) - 1
    
    coluna = colunas[obtem_col(i)]

    #como estou a usar uma lista de listas posso colocar diretamente a pedra:
    g[coluna][linha] = p
    return g

def remove_pedra(g,i):
     
    """
    Recebe um goban e uma interceção e a função deve retornar o mesmo goban 
    sem a pedra correspondente a posição introduzida. Ou seja a interceção introduzida
    deve corresponder a uma pedra neutra. Esta função modifica destrutivamente o goban.
    
    remove_pedra: goban x interseção -> goban
    
    """

    colunas = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18} 
    coluna = colunas[obtem_col(i)]

    linha = obtem_lin(i) - 1    

    #como estou a usar uma lista de listas posso remover diretamente a pedra:
    g[coluna][linha] = cria_pedra_neutra()
    return g

def remove_cadeia(g,t):
         
    """
    Recebe um goban e um tuplo com interceções e deve retornar o mesmo goban só que 
    sem as interceções do tuplo introduzido. Ou seja a função deve modificar destrutivamente o goban introduzido e as interseções
    do tuplo introduzido devem passar a corresponder a pedras neutras.

    remove_cadeia: goban x tuplo -> goban
    
    """

    colunas = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18} 

    for intersecao in t:
        linha = obtem_lin(intersecao)    
        coluna = obtem_col(intersecao)

        #para cada uma das interseções da cadeia coloco uma pedra neutra
        coloca_pedra(g,cria_intersecao(coluna,linha),cria_pedra_neutra())

    return g

   
def eh_goban(arg):
          
    """
    Recebe um goban e um tuplo com interceções e deve retornar o mesmo goban só que 
    sem as interceções do tuplo introduzido. Ou seja a função deve modificar destrutivamente o goban introduzido e as interseções
    do tuplo introduzido devem passar a corresponder a pedras neutras.

    eh_goban: universal -> booleano
    
    """

    if not isinstance(arg,list):            
        return False
    if arg == ():
        return False
    if arg == []:
        return False
    
    #variavel que obtem indiretamente o tamanho do goban
    ultima_linha = obtem_lin(obtem_ultima_intersecao(arg))
    
    if ultima_linha != 9 and  ultima_linha != 13 and ultima_linha != 19:
        return False

    #verifico se cada linha corresponde à minha representação de linha, um tuplo com as pedras
    for subtuplo in arg:
          if not isinstance (subtuplo,list):
               return False
          #para cada pedra faço
          for intercecao in subtuplo:
               if not eh_pedra(intercecao):
                    return False
               if subtuplo == ():
                    return False
               if not eh_pedra(intercecao):
                    return False
               
    if type(arg) != type(cria_goban_vazio(ultima_linha)):
        return False

    return True

def eh_intersecao_valida(g, i):

    """
    Recebe um goban e uma interseção e devolve True se a interseção está de facto dentro do tabuleiro de GO (goban).
    Se a interseção não corresponder a uma interseção do goban então a função deve retornar False.

    eh_intersecao_valida: goban x intersecao -> booleano
    
    """

    intersecao = cria_intersecao(obtem_col(i),obtem_lin(i))
    ultima_intersecao = obtem_ultima_intersecao(g)

    if eh_intersecao(intersecao):
        colunas = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S"} 
        coluna_valida = []               
        
        for elemento in colunas:
            if elemento <= obtem_lin(ultima_intersecao):
                coluna_valida.append(colunas[elemento])

        if not obtem_col(intersecao) in coluna_valida:                          
            return False
        
        if obtem_lin(intersecao) < 1 or obtem_lin(intersecao) > obtem_lin(ultima_intersecao):                
            return False 
        
        return True

    return False
    

def gobans_iguais(g1,g2):

    """
    Recebe dois gobans, g1 e g2 e devolve True apenas se os dois gobans forem exatamente iguais.
    Caso contrario deve retornar False
    
    obtem_cadeia: goban x goban -> booleano
    
    """
    todas_as_intercecoes = ()
    
    ultima_intg1 = obtem_ultima_intersecao(g1)
    ultima_intg2 = obtem_ultima_intersecao(g2)

    #se o tamanho dos gobans não forem iguais então retorna false
    if ultima_intg1 != ultima_intg2:
        return False
    
    #List comprehension com todas as interseções
    if obtem_col(ultima_intg1) == 'I':
        colunas = 'ABCDEFGHI'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 10)]
    if obtem_col(ultima_intg1) == 'M':
        colunas = 'ABCDEFGHIKLM'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 14)]
    if obtem_col(ultima_intg1) == 'S':
        colunas = 'ABCDEFGHIKLMNOPQRS'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 20)]

    ip1,ib1 = (),()
    ip2,ib2 = (),()

    #armazena todas as interseções que correspondem a pedras tanto do goban um como do goban dois
    for int in todas_as_intercecoes:
        if eh_intersecao_pbranca(g1,int):
            ib1 += (int,)
        if eh_intersecao_ppreta(g1,int):
            ip1 += (int,)
    for int in todas_as_intercecoes:
        if eh_intersecao_pbranca(g2,int):
            ib2 += (int,)
        if eh_intersecao_ppreta(g2,int):
            ip2 += (int,)

    #por fim verifica se são iguais
    if ip1 != ip2:
        return False
    if ib1 != ib2:
        return False
 
    return True


def goban_para_str(g):

    """
    Recebe um goban e devolve uma cadeia de caracteres que deve representar o goban
    como um tabuleiro com as seus limites bem defenidos, colunas e linhas visiveis e 
    com todas as suas peças.

    Exemplo de um Tabuleiro de GO 9 x 9:

      A B C D E F G H I
    9 O . . . . . . . .  9
    8 . . . . . . . . .  8
    7 . . . . . . . . .  7
    6 . . . . . . . . .  6
    5 . . . . . X O . .  5
    4 O . . . O X O . .  4
    3 X O . . . O . . .  3
    2 . X . . . . . . .  2
    1 X . X . . X . . .  1
      A B C D E F G H I
    
    goban_para_str: goban -> string
    
    """
    

    contador_de_colunas = 0
    #cotador_de_colunas vai precorrer cada coluna do goban introduzido
    string_com_colunas = ""
    colunas = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S"}
     
    for coluna in g:
        contador_de_colunas += 1
        string_com_colunas += colunas[contador_de_colunas]
        string_com_colunas += " "

    string_com_colunas = string_com_colunas.rstrip()
    #retira o espaço á direita para a formatação final  
      
    tuplo_pedras = []
    #Este tuplo vai ser utilizado para armazenar as interceções, 'O' ou 'X' ou '.'

    for intersecoes in range(len(g[0])):
        #range do valor do tamanho do primeiro subtuplo do territorio
        qualquerpedra = []
        for subtuplo in g:
            if subtuplo[intersecoes] == cria_pedra_branca():
                qualquerpedra.append(cria_pedra_branca())
            elif subtuplo[intersecoes] == cria_pedra_preta():
                qualquerpedra.append(cria_pedra_preta())
            elif subtuplo[intersecoes] == cria_pedra_neutra():
                qualquerpedra.append(cria_pedra_neutra())

        tuplo_pedras.append(qualquerpedra)

    subtuplos_strings = [' '.join(subtuplo) for subtuplo in tuplo_pedras]
    linha_res = ""
    #transforma cada subtuplo em qualquepedra em strings e adiciona no tuplo subtuplo_strings

    numero_linha = len(g[0])
    contador_de_intercecoes = -1
    espaço_em_branco = " "
    #numero_linhas será utilizada no print final e o contador_de_intercecoes funcionará para iterar sobre o tuplo subtuplos_strings

    #como a formatação depende do numero de digitos no numero_linha então se o numero for inferior a 10:
    if numero_linha < 10:
        if len(g) != 0:
            while numero_linha >= 1:
                linha_res += f'\n{espaço_em_branco}{numero_linha}{espaço_em_branco}{subtuplos_strings[contador_de_intercecoes]}{espaço_em_branco}{espaço_em_branco}{numero_linha}'
                contador_de_intercecoes -= 1
                numero_linha -= 1
            return f"   {string_com_colunas}{linha_res}\n   {string_com_colunas}"

        else: 
            numero_linha -= 1
            linha_res += f'\n{espaço_em_branco}{numero_linha}{espaço_em_branco}{subtuplos_strings[contador_de_intercecoes]}{espaço_em_branco}{espaço_em_branco}{numero_linha}'
            return f"   {string_com_colunas}{linha_res}\n   {string_com_colunas}"
          
    else:
        if len(g) != 0:
                while numero_linha >= 1:
                        if numero_linha >= 10:
                            linha_res += f'\n{numero_linha}{espaço_em_branco}{subtuplos_strings[contador_de_intercecoes]}{espaço_em_branco}{numero_linha}'
                            numero_linha -= 1
                            contador_de_intercecoes -= 1
                        else:
                            linha_res += f'\n{espaço_em_branco}{numero_linha}{espaço_em_branco}{subtuplos_strings[contador_de_intercecoes]}{espaço_em_branco}{espaço_em_branco}{numero_linha}'
                            numero_linha -= 1
                            contador_de_intercecoes -= 1

                return f"   {string_com_colunas}{linha_res}\n   {string_com_colunas}"      


def ordena_territorios(tuplo_territorio):

    """
    Função auxiliar que recebe um tuplo de territorios e devolve esse mesmo tuplo com os territorios ordenados por ordem de leitura.
    Ou seja, a função devolve um tuplo onde a ordem que os territorios estão 
    dispostos no tuplo estão de acordo com a ordem de leitura do tabuleiro de GO.

    ordena_territorios: tuplo -> tuplo
    
    """

    
    lista_ordenada = sorted(tuplo_territorio, key=lambda x: obtem_lin(x[0]))

    return lista_ordenada



def obtem_territorios(g):
    
    """
    Recebe um goban e devolve um tuplo formado por todas os territorios desse mesmo goban. A função deve
    retornar o tuplo de territorios ordenado pela ordem de leitura de um goban e cada um dos territorios deve ter
    as interseções ordenadas tambem pela ordem de leitura de um goban.

    obtem_territorios: goban -> tuplo
    
    """

    ultima_intersecao = obtem_ultima_intersecao(g)
    
    todas_as_intercecoes = ()
    tuplo_territorios = ()
    elementos_d_territorio = []


    #verifica o tamnanho do goban e cria uma lista com todas as interseções
    if obtem_col(ultima_intersecao) == 'I':
        colunas = 'ABCDEFGHI'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 10)]
    if obtem_col(ultima_intersecao) == 'M':
        colunas = 'ABCDEFGHIKLM'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 14)]
    if obtem_col(ultima_intersecao) == 'S':
        colunas = 'ABCDEFGHIKLMNOPQRS'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 20)]
          
    #precorre todas as interseções e verifica se correspondem a pedras neutras se for uma pedra neutra pertence a um territorio
    for int in todas_as_intercecoes:
        if eh_pedra_neutra(obtem_pedra(g,int)):
            if int not in elementos_d_territorio:
                elementos_d_territorio.extend(obtem_cadeia(g,int))
                obtem_cada_territorio = tuple(obtem_cadeia(g,int))
                if obtem_cada_territorio not in tuplo_territorios:
                    tuplo_territorios += ordena_intersecoes(obtem_cada_territorio),
    
    return tuple(ordena_territorios(tuplo_territorios))

def obtem_adjacentes_diferentes(goban,t):

    """ 
    Recebe um goban e um tuplo de interseções e deve retornar:
    -> Um tuplo com as interceções adjacentes que correspondam a interseções livres se as interseções introduzidas são pedras de jogadores; 
    -> Um tuplo com as interceções adjacentes que correspondam a interseções ocupadas por pedras de jogadores se as interseções introduzidas correspondem a interseções livres;

    obtem_adjacentes_diferentes: goban x tuplo -> tuplo
        
    """

    ultima_int = obtem_ultima_intersecao(goban)

    #todas_as_adjacentes vai receber todas as pedras adjacentes da cadeia t
    todas_as_adjacentes = []
    adjacentes_sem_rep = []

    #adjacentes final é a variavel final que irá ter as 'adjacentes diferentes'
    adjacentes_finais = []

    pedra_indicadora = obtem_pedra(goban,t[0])

    for interseçao in t:
        todas_as_adjacentes.extend(obtem_intersecoes_adjacentes(interseçao,ultima_int))
    
    #adjacentes_sem_rep tem todos os adjacentes sem repetição de interseções
    for elemento in todas_as_adjacentes:
        if elemento not in adjacentes_sem_rep:
            adjacentes_sem_rep += elemento,

    #verifica se queremos as interseções que correspondem a pedras neutras ou a pedras de jogadores
    if eh_pedra_preta(pedra_indicadora) or eh_pedra_jogador(pedra_indicadora):
        for adjacente in adjacentes_sem_rep:
            if eh_pedra_neutra(obtem_pedra(goban,adjacente)):
                adjacentes_finais += (adjacente,)

    if eh_pedra_neutra(pedra_indicadora):
        for adjacente in adjacentes_sem_rep:
            if eh_pedra_branca(obtem_pedra(goban,adjacente)) or eh_pedra_preta(obtem_pedra(goban,adjacente)):
                adjacentes_finais += (adjacente,)

    return tuple(ordena_intersecoes(adjacentes_finais))

def jogada(g,i,p):
     
    """ 
    Recebe um goban, uma interseção e uma pedra. Modifica destrutivamente o goban introduzido colocando a pedra introduzida
    posição indicada. Todas as as pedras do jogador contrario pertecentes a cadeias adjacentes de i que fiquem sem liberdades
    são removidas.
    
    jogada: goban x intersecao x pedra -> goban
        
    """

    intersecao_indicada = cria_intersecao(obtem_col(i),obtem_lin(i))
    tuplo_com_int = []

    #modificamos destrutivamente o goban introduzido
    coloca_pedra(g,intersecao_indicada,p)

    adjacentes_ah_int = obtem_intersecoes_adjacentes(intersecao_indicada,obtem_ultima_intersecao(g))
    
    pedrajogada = obtem_pedra(g,intersecao_indicada)
    #pedrajogada corresponde à pedra que foi colocada no tabuleiro

    for intersecao in adjacentes_ah_int:
        if obtem_pedra(g,intersecao) != pedrajogada:
            tuplo_com_int += [intersecao]
    
    cadeia_emrisco = []

    for inters in tuplo_com_int:
        if obtem_cadeia(g,inters) not in cadeia_emrisco:
            cadeia_emrisco.append(obtem_cadeia(g,inters))

    for cadeia in cadeia_emrisco:
        if obtem_adjacentes_diferentes(g,cadeia) == ():
            return remove_cadeia(g,cadeia)

    return g

def obtem_pedras_jogadores(g):

    """ 
    Recebe um goban e devolve um tuplo de dois inteiros que devem corresponder ao numero de posições ocupadas
    por pedras do jogador branco e preto, respetivamente.
    
    obtem_pedras_jogadores: goban -> tuplo
        
    """

    #variaveis que guardam a contagem das pedras
    p_brancas = 0
    p_pretas = 0

    ultima_intersecao = obtem_ultima_intersecao(g)
    todas_as_intercecoes = ()

    #verifica o tamnanho do goban e cria uma lista com todas as interseções
    if obtem_col(ultima_intersecao) == 'I':
        colunas = 'ABCDEFGHI'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 10)]
    if obtem_col(ultima_intersecao) == 'M':
        colunas = 'ABCDEFGHIKLM'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 14)]
    if obtem_col(ultima_intersecao) == 'S':
        colunas = 'ABCDEFGHIKLMNOPQRS'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 20)]

    #itera o tuplo com todas as interseções e verifica o numero de pedras pretas e brancas
    for int in todas_as_intercecoes:
        if eh_pedra_branca(obtem_pedra(g,int)):
            p_brancas += 1
        if eh_pedra_preta(obtem_pedra(g,int)):
            p_pretas += 1

    return (p_brancas, p_pretas)   

def obtem_pedras_brancas(g):

    """ 
    Função auxiliar que recebe um goban e devolve um numero inteiro correspondente ao numero de pedras brancas.
    
    obtem_pedras_brancas: goban -> inteiro
        
    """

    #variaveis que guardam a contagem das pedras
    p_brancas = 0

    ultima_intersecao = obtem_ultima_intersecao(g)
    todas_as_intercecoes = ()

    #verifica o tamnanho do goban e cria uma lista com todas as interseções
    if obtem_col(ultima_intersecao) == 'I':
        colunas = 'ABCDEFGHI'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 10)]
    if obtem_col(ultima_intersecao) == 'M':
        colunas = 'ABCDEFGHIKLM'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 14)]
    if obtem_col(ultima_intersecao) == 'S':
        colunas = 'ABCDEFGHIKLMNOPQRS'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 20)]

    #itera o tuplo com todas as interseções e verifica o numero de pedras pretas e brancas
    for int in todas_as_intercecoes:
        if eh_pedra_branca(obtem_pedra(g,int)):
            p_brancas += 1

    return p_brancas 

def obtem_pedras_pretas(g):

    """ 
    Função auxiliar que recebe um goban e devolve um numero inteiro correspondente ao numero de pedras pretas.
    
     obtem_pedras_pretas: goban -> inteiro
        
    """

      #variaveis que guardam a contagem das pedras
    p_pretas = 0

    ultima_intersecao = obtem_ultima_intersecao(g)
    todas_as_intercecoes = ()

    #verifica o tamnanho do goban e cria uma lista com todas as interseções
    if obtem_col(ultima_intersecao) == 'I':
        colunas = 'ABCDEFGHI'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 10)]
    if obtem_col(ultima_intersecao) == 'M':
        colunas = 'ABCDEFGHIKLM'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 14)]
    if obtem_col(ultima_intersecao) == 'S':
        colunas = 'ABCDEFGHIKLMNOPQRS'
        todas_as_intercecoes = [[coluna, linha] for coluna in colunas for linha in range(1, 20)]

    #itera o tuplo com todas as interseções e verifica o numero de pedras pretas e brancas
    for int in todas_as_intercecoes:
        if eh_pedra_preta(obtem_pedra(g,int)):
            p_pretas += 1

    return p_pretas

def eh_territorio_jogador_branco(g,t):

    """ 
    Função auxiliar que recebe um goban e um territorio e devolve True apenas se o territorio de facto for do 
    jogador branco. Retorna False caso contrario.

    eh_territorio_jogador_branco: goban x territorio -> booleano
        
    """

    fronteira_territorio = obtem_adjacentes_diferentes(g,t)
    
    #verifico se a fronteira correspobde apenas a pedra brancas, se for o caso então é territorio do jogador das peças brancas
    for int in fronteira_territorio:
        if not eh_pedra_branca(obtem_pedra(g,int)):
            return False        
    else:
        return True

def eh_territorio_jogador_preto(g,t):
      
    """ 
    Função auxiliar que recebe um goban e um territorio e devolve True apenas se o territorio de facto for do 
    jogador preto. Retorna False caso contrario.

    eh_territorio_jogador_preto: goban x territorio -> booleano
        
    """

    #verifico se a fronteira correspobde apenas a pedra pretas, se for o caso então é territorio do jogador das peças preto
    fronteira_territorio = obtem_adjacentes_diferentes(g,t)
    
    for int in fronteira_territorio:
        if not eh_pedra_preta(obtem_pedra(g,int)):
            return False        
    else:
        return True


def calcula_pontos(g):
     
    """ 
    Função auxiliar que recebe um goban e deve devolver um tuplo de dois numeros inteiros com as pontuações do
    jogador branco e pretom respetivamente.

    calcula_pontos: goban -> tuplo
        
    """
    

    if obtem_pedras_brancas(g) == 0 and obtem_pedras_pretas(g) == 0:
        return (0,0)
    
    pontos_pedrasbrancas = 0
    pontos_pedraspretas = 0

    pontos_pedrasbrancas += obtem_pedras_brancas(g)
    pontos_pedraspretas += obtem_pedras_pretas(g)

    territorios_de_g = obtem_territorios(g)

    #para cada um dos territorios vejo se é do jogador branco ou do jogador preto, ou de nenhum deles e adiciono a pontuação desse territorio à contagem final
    for territorio in territorios_de_g:
        if eh_territorio_jogador_branco(g,territorio):
            pontos_pedrasbrancas += len(territorio)
        if eh_territorio_jogador_preto(g,territorio):
            pontos_pedraspretas += len(territorio)

    return pontos_pedrasbrancas,pontos_pedraspretas



def calcula_pontos_brancos(g):

    """ 
    Função auxiliar que recebe um goban e deve devolver um inteiro correspondente a pontuação do jogador
    branco

    calcula_pontos_brancos: goban -> tuplo
        
    """


    if obtem_pedras_brancas(g) == 0 and obtem_pedras_pretas(g) == 0:
        return 0
    
    pontos_pedrasbrancas = 0

    pontos_pedrasbrancas += obtem_pedras_brancas(g)

    territorios_de_g = obtem_territorios(g)

    #diferente da função calcula_pontos nesta vejo apenas se o territorio pertence ao jogador correspondente as brancas
    for territorio in territorios_de_g:
        if eh_territorio_jogador_branco(g,territorio):
            pontos_pedrasbrancas += len(territorio)

    return pontos_pedrasbrancas



def calcula_pontos_pretas(g):

    """ 
    Função auxiliar que recebe um goban e deve devolver um inteiro correspondente a pontuação do jogador
    preto

    calcula_pontos_pretas: goban -> tuplo
        
    """

    if obtem_pedras_brancas(g) == 0 and obtem_pedras_pretas(g) == 0:
        return 0
    
    pontos_pedraspretas = 0

    pontos_pedraspretas += obtem_pedras_pretas(g)

    territorios_de_g = obtem_territorios(g)

    #diferente da função calcula_pontos nesta vejo apenas se o territorio pertence ao jogador correspondente as pretas
    for territorio in territorios_de_g:
        if eh_territorio_jogador_preto(g,territorio):
            pontos_pedraspretas += len(territorio)

    return pontos_pedraspretas


def eh_jogada_legal(g,i,p,l):

    """ 
    Função auxiliar que recebe um goban l, uma interseção i, uma pedra p e um outro goban l, e deve retornar 
    True se a jogada for efetivamente uma jogada legal, devolve False caso contrario. Não deve alterar nem g
    nem l. O argumento l representa o estado do tabuleiro de GO que g não pode corresponder após a jogada.

    eh_jogada_legal: goban x intersecao x pedra, goban -> booleano
        
    """

    #verifico se a interseção ubtroduzida e o goban introduzido é valido
    if not eh_intersecao(i):
        return False
    if not 65 <= ord(obtem_col(i)) <= 83:
            return False
    if not 0 < (obtem_lin(i)) <= obtem_lin(obtem_ultima_intersecao(g)):
            return False
    i = cria_intersecao(obtem_col(i),obtem_lin(i))
    if not eh_intersecao(i):
        return False
    if not eh_intersecao_valida(g,i):
        return False
    if not eh_goban(g):
        return False
        
    #copia_para_analise serve para copiar o goban inicial para poder aplicar jogadas sem modificar o goban inicial
    #estada_em_analise é a representação do goban após a jogada
    copia_para_analise = cria_copia_goban(g)
    estado_em_analise = jogada(copia_para_analise,i,p)

    #verifico se a pedra introduzida está livre
    if not eh_pedra_neutra(obtem_pedra(g,i)):
        return False
    
    #Regra K.O
    if gobans_iguais(l,estado_em_analise):
        return False

    #Regra do Suicidio
    cadeia_dajogda = obtem_cadeia(estado_em_analise,i)
    if obtem_adjacentes_diferentes(estado_em_analise,cadeia_dajogda) == ():
        return False    

    return True


def turno_jogador(g,p,l):

    """ 
    Função auxiliar que recebe um goban g, uma pedra p e um outro goban l. Deve perguntar ao jogador o que ele quer fazer no seu turno:
    -> Introduzir a letra 'P' para passar;
    -> Introduzir uma interseção para colocar a sua pedra;
    Se o jogador passar então a função retorna False, se decidir introduzir uma interseção deve retornar True. A função avalia a validade da jogada e apenas
    introduzir a pedra no tabuleiro se de facto for uma jogada legal. Se a jogada não for legal então a função volta a apresentar as opções acima. 
    O argumento l é o estado do tabuleiro que g não pode ficar após o turno do jogador.

    turno_jogador: goban,pedra,goban -> booleano
        
    """

    #dividi em dois casos, se for pedra preta ou se for pedra branca isto porque a mensagem para o utilizador muda dependendo da pedra a ser introduzida
    if eh_pedra_preta(p):
        while True:
            if p == cria_pedra_preta():
                letraP = "'P'"
                inters = input(f'Escreva uma intersecao ou {letraP} para passar [X]:')    
                if inters == 'P':
                    return False
                if eh_jogada_legal(g,str_para_intersecao(inters),p,l):
                    jogada(g,str_para_intersecao(inters),p)
                    return True
                
    else:
        while True:
            if p == cria_pedra_branca():
                letraP = "'P'"
                inters = input(f'Escreva uma intersecao ou {letraP} para passar [O]:')
                if inters == 'P':
                    return False
                if eh_jogada_legal(g,str_para_intersecao(inters),p,l):
                    jogada(g,str_para_intersecao(inters),p)
                    return True

def ver_turno_jogador(g,pedra,l):

    """ 
    Função auxiliar similar a função turno_jogador que recebe um goban g, uma pedra p e um outro goban l. Deve perguntar ao jogador o que ele quer fazer no seu turno:
    -> Introduzir a letra 'P' para passar;
    -> Introduzir uma interseção para colocar a sua pedra;
    Se o jogador passar então a função retorna False, se decidir introduzir uma interseção deve retornar True. A função avalia a validade da jogada e apenas
    introduzir a pedra no tabuleiro se de facto for uma jogada legal. Se a jogada não for legal então a função volta a apresentar as opções acima. Esta função
    diferete da função turno_jogador retorna tambem ao utilizador uma representação grafica do tabueleiro com a função goban_para_str;

    Escreva uma intersecao ou 'P' para passar [O]:F5
    Branco (O) tem 62 pontos
    Preto (X) tem 17 pontos
      A B C D E F G H I
    9 . . . . . . . . . 9
    8 . . O O O O O O O 8
    7 . . O X X X X X O 7
    6 . O X O O O O X O 6
    5 . O X O . O O X O 5
    4 . O X O O O X X . 4
    3 . O X X X X X . O 3
    2 . . O O O O O O . 2
    1 . . . . . . . . . 1
      A B C D E F G H I

    O argumento l é o estado do tabuleiro que g não pode ficar após o turno do jogador.

    ver_turno_jogador: goban,pedra,goban -> booleano
        
    """
    
    #A principal diferenca desta função para a turno_jogador é que apos o utilizador escolher passar ou jogar a pedra ele consegue ver o tabuleiro. Utilizei dois prints antes da função retornar False ou True.
    if eh_pedra_preta(pedra):
        while True:
                letraP = "'P'"
                inters = input(f'Escreva uma intersecao ou {letraP} para passar [X]:')
                if inters == 'P':
                    print(f'Branco (O) tem {calcula_pontos_brancos(g)} pontos\nPreto (X) tem {calcula_pontos_pretas(g)} pontos') # <--
                    print(goban_para_str(g))                                                                                     # <--
                    return False
                if eh_jogada_legal(g,str_para_intersecao(inters),pedra,l):
                    jogada(g,str_para_intersecao(inters),pedra)
                    print(f'Branco (O) tem {calcula_pontos_brancos(g)} pontos\nPreto (X) tem {calcula_pontos_pretas(g)} pontos')
                    print(goban_para_str(g))
                    return True
    else:
        while True:
            letraP = "'P'"
            inters = input(f'Escreva uma intersecao ou {letraP} para passar [O]:')
            if inters == 'P':
                print(f'Branco (O) tem {calcula_pontos_brancos(g)} pontos\nPreto (X) tem {calcula_pontos_pretas(g)} pontos')
                print(goban_para_str(g))
                return False
            if eh_jogada_legal(g,str_para_intersecao(inters),pedra,l):
                jogada(g,str_para_intersecao(inters),pedra)
                print(f'Branco (O) tem {calcula_pontos_brancos(g)} pontos\nPreto (X) tem {calcula_pontos_pretas(g)} pontos')
                print(goban_para_str(g))
                return True
            


def go(n,tb,tn):
    
    """ 
    Função principal que então permite jogar um jogo completo de GO. Recebe um inteiro que corresponde à dimensão do tabueleiro, 9 x 9 ou 13 x 13 ou 19 x 19,
    dois tuplos,tb e tn, com a representação das interseçoes de pedras brancas e pedras pretas respetivamente.
    O jogo termina quando ambos os jogadores, consecutivamente passarem a vez. Se o jogador com as pedras brancas ganhar a função retorna True, caso contrario
    retorna False.
    A função gera um ValueError se um dos argumentos introduzidos não for valido: 'go: argumentos invalidos'.

    turno_jogador: goban,pedra,goban -> booleano
        
    """
    

    ver_repetidos = []

    #verifico se os arguementos são de facto validos
    if not isinstance(n,int):
        raise ValueError('go: argumentos invalidos')
    if n != 9 and n != 13 and n != 19:
        raise ValueError('go: argumentos invalidos')
    #numeros validos para n, tamanho do goban
    if not isinstance(tb,tuple):
        raise ValueError('go: argumentos invalidos')
    if not isinstance(tn,tuple):
        raise ValueError('go: argumentos invalidos')
    
    if len(tb) == 1:
        ib = tuple(tb)
    else:
        for inters in tb:
            if type(inters) == int:
                raise ValueError('go: argumentos invalidos')
        ib = tuple(str_para_intersecao(i) for i in (tb))

    if len(tn) == 1:
        ip = tuple(tn)
    else:
        for inters in tn:
            if type(inters) == int:
                raise ValueError('go: argumentos invalidos')
        ip = tuple(str_para_intersecao(i) for i in (tn))

    #é necessario verificar se as interseções em ip e ib são interseções repetidas
    for inters in ib:
        if inters in ver_repetidos:
            raise ValueError('go: argumentos invalidos')
        ver_repetidos += [inters]
    for inters in ip:
        if inters in ver_repetidos:
            raise ValueError('go: argumentos invalidos')
        ver_repetidos += [inters]

    #depois verificar se as interceções de ip e ib são validas
    for inters in ib:
        if type(inters) == int:
            raise ValueError('go: argumentos invalidos')
        if type(obtem_col(inters)) != str:
            raise ValueError('go: argumentos invalidos')
        if len(obtem_col(inters)) != 1:
            raise ValueError('go: argumentos invalidos')
        if not 65 <= ord(obtem_col(inters)) <= 83:
            raise ValueError('go: argumentos invalidos')
        if type(obtem_lin(inters)) != int:
            raise ValueError('go: argumentos invalidos')
        if obtem_lin(inters) <= 0:
            raise ValueError('go: argumentos invalidos')
        if obtem_lin(inters) > 19:
            raise ValueError('go: argumentos invalidos')
        if type(obtem_lin(inters)) != int:
            raise ValueError('go: argumentos invalidos')
        
        if not eh_intersecao_valida(cria_goban_vazio(n),inters):
            raise ValueError('go: argumentos invalidos')
    for inters in ip:
        if not eh_intersecao_valida(cria_goban_vazio(n),inters):
            raise ValueError('go: argumentos invalidos')


    g = cria_goban(n,ib,ip)
    #g é o estado inicial do goban

    print(f'Branco (O) tem {calcula_pontos_brancos(g)} pontos\nPreto (X) tem {calcula_pontos_pretas(g)} pontos')
    print(goban_para_str(g))
    #informação da disposição inicial do tabueliro acompanhado de informações sobre as pontuações 

    p = cria_pedra_preta()
    b = cria_pedra_branca()
    #pedras que serão colocadas nas jogadas(turnos)

    lista_verificar_P = []
    #lista que vai verificar se os dois jogadores passaram

    l1 = cria_goban_vazio(obtem_lin(obtem_ultima_intersecao(g)))
    l2 = cria_goban_vazio(obtem_lin(obtem_ultima_intersecao(g)))

    while len(lista_verificar_P) < 2:

        jogador_preto = ver_turno_jogador(g,p,l2)
        l2 = cria_copia_goban(g)

        if jogador_preto == False:
            lista_verificar_P += [jogador_preto]
            #o jogador passar o seu turno atribui o valor False à variavel jogador_preto, caso contrario atribui True
        else:
            lista_verificar_P.clear()
        if len(lista_verificar_P) == 2:
            break

        jogador_branco = ver_turno_jogador(g,b,l1)
        l1 = cria_copia_goban(g)

        if jogador_branco == False:
            lista_verificar_P += [jogador_branco]
            #o jogador passar o seu turno atribui o valor False à variavel jogador_preto, caso contrario atribui True   
        else:
            lista_verificar_P.clear()
        
    if calcula_pontos_brancos(g) >= calcula_pontos_pretas(g):
        return True 
    return False
