#########################
#
#  Chess Player AI
#  CPSC 481
#
#  Christopher Rodney
#  Daniel Henderson
#  Long Nguyen
#  Erik Davis
#
#########################

import sys

#Use enumerations to make code more readable.  (In Python, we'll use a simple class)  
#Enums map a an english word to an int (or index)
#They can be specified either with the word OR directly with the int value

class chessPieceEnum:
	King = 1
	Rook = 2
	Knight = 3

class spotEnum:
	a = 1
	b = 2
	c = 3
	d = 4
	e = 5
	f = 6
	g = 7
	h = 8
	
class playerEnum:
	X = 1
	Y = 2

#Create a simple class to hold information about each piece on the board
class chessPieces:
	def __init__ (self):
		self.player = playerEnum.X
		self.piece = chessPieceEnum.King
		self.x = 1
		self.y = spotEnum.a
		self.inPlay = True

#The board state is a python list of all pieces
boardState = []

def setupBoard():
#setup initial state of the board.
	#add five pieces to the board
	for i in xrange (0, 5) :
		newPiece = chessPieces()
		boardState.append (newPiece)
	
	#define the pieces
	#Player X King at e1
	boardState[0].y = spotEnum.e
	
	#Player X Rook at a1
	boardState[1].piece = chessPieceEnum.Rook
	
	#PlayerX Knight at g1
	boardState[2].piece = chessPieceEnum.Knight
	boardState[2].y = spotEnum.g
	
	#PlayerY King at e8
	boardState[3].player = playerEnum.Y
	boardState[3].y = spotEnum.e
	boardState[3].x = 8
	
	#PlayerY Knight at b8
	boardState[4].player = playerEnum.Y
	boardState[4].piece = chessPieceEnum.Knight
	boardState[4].y = spotEnum.b
	boardState[4].x = 8
	
def printPiece( piece, player ):
	#Print a chess piece out.  Call this function when printing of the board is at the right
	#location.  Player X = white and Player Y = black
	if piece == chessPieceEnum.Knight and player == playerEnum.X :
		return u'\u265E' + ' '
	if piece == chessPieceEnum.King and player == playerEnum.X :
		return u'\u265A' + ' '
	if piece == chessPieceEnum.Rook and player == playerEnum.X :
		return u'\u265C' + ' '
	if piece == chessPieceEnum.King and player == playerEnum.Y :
		return u'\u2654' + ' '
	if piece == chessPieceEnum.Knight and player == playerEnum.Y :
		return u'\u2658' + ' '


def play( n ):
	a = 1
	
def move():
	a = 1
	
def heuristicX():
	a = 1
	
def heuristicY():
	a = 1
	
def showMove():
	print '\n'
	for x in range (8, 0, -1) :
		print x,
		print "  ",
		Output = ""
		for y in xrange (1, 9) :
			Match = False
			for z in xrange (0, 5) :
				#If a chess piece is at this location, print it.
				if boardState[z].x == x and boardState[z].y == y and boardState[z].inPlay == True :
					Match = True
					Output += printPiece ( boardState[z].piece, boardState[z].player )
			if Match == False :
				#Otherwise print a space character instead
				#Use XOR logic to generate a chess board
				if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0) :
					#print black square
					Output += u'\u2593' + u'\u2593'   #25FC
				else :
					#print white square
					Output += u'\u2591' + u'\u2591'  #25FB
		print Output
	print "     a b c d e f g h"

#  MAIN

setupBoard()
showMove()
