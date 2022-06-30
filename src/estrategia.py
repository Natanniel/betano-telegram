VERMELHOS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
PRETOS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
NUMEROS_IMPARES = [1, 3, 5, 7, 9, 11, 13, 15,
                   17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
NUMEROS_PARES = [2, 4, 6, 8, 10, 12, 14, 16,
                 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
NUMEROS_ALTOS = [19, 20, 21, 22, 23, 24, 25,
                 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
NUMEROS_BAIXOS = [1, 2, 3, 4, 5, 6, 7, 8,
                  9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
DUZIA_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
DUZIA_2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
DUZIA_3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
COLUNA_1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
COLUNA_2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
COLUNA_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]


def VerificarRepeticao(repeticao, numero):

    match repeticao:
        case 'r-v':
            return VERMELHOS.__contains__(int(numero))
        case 'r-p':
            return PRETOS.__contains__(int(numero))
        case 'r-np':
            return NUMEROS_PARES.__contains__(int(numero))
        case 'r-ni':
            return NUMEROS_IMPARES.__contains__(int(numero))
        case 'r-na':
            return NUMEROS_ALTOS.__contains__(int(numero))
        case 'r-nb':
            return NUMEROS_BAIXOS.__contains__(int(numero))
        case 'r-d1':
            return DUZIA_1.__contains__(int(numero))
        case 'r-d2':
            return DUZIA_2.__contains__(int(numero))
        case 'r-d3':
            return DUZIA_3.__contains__(int(numero))
        case 'r-c1':
            return COLUNA_1.__contains__(int(numero))
        case 'r-c2':
            return COLUNA_2.__contains__(int(numero))
        case 'r-c3':
            return COLUNA_3.__contains__(int(numero))


def repeticaoVermelho(bolas, estrategias):

    resultado = []
    encontrou = False

    # Verifica todas estrategias
    for estrategia in estrategias:

        # Verifica se alguma estrategia ja foi encontrada
        if encontrou == False:

            # Pega a estrategia
            repeticao = estrategia['estrategia']

            contador = 0  # Contagem de repeticoes
            # Caso precise parar a contagem da sequencia esse indicador muda para cancelar a estrategia
            pararContagem = False

            # Contar sequencia
            for bola in bolas:

                if pararContagem == False:

                    if VerificarRepeticao(repeticao, bola['numero']):
                        contador = contador + 1

                        if estrategia['analise'] == contador:
                            pararContagem = True
                            encontrou = True
                            resultado.append(estrategia)

                    else:
                        pararContagem = True

    return resultado


def VerificarApostarNo(analisa, aposta, numero, jogadaConfirmada):

    if jogadaConfirmada == 0:

        match analisa:
            case 'r-v':
                return VERMELHOS.__contains__(int(numero))
            case 'r-p':
                return PRETOS.__contains__(int(numero))
            case 'r-np':
                return NUMEROS_PARES.__contains__(int(numero))
            case 'r-ni':
                return NUMEROS_IMPARES.__contains__(int(numero))
            case 'r-na':
                return NUMEROS_ALTOS.__contains__(int(numero))
            case 'r-nb':
                return NUMEROS_BAIXOS.__contains__(int(numero))
            case 'r-d1':
                return DUZIA_1.__contains__(int(numero))
            case 'r-d2':
                return DUZIA_2.__contains__(int(numero))
            case 'r-d3':
                return DUZIA_3.__contains__(int(numero))
            case 'r-c1':
                return COLUNA_1.__contains__(int(numero))
            case 'r-c2':
                return COLUNA_2.__contains__(int(numero))
            case 'r-c3':
                return COLUNA_3.__contains__(int(numero))

    else:
        match aposta:
            case 'a-v':
                return VERMELHOS.__contains__(int(numero))
            case 'a-p':
                return PRETOS.__contains__(int(numero))
            case 'a-np':
                return NUMEROS_PARES.__contains__(int(numero))
            case 'a-ni':
                return NUMEROS_IMPARES.__contains__(int(numero))
            case 'a-na':
                return NUMEROS_ALTOS.__contains__(int(numero))
            case 'a-nb':
                return NUMEROS_BAIXOS.__contains__(int(numero))
            case 'a-d1':
                return DUZIA_1.__contains__(int(numero))
            case 'a-d2':
                return DUZIA_2.__contains__(int(numero))
            case 'a-d3':
                return DUZIA_3.__contains__(int(numero))
            case 'a-d1d2':
                win = DUZIA_1.__contains__(int(numero))
                if win == False:
                    win = DUZIA_2.__contains__(int(numero))
                return win

            case 'a-d2d3':
                win = DUZIA_2.__contains__(int(numero))
                if win == False:
                    win = DUZIA_3.__contains__(int(numero))
                return win
            
            case 'a-d1d3':
                win = DUZIA_1.__contains__(int(numero))
                if win == False:
                    win = DUZIA_3.__contains__(int(numero))
                return win
            

            case 'a-c1':
                return COLUNA_1.__contains__(int(numero))
            case 'a-c2':
                return COLUNA_2.__contains__(int(numero))
            case 'a-c3':
                return COLUNA_3.__contains__(int(numero))
          
            case 'a-c1c2':
                win = COLUNA_1.__contains__(int(numero))
                if win == False:
                    win = COLUNA_2.__contains__(int(numero))
                return win

            case 'a-c2c3':
                win = COLUNA_2.__contains__(int(numero))
                if win == False:
                    win = COLUNA_3.__contains__(int(numero))
                return win
            
            case 'a-c1c3':
                win = COLUNA_1.__contains__(int(numero))
                if win == False:
                    win = COLUNA_3.__contains__(int(numero))
                return win


def analisaConfirmacao(estrategia, sinais):
    # Referencia global
    # 0 - ChatID  1 - MessageID  2 - Sinal  3 - Roleta
    # 4 - Gale 5 - confirma 6 - Entrada confirmada
    green = False
    entradaConfirmada = False
    apagarMensagem = False
    pararContagem = False
    contador = 0
    emMartinGale = False
    valorGale = 0
    if(estrategia[7] == 1):
        emMartinGale = True

    apostarNo = estrategia[6]

#     ACHO QUE ESSA LINHA NAO
 #   # Repeticao vermelho ==================================================================
#    if estrategia[2] == 'r-v':

    for bola in sinais:

        if pararContagem == False:

            # Verifica se o numero que caiu e o mesmo que deve apostar
            if VerificarApostarNo(estrategia[2], apostarNo, bola['numero'], estrategia[7]):
                contador = contador + 1

                if estrategia[5] == contador and emMartinGale == False:
                    pararContagem = True
                    entradaConfirmada = True

                if emMartinGale == True:
                    green = True
                    pararContagem = True

            else:
                # o valor encontrado nao e o esperado
                if(contador == 0):
                    # ja foi dado entrada e a operacao esta em gale ?
                    if(emMartinGale):
                        # o valor de gale atual tem que ser menor que 3
                        valorGale = valorGale + 1
                        if(valorGale == 3):
                            # LOSS
                            apagarMensagem = True
                            pararContagem = True
                    else:
                        # Cancelar analise do sinal
                        apagarMensagem = True
                        pararContagem = True

    return entradaConfirmada, apagarMensagem, green
