RED_NUMBERS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
BLACK_NUMBERS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
ODD_NUMBERS = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
EVEN_NUMBERS = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
HIGH_NUMBERS = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
LOW_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
DOZEN_01_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
DOZEN_02_NUMBERS = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
DOZEN_03_NUMBERS = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
COLUMN_01_NUMBERS = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
COLUMN_02_NUMBERS = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
COLUMN_03_NUMBERS = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]


estrategias = ['vermelho', 'preto', 'impar', 'par', 'alto', 'baixo', 'duzia-01', 'duzia-02', 'duzia-03', 'coluna-01', 'coluna-02', 'coluna-03']



def encontrarEstrategia(bola, estrategias):

        if bola in RED_NUMBERS:
            estrategias[0] += 1
       
        if bola in BLACK_NUMBERS:
            estrategias[1] += 1

     #   if (ODD_NUMBERS.contains(ball)) {
     #       strategies.add(RouletteStrategy.ODD_BALL)
     #   } else if (EVEN_NUMBERS.contains(ball)) {
     #       strategies.add(RouletteStrategy.EVEN_BALL)
     #   }

      #  if (HIGH_NUMBERS.contains(ball)) {
      #      strategies.add(RouletteStrategy.HIGH_BALL)
      #  } else if (LOW_NUMBERS.contains(ball)) {
      #      strategies.add(RouletteStrategy.LOW_BALL)
      #  }

     #   if (DOZEN_01_NUMBERS.contains(ball)) {
     #       strategies.add(RouletteStrategy.DOZEN_01_BALL)
     #   } else if (DOZEN_02_NUMBERS.contains(ball)) {
     #       strategies.add(RouletteStrategy.DOZEN_02_BALL)
     #   } else if (DOZEN_03_NUMBERS.contains(ball)) {
     #       strategies.add(RouletteStrategy.DOZEN_03_BALL)
     #   }

 #       if (COLUMN_01_NUMBERS.contains(ball)) {
#            strategies.add(RouletteStrategy.COLUMN_01_BALL)
 #       } else if (COLUMN_02_NUMBERS.contains(ball)) {
  #          strategies.add(RouletteStrategy.COLUMN_02_BALL)
   #     } else if (COLUMN_03_NUMBERS.contains(ball)) {
    #        strategies.add(RouletteStrategy.COLUMN_03_BALL)
    #    }

        return estrategias
    