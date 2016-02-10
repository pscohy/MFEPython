from pandas import *
from time import *

root = '/home/philomene/MFE/'
GTExRoot = root + 'GTEx/v6/'
dataBaseRoot = root + 'dataBase/'

ARNFileName = GTExRoot + 'All_Tissue_Site_Details_Analysis.combined.rpkm11.gct'
transcriptFileName = GTExRoot + 'Flux_SetSummary_Merged.txt'

ARNTableFileName =dataBaseRoot + 'ARNTable.csv'


def extractGene(fileName):
    geneList = []
    ARNList = []
    i = 0
    file = open(fileName,'r')
    for line in file:
        print i
        element = ''
        for c in line:
            element += c
            if i == 2:
                if c == '	':
                    ARNList.append(element)
                    element = ''
            else:
                if c == '	':
                    geneList.append(element)
                    break
        i += 1
    return ARNList, geneList

def cleanList(list, listType):
    comparison = False
    for element in list:
        if listType == 'gene':
            comparison = element[0:4] != 'GTEX'
        elif listType == 'ARN':
            comparison = element[0:3] != 'ENS'
        if comparison: #pourquoi ne connait pas l'element Description???? (element juste avant ceux a garder
            list.remove(element)
    return

def cleanGeneList(list):
    for element in list:
        if element[0:3] != 'ENS':
            list.remove(element)
    return

def writeARNTable(list):
    ARNTable = pandas.read_csv(ARNTableFileName)

def main():
    startTime = time()

    ARNList, geneList = extractGene(ARNFileName)
    cleanList(geneList, 'gene')
    cleanList(ARNList, 'ARN')
    cleanList(ARNList, 'ARN')

    print 'ARNList: ', ARNList
    print 'geneList: ', geneList

    endTime = time()-startTime
    print 'endTime : ', endTime
    return

main()