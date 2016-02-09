ARNFileName = '/home/philomene/MFE/GTEx/v6/All_Tissue_Site_Details_Analysis.combined.rpkm11.gct'

geneList = []
ARNList = []

def extractGene(fileName):
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
    return

def extractARN(fileName):
    file = open(fileName, 'r')
    return

def cleanARNList(list):
    for element in list:
        if element[0:4] != 'GTEX': #pourquoi ne connait pas l'element Description???? (element juste avant ceux a garder
            print 'element: ' + element
            list.remove(element)
    return

def cleanGeneList(list):
    for element in list:
        if element[0:3] != 'ENS':
            list.remove(element)
    return

def main():
    extractGene(ARNFileName)
    print ARNList[0:15]
    print geneList[0:15]
    cleanGeneList(geneList)
    cleanARNList(ARNList)
    print ARNList[0:15]
    print geneList[0:15]
    cleanARNList(ARNList)
    print ARNList

    return

main()