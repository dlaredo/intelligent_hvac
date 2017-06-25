import math
import numpy
import matplotlib.pyplot as plt



def surfaceTemperatureClothingComputation(M, W, Icl, fcl, Tai, hc, Tcl):

	tolerance = 10**(-2)
	iterations = 0
	maxIterations = 100

	#Run until convergence or 1000 iterations are done
	while (TclCurrent - TclPrevious > tolerance or iterations < maxIterations):
		
		TclCurrent = 35.7 - 0.028 * (M - W) - Icl * ( 3.96 * 10**(-8) * fcl
			* ( math.pow(Tcl + 273, 4) - math.pow(Tr + 273, 4) )
			- fcl * hc * (TclPrevious - Tai) )

def convectiveHeatTransferCoefficientComputation(Va, Tcl, Tai):

	hc1 = 2.38 * math.pow(Tcl - Tai, 0.25)
	hc = 12.1 * math.sqrt(Va)

	if hc1 > hc:
		hc = hc1

	return hc

def ratioBodySurfaceAreaCoveredComputation(Icl):

	fcl = 0

	if Icl <= 0.0708:
		fcl = 1 + 1.129*Icl
	else:
		fcl = 1.05 + 0.645*Icl

	return fcl

def TclComputation():

	TclArray = numpy.linspace(22, 40, num=1000)
	Va = 0.1
	Tai = 22
	index = 0
	M = 70
	W = 0
	Icl = 1
	fcl = ratioBodySurfaceAreaCoveredComputation(Icl)
	Tr = 22
	gtArray = numpy.zeros(TclArray.shape)

	for Tcl in TclArray:
		hc = convectiveHeatTransferCoefficientComputation(Va, Tcl, Tai)
		gtArray[index] = Tcl - 35.7 - 0.028 * (M - W) - Icl * ( 3.96 * 10**(-8) * fcl
				* ( math.pow(Tcl + 273, 4) - math.pow(Tr + 273, 4) )
				- fcl * hc * (Tcl - Tai) )
		index += 1

	return TclArray, gtArray

	#print(gtArray)

def meanRadiantTemperatureComputation(Tg, Tai, Va, epsilon, diameter):

	temp = math.pow(Tg + 273, 4) + (1.10 * 10**8 * math.pow(Va, 0.6) * (Tg - Tai) )/(epsilon * pow(diameter, 0.4))

	Tr = math.pow(temp, 0.25) - 273

	return Tr

def waterVaporPressure(Hai, Tai):

	exponent = 16.6536 - 4030.183/(Tai + 235)
	Pa = 10 * Hai * math.exp(exponent)


def pmvComputation(Tai, Tg, Hai, Va, Icl, M):

	epsilon = 1
	diameter = 1
	#hc = 

	Pa = waterVaporPressure(Hai, Tai)
	fcl = ratioBodySurfaceAreaCoveredComputation(Icl)
	Tcl = surfaceTemperatureClothingComputation(M, W, Icl, fcl, Tai, hc, Tcl)
	Tr = meanRadiantTemperatureComputation(Tg, Tai, Va, epsilon, diameter)
	
	pmv = (0.303 * math.exp(-0.036*M) + 0.028) * ( (M - W) 
		- 3.05 * 10**(-3) * (5733 - 6.99 * (M - W) - Pa)
		- 0.42 * ( (M - W) - 58.15 ) - 1.7 * 10**(-5) * M * (5867 - Pa)
		- 0.0014 * M * (34 - Tai) - 3.96 * 10**(-8) * fcl 
		* ( math.pow(Tcl + 273, 4) - math.pow(Tr + 273, 4) )
		- fcl * hc * (Tcl - Tai) )

	return pmv

#Start of the main program
TclArray, gtArray = TclComputation()

plt.plot(TclArray, gtArray)

print(gtArray)

plt.show()
#plt.title('not equal, looks like ellipse', fontsize=10)


