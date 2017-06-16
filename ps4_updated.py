# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
def helper(viruses, maxPop, rangenum, numTrials):
    totalsize = []
    for i in range(numTrials):
        treatedpatient = TreatedPatient(viruses, maxPop)
        for j in range(rangenum):
            treatedpatient.update()
        treatedpatient.addPrescription('guttagonol')
        for k in range(150):
            treatedpatient.update()
        totalsize.append(treatedpatient.getTotalPop())
    return totalsize
   
def simulationDelayedTreatment(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    viruses = []
    for j in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    totalsize = []
    rangenum = [300, 150, 75, 0]
    for n in rangenum:
        totalsize.append(helper(viruses, maxPop, n, numTrials))     
    fig = pylab.figure()
    f1 = fig.add_subplot(221)
    f2 = fig.add_subplot(222)
    f3 = fig.add_subplot(223)
    f4 = fig.add_subplot(224)
    f1.hist(totalsize[0],10)
    f2.hist(totalsize[1],10)
    f3.hist(totalsize[2],10)
    f4.hist(totalsize[3],10)
    pylab.show()
    
#simulationDelayedTreatment(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 10)


def guttagonol(viruses, maxPop, rangenum, numTrials):
    totalsize = []
    for i in range(numTrials):
        treatedpatient = TreatedPatient(viruses, maxPop)
        for n in range(150):
            treatedpatient.update()
        treatedpatient.addPrescription('guttagonol')
        for j in range(rangenum):
            treatedpatient.update()
        treatedpatient.addPrescription('grimpex')
        for k in range(150):
            treatedpatient.update()
        totalsize.append(treatedpatient.getTotalPop())
    return totalsize

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    viruses = []
    for j in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    totalsize = []
    rangenum = [300, 150, 75, 0]
    for n in rangenum:
        totalsize.append(guttagonol(viruses, maxPop, n, numTrials))     
    fig = pylab.figure()
    f1 = fig.add_subplot(221)
    f2 = fig.add_subplot(222)
    f3 = fig.add_subplot(223)
    f4 = fig.add_subplot(224)
    f1.hist(totalsize[0],10)
    f2.hist(totalsize[1],10)
    f3.hist(totalsize[2],10)
    f4.hist(totalsize[3],10)
    pylab.show()
    
simulationTwoDrugsDelayedTreatment(100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005, 100)
