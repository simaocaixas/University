##PROJETO FP 2023  

# Este primeiro projeto de Fundamentos da Programação consiste em desenvolver funções que permitam obter certas
# informações sobre um território formado apenas por caminhos verticais e horizontais. As colunas de cada territorio
# estão nomeadas com letras de A-Z e as respetivas linhas numeradas de 1-99. 
# As intercesões deste territorio podem ou não estar ocupadas por montanhas. As interseções livres adjacentes às montanhas formam um vale.
# Podem existir montanhas ou vales conectados e assim formam cadeias. Na conclusão deste projeto será possivel ver e verificar: as colunas e linhas de um territorio
# as suas montanhas, os seus vales e cadeias. 

def eh_territorio(t):

     """

     Recebe um argumento de qualquer tipo e retorna True ou False, caso o argumento
     corresponda a um territorio valido, isto é, entre outras condições
     um tuplo de subtuplos com o mesmo comprimento e em que todos os elementos do subtuplo são 0 ou 1.

     eh_territorio: universal -> booleano

     """

     permitido = [0,1]    
     #Tuplo com os elementos permitidos de cada subtuplo
 
     if not isinstance(t,tuple):            
          return False     
     if t == ():
          return False

     for subtuplo in t:
          if not isinstance (subtuplo,tuple):
               return False
          for intercecao in subtuplo:
               if not isinstance(intercecao,int):
                    return False
               if intercecao not in permitido:
                    return False
               if subtuplo == ():
                    return False
               if len(subtuplo) != len(t[0]):
                    return False
     #Conjunto de condições para os subtuplos do tuplo
                        
     if len(t) > 26:
          return False
     if len(t) < 0:
          return False
     if len(t[0]) > 99:
          return False
     #Condições para o tamanho de cada linha/tuplo

     return True


def obtem_ultima_intersecao(t):     

     """

     Recebe um territorio e devolve a intersecao do extremo superior direito. 
     Ou seja recebe um tuplo de tuplos e retorna um tuplo com o valor correspondente
     à interceção da ultima coluna com a ultima linha.

     obtem_ultima_intersecao: territorio -> intersecao
      
     """

     fila = len(t[0])                        
     colunas = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"} 
     
     return((colunas[len(t)]),fila)           


def eh_intersecao(arg):

     """

     Recebe um argumento de qualquer tipo e devolve True se o argumento for de facto uma interseçao.
     Esta função nunca deve retornar erros ao utilizador. Ou seja se o argumento for um tuplo em que a primeira
     posição corresponde a uma coluna e segunda posição corresponder a uma linha, então deve retornar True, caso contrario False

     eh_intersecao: universal -> booleano

     """

     colunas_possiveis = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]  
     #Lista com as letras de A-Z possiveis para as colunas 

     if not isinstance(arg,tuple):          
          return False
     
     elif len(arg) != 2:                 
          return False
     
     elif type(arg[0]) != str:   
          return False
     elif type(arg[1]) != int:  
          return False
     elif arg[0] not in colunas_possiveis:                 
          return False
     
     elif arg[1] < 1 or arg[1] > 99:                        
          return False
          
     else: return True


def eh_intersecao_valida(t, i):
      
     """

     Recebe um territorio e uma interceção e devolve True se a interceção corresponde de facto a uma interceção dentro do terriorio.
     Ou seja retorna True se a interceção corresponde a uma das interceções linha coluna dentro do territorio.
     
     eh_intersecao_valida: territorio -> intersecao

     """
     if eh_intersecao(i):
          colunas = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"} 
          coluna_valida = []               
          #variavel que vai armazenar as colunas validas para o territorio 

          linhas_validas = len(t[0])        

          for elemento in colunas:
               if elemento < (len(t) + 1):
               #len(t) + 1 pois a identação começa no 0                      
                    coluna_valida.append(colunas[elemento])        
          if not i[0] in coluna_valida:                          
               return False
          elif i[1] < 1 or i[1] > linhas_validas:                
               #garante que o valor da linha está entre 1 o valor maximo e minimo
               return False 
          else:
               return True
     else:
          return False


def eh_intersecao_livre(t, i):
     
     """

     Recebe um territorio e uma interceção, devolve True se essa mesma interceção corresponde a uma interceção livre.
     Ou seja retorna True se é uma interceção não ocupada por montanhas. Uma interceção não ocupada por uma montanha
     tem o valor 0, uma interceção ocupada por uma montanha tem o valor 1.

     eh_intersecao_livre: territorio -> intersecao

     """

     colunas = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25} 

     coluna_indicada = (colunas[i[0]])                     
     linha_indicada = i[1] - 1                            
     #identação começa com o valor 0, temos que sempre subtrair 1 para procurar na posição certa

     posição_indicada = t[coluna_indicada][linha_indicada] 

     if posição_indicada == 1:
          return False 
     else:
          return True
     

def obtem_todas_as_interceções(t):

     """

     Uma função auxiliar que recebe um territorio e devolve todas as interceções desse mesmo territorio. Ou seja a partir de um tuplo
     de subtuplos, obtem um tuplo de subtuplos com todas as interceções no formato pretendido ('coluna',linha).

     obtem_todas_as_interceções: territorio -> interceções 

     """
     
     colunas = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"} 
     todas_as_intercecoes = ()
     contador_coluna = 1
     contador_linha = 1
     #contador_coluna vai iterar sobre o dicionario com as colunas, contador_linha serve corresponde ao numero da linha
               
     if not isinstance (t[0],tuple):
          for intercecao in t:
               todas_as_intercecoes += ((colunas[1],contador_coluna))
               contador_coluna += 1
               
               return todas_as_intercecoes
     else:
               
          for linha in t:
               for intercecao in linha:
                    todas_as_intercecoes += (((colunas[contador_linha],contador_coluna))),
                    contador_coluna += 1
               contador_coluna = 1
               contador_linha += 1
          
          return todas_as_intercecoes


def todas_as_montanhas(t):

     """

     Uma função auxiliar que recebe um territorio e devolve todas as interceções do territorio que correspondem a montanhas.
     Ou seja a partir de um tuplo de subtuplos, obtem um tuplo de subtuplos com todas as interceções no formato pretendido ('coluna',linha) e que
     obdecam à condição de ser uma montanha

     todas_as_montanhas: territorio -> interceções  

     """

     todas_as_intercecoes = (obtem_todas_as_interceções(t))
     apenas_montanhas = ()

     for intercecao in todas_as_intercecoes:
          if not eh_intersecao_livre(t,intercecao):
               apenas_montanhas += (intercecao),
          #filtra todas as montanhas e coloca no tuplo apenas_montanhas

     return apenas_montanhas



def obtem_intersecoes_adjacentes(t,i):

     """

     Recebe um territorio e uma interceção desse territorio e retorna um tuplo formado pelas interceções válidas adjacentes a essa interceção.
     A as interceções adjacentes correspondem às interceções à esquerda, à direita, em cima e em baixo. A ordem de leitura é a seguinte: baixo -> esquerda -> direita -> cima

     obtem_intercecoes_adjacentes: territorio & interceção -> tuplo 

     """

     colunas = {"Não pertence":0,"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,"Nunca pertence":27}  
     colunas_inversa = {0:"Não pertence",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z",27:"Nunca pertence"} 
     #colunas_inversas é util para reverter o numero da coluna para a respetiva letra 

     respetiva_coluna = colunas[i[0]]        
     respetiva_linha = i[1]                  
     #respetiva linha e coluna da interceção que é o centro das adjacentes

     intercecao_à_esquerda = colunas_inversa[respetiva_coluna - 1],respetiva_linha
     intercecao_à_direita = colunas_inversa[respetiva_coluna + 1],respetiva_linha

     intercecao_em_cima = colunas_inversa[respetiva_coluna],respetiva_linha + 1
     intercecao_em_baixo = colunas_inversa[respetiva_coluna],respetiva_linha - 1

     tuplo_final = ()

     for intercecao in intercecao_em_baixo,intercecao_à_esquerda,intercecao_à_direita,intercecao_em_cima:
          if eh_intersecao_valida(t,intercecao):
               tuplo_final += (intercecao,)
     #se a interceção não for valida, ou seja não estiver no territorio, não vai chegar ao tuplo_final

     return tuplo_final


def ordena_intersecoes(tup):
    
    """

    Recebe um tuplo de interceções e retorna um tuplo com essas mesmas interceções mas ordenadas de acordo com a ordem de leitura
    do territorio, isto é: baixo -> esquerda -> direita -> cima. 
    O tuplo pode estar vazio e deve retornar um tuplo vazio.
    
    ordena_intercecoes: tuplo -> tuplo

    """
    
    if not tup:
        return ()
    #pode ser vazio então retorna um tuplo vazio
    
    def ordena(tup):
    #função auxiliar para defenir a maneira de ordenar os subtuplos. ordena: tuplo -> tuplo
     
        coluna, linha = tup
        return (linha, coluna)
        #ordena primeiro as linhas e posteriormente as colunas
     
    tup_ordenado = sorted(tup, key = ordena)

    return tuple(tup_ordenado)


def territorio_para_str(t):

     """

     Recebe um territorio e devolve uma cadeia de caracteres que representa visualmente esse mesmo territorio.
     Ou seja apresenta ao utilizador as linhas e as colunas desse territorio e também as interceções. Colunas de A a Z
     linhas 1 a 99 e interceções 'X' e/ou '.' em função ao territorio introduzido. Caso o territorio não corresponder a um 
     territorio valido a função deve gerar o erro: 'territorio_para_str: argumento invalido'.

     territorio_para_str: territorio -> cad. caracters

     """

     if not eh_territorio(t):
          raise ValueError('territorio_para_str: argumento invalido')
     #verificar se é um argumento valido

     contador_de_colunas = 0
     string_com_colunas = ""
     colunas = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"} 
     
     for coluna in t:
          contador_de_colunas += 1
          string_com_colunas += colunas[contador_de_colunas]
          string_com_colunas += " "

     string_com_colunas = string_com_colunas.rstrip()
     #retira o espaço á direita para a formatação final
          
     tuplo_montanhasevales = []
     #Este tuplo vai ser utilizado para armazenar as interceções, '.' ou 'X'

     for intersecoes in range(len(t[0])):
          #range do valor do tamanho do primeiro subtuplo do territorio
          montanhas_ou_vales = []
          for subtuplo in t:
               if subtuplo[intersecoes] == 0:
                    montanhas_ou_vales.append(".")
               elif subtuplo[intersecoes] == 1:
                    montanhas_ou_vales.append("X")
          tuplo_montanhasevales.append(tuple(montanhas_ou_vales))
     

     subtuplos_strings = [' '.join(subtuplo) for subtuplo in tuplo_montanhasevales]
     linha_res = ""
     #transforma cada subtuplo em tuplo_montanhasevales em strings e adiciona no tuplo subtuplo_strings

     numero_linha = len(t[0])
     contador_de_intercecoes = -1
     espaço_em_branco = " "
     #numero_linhas será utilizada no print final e o contador_de_intercecoes funcionará para iterar sobre o tuplo subtuplos_strings

     #como a formatação depende do numero de digitos no numero_linha então se o numero for inferior a 10:
     if numero_linha < 10:
          if len(t) != 0:
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
          if len(t) != 0:
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
          
def obtem_cadeia(t,i):

     """

     Recebe um territorio e uma interseção desse territorio. Retorna um tuplo formado pelas interceções desse territorio que estão conectadas a essa interceção, incluindo-a. 
     Deve retornar as interceções pela ordem de leitura do territorio. Ou seja se a interceção corresponder a uma montanha esta função esta função retornar todas as montanhas 
     que estejam conectadas a essa montanha, igualmente para uma interceção que não seja montanha. Deve gerar o seguinte erro se algum dos argumentos não for valido: 
     'obtem_cadeia: argumentos invalidos.

     obtem_cadeia: territorio & intersesao -> tuplo

     """

     if not eh_territorio(t):
          raise ValueError('obtem_cadeia: argumentos invalidos')
     if not eh_intersecao_valida(t,i):
          raise ValueError('obtem_cadeia: argumentos invalidos')
     #verifica a validade dos argumentos

     lista_com_montanhas = []
     lista_com_montanhas.extend(todas_as_montanhas(t)) 


     #se a interceção corresponde a uma montanha, então:
     if i in lista_com_montanhas:

          cadeia_inicial = []
          cadeia_todos = []
          cadeia_inicial.append(i,)
          #cadeia_inicial inicialmente armazena apenas a interceção inicial mas durante o ciclo for vai armazenar tambem as intercecoes adjacentes que são montanhas
          #cadeia_todos inicialmente está vazia mas durante o ciclo for vai armazenar sucessivas interceções adjacentes.

          cadeia_final = ()
          #como a ordem de leitura interessa então cadeia_ordenanda corresponde à cadeia_final ordenada pela ordem de leitura


          for montanha in cadeia_inicial:
                    cadeia_todos = [obtem_intersecoes_adjacentes(t,montanha)]
                    for montanha_ou_vale in cadeia_todos[0]:                
                    #cadeia_todos[0] porque queremos impor uma ordem na qual verificamos as interceções adjacentes
                         if not eh_intersecao_livre(t,montanha_ou_vale):
                              if montanha_ou_vale not in cadeia_inicial:
                                   cadeia_inicial += [montanha_ou_vale]

          for int in cadeia_inicial:
               cadeia_final += (int),

          return ordena_intersecoes(cadeia_final)

     #se a interceção não corresponde a uma montanha, então:
     else:

          cadeia_inicial = []
          cadeia_todos = []
          cadeia_final = ()
          cadeia_inicial.append(i,)

          for não_mont in cadeia_inicial:
                    cadeia_todos = [obtem_intersecoes_adjacentes(t,não_mont)]
                    for montanha_ou_vale in cadeia_todos[0]:
                         if eh_intersecao_livre(t,montanha_ou_vale):
                              if montanha_ou_vale not in cadeia_inicial:
                                   cadeia_inicial += [montanha_ou_vale]
          #exatamente a mesma logica só que apenas para interceções não montanhas

          for int in cadeia_inicial:
               cadeia_final += (int),

          return ordena_intersecoes(cadeia_final)

def obtem_vale(t,i):

     """

     Recebe um territorio e uma interseção ocupada por uma montanha e devolve um tuplo com todos os vales da cadeia de montanhas dessa montanha.
     Ou seja retorna os vales adjacentes a todos os membros da cadeia da interceção indicada pelo utilizador. Pode retornar um tuplo vazio se não 
     existir vales e deve retornar os vales de acordo com a ordem de leitura do territorio. Deve retornar o seguinte erro se um dos argumentos for invalido:
     'obtem_vale: argumentos invalidos'

     obtem_vale: territorio & intersesao -> tuplo

     """

     if t == ():
          return ()
     #caso o territorio seja vazio esta funcao deve retornar ()
     
     if not eh_territorio(t):
          raise ValueError("obtem_vale: argumentos invalidos")
     if not eh_intersecao_valida(t,i):
          raise ValueError("obtem_vale: argumentos invalidos")
     if eh_intersecao_livre(t,i):
          raise ValueError("obtem_vale: argumentos invalidos")
     #verifica se todos os argumentos são validos e se i corresponde a uma montanha
     
     cadeia_montanhas = obtem_cadeia(t,i)
     vales_finais = ()

     for montanha in cadeia_montanhas:
          for vale_ou_montanha in obtem_intersecoes_adjacentes(t,montanha):
               if eh_intersecao_livre(t,vale_ou_montanha):
                    vales_finais += (vale_ou_montanha,)

     vales_finais_sem_repeticao = set(vales_finais)
     #retira elemnentos repetidos
          
     return ordena_intersecoes(vales_finais_sem_repeticao)


def verifica_conexao(t,i1,i2):

     """

     Recebe um territorio e duas interceções desse territorio e devolve True se as duas estão conectadas ou 
     False caso não estejas conectadas. Ou seja se as duas interceções estão na mesma cadeia então estão conectdas.
     Se algum dos argumentos for invalido então deve gerar o seguinte erro:'verifica_conexao: argumentos invalidos'.

     verifica_conexao: territorio & intersecao & intersecao -> booleano

     """
     
     if not eh_territorio(t):
          raise ValueError('verifica_conexao: argumentos invalidos')
     if not eh_intersecao_valida(t,i1):
          raise ValueError('verifica_conexao: argumentos invalidos')
     if not eh_intersecao_valida(t,i2):
          raise ValueError('verifica_conexao: argumentos invalidos')
     #verifica se todos os argumentos são validos
     
     if eh_intersecao_livre(t,i1):
          if not eh_intersecao_livre(t,i2):
               return False
     if not eh_intersecao_livre(t,i1):
          if eh_intersecao_livre(t,i2):
               return False
     #caso i1 e i2 não sejam ambos montanhas ou vales retorna False

     cadeia_de_i1 = ()
     cadeia_de_i1 += (obtem_cadeia(t,i1))

     if i2 not in cadeia_de_i1:
          return False
     else: 
          return True
     #se i2 não tiver na cadeia de i1 retorna False

def calcula_numero_montanhas(t):
        
        """

        Recebe um territorio e devolve um numero correpondente ao numero de montanhas do territorio.
        Ou seja do territorio introduzido devolve o numero de interceções que correspondem a uma montanha.
        Se o argumento não for valido deve retornar um erro com as seguinte mensagem:  'calcula_numero_montanhas: argumento invalido'.
       
        calcula_numero_montanhas: territorio -> int

        """
  
        if not eh_territorio(t):
            raise ValueError("calcula_numero_montanhas: argumento invalido")
        #verifica se o argumento é valido

        numero_de_montanhas = 0
        
        for linha in t:
              for intercecao in linha:
                    if intercecao == 1:   
                          numero_de_montanhas += 1
        #1 porque cada montanha é representada dentro do subtuplo com o valor inteiro 1
        
        return numero_de_montanhas


def calcula_numero_cadeias_montanhas(t):
      
     """

     Recebe um territorio e devolve o numero de cadeias de montanhas desse mesmo territorio. 
     Ou seja para cada montanha verifica a sua cadeia e vai retornar o numero de cadeias diferentes.
     Caso o territorio não corresponder a um teritorio valido então deve gerar um erro com a seguinte mensagem: 'calcula_numero_cadeias_montanhas: argumento invalido'.

     calcula_numero_cadeia_montanhas: territorio -> int

     """
     
     if not eh_territorio(t):
          raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
     #verifica o argumento 

     tuplo_com_todas_montanhas = todas_as_montanhas(t)
     cada_cadeia = ()
     contador_de_cadeias = 0
     tuplo_montanhas = ()

     for montanha in tuplo_com_todas_montanhas:
          if montanha not in tuplo_montanhas:
               if montanha not in cada_cadeia:
                    obtem_cadeia_montanha = obtem_cadeia(t,montanha)
                    if obtem_cadeia_montanha not in cada_cadeia:
                         cada_cadeia += (obtem_cadeia_montanha)
                         tuplo_montanhas += montanha
                         contador_de_cadeias += 1
     
               
     return contador_de_cadeias


def calcula_tamanho_vales(t):
    
    """

     Recebe um territorio e devolve o numero total de intersecoes diferentes que correspondem a todos 
     os vales do territorio. Ou seja esta função conta o numero  de vales diferentes do territorio introduzido.
     Caso o territorio não seja valido a função deve retornar o erro com a seguinte mensagem: 'calcula_tamanho_vales: argumento invalido'

     calcula_tamanho_vales: territorio -> int
    
    """

    if not eh_territorio(t):
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    #verifica o argumento 

    adjcacentes_das_cadeias = ()
    montanhas = ()
    adjcacentes_das_cadeias_semrepeticao = ()
    vales = ()
    
    montanhas += todas_as_montanhas(t)
    #tuplo com todas as montanhas do teritorio

    for cada_montanhas in montanhas:
         adjcacentes_das_cadeias += obtem_intersecoes_adjacentes(t,cada_montanhas)
     
    for intercecao in adjcacentes_das_cadeias:
        if intercecao not in adjcacentes_das_cadeias_semrepeticao:
            adjcacentes_das_cadeias_semrepeticao += (intercecao),
    
    for montanha_ou_vale in adjcacentes_das_cadeias_semrepeticao:
         if eh_intersecao_livre(t,montanha_ou_vale):
              vales += (montanha_ou_vale),
    #Verifica se é de facto vale

    return len(vales)
