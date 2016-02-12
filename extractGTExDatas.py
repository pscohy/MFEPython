from xlrd import *
from xlwt import *
from xlutils.copy import *
import time

root = '/home/philomene/MFE/'

GTExRoot = root + 'GTEx/v6/'

geneRoot = GTExRoot + 'geneRPKM/'
transcriptRoot = GTExRoot + 'transcriptRPKM/'

tablesRoot = GTExRoot + 'tables/'
phenotypeRoot = GTExRoot + 'subjectPhenotypes/'

geneRPKMFileName = geneRoot + 'All_Tissue_Site_Details_Analysis.combined.rpkm.gct'
geneRPKMFileNameTest = geneRoot + 'All_Tissue_Site_Details_Analysis.combined.rpkm11.gct'
transcriptRPKMFileName = transcriptRoot + 'Flux_SetSummary_Merged.txt'

ARNPhenotypeTableFileName = phenotypeRoot + 'GTEx_Data_V6_Annotations_SubjectPhenotypesDS.xlsx'
ARNTableFileName = tablesRoot + 'ARNTable.xlsx'
ARNTableFileNameTest = tablesRoot + 'ARNTableTest.xlsx'

geneTableFileName = tablesRoot + 'geneTable.xlsx'
geneTableFileNameTest = tablesRoot + 'geneTableTest.xlsx'



def extractGene(fileName):
    geneNameList = []
    geneDescriptionList = []
    ARNList = []
    i = 0
    file = open(fileName,'r')
    for line in file:
        print i
        element = ''
        j = 0
        for c in line:
            element += c
            if i == 2:
                if c == '	':
                    ARNList.append(element)
                    element = ''
            else:
                if c == '	':
                    if j==0:
                        geneNameList.append(element)
                    else:
                        geneDescriptionList.append(element)
                        break
                    element = ''
                    j+=1
        i += 1
    return ARNList, geneNameList, geneDescriptionList

def cleanList(list, listType):
    comparison = False
    for element in list:
        if listType == 'gene':
            comparison = element[0:4] != 'GTEX'
        elif listType == 'ARN':
            comparison = element[0:4] != 'ENSG'
        if comparison: #pourquoi ne connait pas l'element Description???? (element juste avant ceux a garder
            list.remove(element)
    return

def writeARNTable():
    ARNTable = open_workbook(ARNTableFileName)
    ARNPhenotypeTable = open_workbook(ARNPhenotypeTableFileName)

    ARNTableCopy = copy(ARNTable)

    subjIDPhenList =[]
    phenTitleList = []

    firstTime = True
    for element in ARNPhenotypeTable.sheet_by_index(0)._cell_values:
        if firstTime:
            phenTitleList = element
            firstTime = False
        subjIDPhen = element [0]
        subjIDPhenList.append(subjIDPhen)

    ARNTableCopy.get_sheet(0).write(0,61,phenTitleList[0])
    ARNTableCopy.get_sheet(0).write(0,62,phenTitleList[1])
    ARNTableCopy.get_sheet(0).write(0,63,phenTitleList[2])
    ARNTableCopy.get_sheet(0).write(0,64,phenTitleList[3])

    j=0
    for element in ARNTable.sheet_by_index(0)._cell_values:
        i=0
        subjIDGen = ''
        for c in element[0]:
            subjIDGen += c
            if c == '-':
                i+=1
                if i == 2:
                    subjIDGen = subjIDGen[:-1]
                    try:
                        row = ARNPhenotypeTable.sheet_by_index(0)._cell_values[subjIDPhenList.index(subjIDGen)]
                    except ValueError:
                        print 'SUBJID : ', subjIDGen, ' not find in the phenotype table'
                    ARNTableCopy.get_sheet(0).write(j,61,row[0])
                    ARNTableCopy.get_sheet(0).write(j,62,row[1])
                    ARNTableCopy.get_sheet(0).write(j,63,row[2])
                    ARNTableCopy.get_sheet(0).write(j,64,row[3])
                    break
        j+=1

    ARNTableCopy.save(ARNTableFileName)
    return

def writeGeneTable(nameList, descriptionList):
    geneTable = open_workbook(geneTableFileName)
    geneTableCopy = copy(geneTable)

    i=0
    while (i < len(nameList)):
        print i
        geneTableCopy.get_sheet(0).write(i+1, 0, nameList[i])
        geneTableCopy.get_sheet(0).write(i+1, 1, descriptionList[i])
        i+=1
    geneTableCopy.save(geneTableFileNameTest)

def main():
    startTime = time.time()

    ARNList, geneNameList, geneDescriptionList = extractGene(geneRPKMFileName)
    geneNameList = geneNameList[1:]
    cleanList(ARNList, 'ARN')
    cleanList(ARNList, 'ARN')
    writeGeneTable(geneNameList,geneDescriptionList)

    #print 'ARNList: ', ARNList, ' length: ', len(ARNList)
    #print 'nameList: ', geneNameList, ' length: ', len(geneNameList)
    #print 'descriptionList', geneDescriptionList, 'length: ', len(geneDescriptionList)

    #writeARNTable()

    endTime = time.time()-startTime
    print 'endTime : ', endTime
    return

main()