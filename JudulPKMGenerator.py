#import req lib
from __future__ import division
import random
import os
#clear screen
clear = lambda: os.system('cls')
#read wordlist KBBI
f = open('00-indonesian-wordlist.txt','r')
f1 = f.readlines()
wordlist = []
for x in f1:
    x = x.replace('\n','')
    wordlist.append(x)
#replace
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])
#find Word
def orderedSampleWithoutReplacement(seq, sampleSize):
    word = []
    totalElems = len(seq)
    if not 0<=sampleSize<=totalElems:
        raise ValueError('Required that 0 <= sample_size <= population_size')

    picksRemaining = sampleSize
    for elemsSeen,element in enumerate(seq):
        elemsRemaining = totalElems - elemsSeen
        prob = picksRemaining/elemsRemaining
        if random.random() < prob:
            if(element != ' '):
                word.append(element)
                seq = replace_str_index(seq,elemsSeen,seq[elemsSeen].upper())
                picksRemaining -= 1
    return ''.join(word), seq
#Input Judul
clear()
title = input('Judul PKM : ').lower()
udah = False
history = []
while not udah :
	clear()
	print('judul yang mungkin adalah :')
	print('')
	while True:
		l = list(orderedSampleWithoutReplacement(title,5))
		if (l[0] in wordlist) and (l[0] not in history):
			break
	print(l[0].upper(),' : ',l[1])
	while True:
		print('')
		cek = input('Setuju? [y/n] : ')
		if(cek == 'y' or cek == 'Y' or cek == 'n' or cek == 'N'):
			break
	if cek == 'y' or cek == 'Y':
		udah = True
	else :
		history.append(l[0])
clear()
print('')
print(l[0].upper(),' : ',l[1])
print('history :')
for x in history :
	print(x[0].upper(),' : ',x[1])