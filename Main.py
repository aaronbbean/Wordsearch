from random import *

class ws():
  def __init__(self):
    self.board = []
    self.hiddenWords = [
        "test"
    ]
    self.HiddenWordNumber = []
    self.alph = ('abcdefghijklmnopqrxtuvwxyz')
    self.coninue = False
    self.boardSize = 0
    self.number = 0

  def horizontal(self, number, word):
    wordList = []
    lenths = self.boardSize - number
    horizontal = randrange(0, lenths)
    vertical = randrange(0, self.boardSize)
    horizontal -= 1
    for let in word:
      horizontal += 1
      wordList.append((vertical, horizontal, let))
    return wordList

  def Down(self, number, word):
    wordList = []
    lenths = self.boardSize - number

    horizontal = randrange(0, self.boardSize)
    vertical = randrange(0, lenths)

    vertical -= 1

    for let in word:
      vertical += 1
      wordList.append((vertical, horizontal, let))
    return wordList

  def diagonalLeft(self, number, word):
    wordList = []
    lenths = self.boardSize - number

    horizontal = randrange(number, self.boardSize)
    vertical = randrange(0, lenths)
    horizontal += 1
    vertical -= 1

    for let in word:
      vertical += 1
      horizontal -= 1

      wordList.append((vertical, horizontal, let))
    return wordList

  def diagonalRight(self, number, word):
    wordList = []
    lenths = self.boardSize - number

    horizontal = randrange(0, lenths)
    vertical = randrange(0, lenths)
    horizontal -= 1
    vertical -= 1
    for let in word:
      vertical += 1
      horizontal += 1
      wordList.append((vertical, horizontal, let))

    return wordList

  def Up(self, number, word):
    wordList = []
    lenths = self.boardSize - number

    horizontal = randrange(0, self.boardSize)
    vertical = randrange(0, lenths)

    vertical -= 1

    for let in word:
      vertical += 1
      wordList.append((vertical, horizontal, let))
    wordList.reverse()

    return wordList

  def MakeBoard(self, rownumber):
    self.boardSize = rownumber
    for h in range(rownumber):
      newRow = []

      for v in range(rownumber):

        BoardSquare = (h, v)
        newRow.append(BoardSquare)
      self.board.append(newRow)

  def BoardPlacment(self, word):
    number = len(word)
    choosinglist = [
        ws.Up(self, number, word),
        ws.Down(self, number, word),
        ws.diagonalRight(self, number, word),
        ws.diagonalLeft(self, number, word),
        ws.horizontal(self, number, word)
    ]
    NewWord = choice(choosinglist)
    self.HiddenWordNumber.append(NewWord)

  def PlaceWords(self):
    for words in self.hiddenWords:
      pass
    pass

  def wordCheck(self):

    checked = []
    TorF = 1
    for words in self.HiddenWordNumber:
      
      for row, colum, letter in words:

        for brow, bcolum, bletter in checked:

          if row == brow and colum == bcolum:

            if letter == bletter:
              
              pass
            else:
              TorF = 0

        checked.append((row, colum, letter))

    if TorF == 1:
      self.coninue = True
    else:
      del checked[:]
      del self.HiddenWordNumber[:]

  def placeLetters(self):

    for rows in self.board:
      for brow, bcolums in rows:
        for words in self.HiddenWordNumber:
          for row, colum, letter in words:
            letterss = letter.upper()
            if row == brow and colum == bcolums:
              self.board[brow][bcolums] = (row, colum, letterss)
    for rows in self.board:
      try:
        for brow, bcolums in rows:

          RanLetter = choice(self.alph)
          self.board[brow][bcolums] = (brow, bcolums, RanLetter)
      except:
        for testing in rows:
          if len(testing) == 2:
            r = testing[0]
            c = testing[1]
            RanLetter = choice(self.alph)
            self.board[r][c] = (r, c, RanLetter)

  def printBoard(self):
    news = 0
    answerfile = open("wordseachanswer.txt", "w")
    openfile = open("wordsearch.txt", "w")
    for enters in self.board:

      try:
        for r, c, l in enters:
          if news == self.boardSize:
            openfile.write("\n")
            answerfile.write("\n")
            news = 0
          w = l.upper()
          openfile.write(w)
          answerfile.write(l)
          openfile.write(' ')
          answerfile.write(' ')
          news += 1
      except:
        print(enters)
        pass

    openfile.write("\n \n")

    for writing in self.hiddenWords:
      word = writing.capitalize()
      openfile.write(word)
     
      openfile.write("\n")
    openfile.close()
    answerfile.close()
  def GameSetUp(self):
    while self.coninue == False:
      for words in self.hiddenWords:
        self.BoardPlacment(words)
      self.wordCheck()
game = ws()
game.MakeBoard(16)
game.GameSetUp()
game.placeLetters()
game.printBoard()


