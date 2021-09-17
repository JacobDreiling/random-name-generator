import random

letterFreq= [8.04,9.52,12.86,16.68,29.17,31.57,33.44,38.49,46.06,46.22,46.76,50.83,53.34,60.57,68.21,70.35,70.47,76.75,83.26,92.54,95.27,96.32,98.00,98.23,99.89,100.00]

scrWidth= 42

#A good one: Eastrvom Ltloeihtas

def nameGen(count,names,initial):
	for i in range(count):
		wholeName= ''
		j= names
		while j>0:
			partName= ''
			letters= round(random.gauss(5,2))
			if letters>2:
				for l in range(letters):
					p= random.uniform(0,100)
					k= 0
					while p>letterFreq[k]:
						k+= 1
					partName+= chr(97+k)
				wholeName+= partName.capitalize()+' '
				j-= 1
		if initial:
			p= random.uniform(0,100)
			k= 0
			while p>letterFreq[k]:
				k+= 1
			print((wholeName[:wholeName.index(' ')+1]+chr(65+k)+'. '+wholeName[wholeName.index(' ')+1:]).center(42)+'\n')
		else:
			print(wholeName[:-1].center(42)+'\n')

nameGen(20,2,False)
