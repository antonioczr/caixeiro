
#
# Caixeiro Viajante
# Aluno: Antônio Cézar Vieira (11121911)
#


mapa = {}
matrix = []
nos = []

def main():

    global matrix
    global mapa
    global nos

    n = int(input())

    matrix = [ list(map(int, raw_input().split())) for _ in range(n) ]
    caminho = [ _ for _ in range(1, n)]

    valor = find_best(0, caminho)
    caminho = rebuild_path(0, caminho)

    circuito_str = ""

    #deixar na saida requisitada pelo prof
    for i in caminho:
        circuito_str = circuito_str + str(i + 1) + " - "

    print "Valor : " + str(valor)
    print "Circuito : " + circuito_str.strip(" - ")
    
    #import pprint 
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(mapa)

def find_best(n, caminho):

    global matrix
    global mapa
    global nos

    if len(caminho) == 0:
        return matrix[0][n]

    key = str(n) + "_" + "".join(map(str, caminho))

    # se valor ja estiver no mapa => utilizar
    if mapa.has_key(key):
        return mapa[key]["value"]
    else:
        #se nao => calcular recursivamente
        
        # guarda as chamadas para no final decidir a mais barata
        calls = []

        for i in caminho: # para cada elemento do conjunto de pontos => calcular custo
            new_caminho = [ _ for _ in caminho if _ is not i ]

            new_key = str(i) + "_" + "".join(map(str, new_caminho))

            res = find_best(i, new_caminho) + matrix[i][n] # chamada recursiva
            
            map_obj = { "value" : res, "from" : i }

            calls.append(map_obj)

        minimo = min(calls, key=lambda x : x["value"])
    
        new_key = str(n) + "_" + "".join(map(str, caminho))
        map_obj = { "value" : minimo['value'], "from" : minimo['from'] } # guarda custo no mapa de custos para possivel uso futuro
        mapa[new_key] = map_obj

        return minimo['value']


# refaz o caminho e retorna os pontos onde o custo eh menor
def rebuild_path(inicial, conj_pontos) :
    
    global mapa

    caminho = [0] # inicia com ponto zero

    pontos = conj_pontos
    chegada = inicial

    while(True):
        key = str(chegada) + "_" + "".join(map(str, pontos))
        try: # ate nao encontrar a chave no MAPA => remontar o caminho
            atual = mapa[key] 

            pontos = [ _ for _ in list(str(key.split("_")[1])) if _ not in [ str(atual['from']) ]]
            chegada = atual['from']

            caminho.append(atual['from'])
        except: # quando der error de acesso no mapa => o caminho foi encontrado
            caminho.append(0) # adiciona ponto inicial
            break;

    return caminho[::-1] # retorna o inverso do caminho ( do inicio ao fim )

if __name__ == "__main__":
    main()
