import string
import random

def encodeLetter(letterPlainText, letterKey):
  
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  
  numPlainText = alphabet.index(letterPlainText) + 1
  numKey = alphabet.index(letterKey) + 1

  numCypherText = (numPlainText + numKey) % 26
  letterCypherText = alphabet[numCypherText]
  return letterCypherText


def decodeLetter(letterCypherText, letterKey):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  
  numCypherText = alphabet.index(letterCypherText) + 1
  numKey = alphabet.index(letterKey) + 1

  numPlainText = numCypherText - numKey
  letterPlainText = alphabet[numPlainText]
  return letterPlainText

def decrypt(cypherText, key):
  plainText = ''
  
  for i in range(len(cypherText)):
    plainText += decodeLetter(cypherText[i], key[i])
  
  return plainText

def encrypt(plainText, key):
  cypherText = ''
  
  for i in range(len(plainText)):
    cypherText += encodeLetter(plainText[i], key[i])
  
  return cypherText

def generateKey(keyLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(keyLength))

while (True):
  
  print("Menu:")
  print("1 - Encrypt")
  print("2 - Decrypt")
  print("3 - Quit")
  selected = input()

  if (selected == '1'):

    print("Type the Plain Text:")
    plainText = input()
    key = generateKey(len(plainText))
    print('Cypher Text:', encrypt(plainText, key))

  elif (selected == '2'):

    print("Type the Cypher Text:")
    cypherText = input()
    key = generateKey(len(cypherText))
    print('Plain Text:', decrypt(cypherText, key))

  elif (selected == '3'):
    break

  else:
    print("Only 1/2/3 options avaible") 
