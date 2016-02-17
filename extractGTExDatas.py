from xlrd import *
from xlwt import *
from xlutils.copy import *
import time
import numpy as np

root = '/home/philomene/MFE/'

GTExRoot = root + 'GTEx/v6/'

geneRoot = GTExRoot + 'geneRPKM/'
transcriptRoot = GTExRoot + 'transcriptRPKM/'

tablesRoot = GTExRoot + 'tables/'
phenotypeRoot = GTExRoot + 'subjectPhenotypes/'

geneRPKMFileName = geneRoot + 'All_Tissue_Site_Details_Analysis.combined.rpkm.gct'
geneRPKMFileNameTest = geneRoot + 'All_Tissue_Site_Details_Analysis.combined.rpkm11.gct'

transcriptRPKMFileName = transcriptRoot + 'Flux_SetSummary_Merged.txt'
transcriptRPKMFileNameTest = transcriptRoot + 'Flux_SetSummary_Merged11.txt'

ARNPhenotypeTableFileName = phenotypeRoot + 'GTEx_Data_V6_Annotations_SubjectPhenotypesDS.xlsx'
ARNTableFileName = tablesRoot + 'ARNTable.xlsx'
ARNTableFileNameTest = tablesRoot + 'ARNTableTest.xlsx'

geneTableFileName = tablesRoot + 'geneTable.xlsx'
geneTableFileNameTest = tablesRoot + 'geneTableTest.xlsx'

transcriptTableFileName = tablesRoot + 'transcriptTable.xlsx'
transcriptTableFileNameTest = tablesRoot + 'transcriptTableTest.xlsx'


transcriptTableFileName = tablesRoot + 'transcriptTable.xlsx'
transcriptTableFileNameTest = tablesRoot + 'transcriptTableTest.xlsx'



def extractGene(fileName):
    '''Extract SAMPID and GeneID'''
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

def extractTranscript(fileName):
    '''extract TranscriptID and chromosome and coord of Gene'''
    geneSymbolList = []
    chromosomesList = []
    coordList = []

    i = 0

    file = open(fileName, 'r')
    for line in file:
        print i
        element = ''
        j = 0
        for c in line:
            element+=c
            if c == '	':
                if j == 1:
                    geneSymbolList.append (element)
                elif j == 2:
                    chromosomesList.append (element)
                elif j == 3:
                    coordList.append(element)
                    break
                element =''
                j+=1
        i+=1
    return geneSymbolList, chromosomesList, coordList

def cleanList(list, listType):
    '''delete elements of list which not correspond to the type of the list'''
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
    '''write table (excel) containing ARN informations'''
    ARNTable = open_workbook(ARNTableFileName)
    ARNPhenotypeTable = open_workbook(ARNPhenotypeTableFileName)

    ARNTableCopy = copy(ARNTable)

    subjIDPhenList =[]
    phenTitleList = []

    firstTime = True
    for row in ARNPhenotypeTable.sheet_by_index(0)._cell_values:
        if firstTime:
            phenTitleList = row
            firstTime = False
        subjIDPhen = row [0]
        subjIDPhenList.append(subjIDPhen)

    ARNTableCopy.get_sheet(0).write(0,61,phenTitleList[0])
    ARNTableCopy.get_sheet(0).write(0,62,phenTitleList[1])
    ARNTableCopy.get_sheet(0).write(0,63,phenTitleList[2])
    ARNTableCopy.get_sheet(0).write(0,64,phenTitleList[3])

    j=0
    for row in ARNTable.sheet_by_index(0)._cell_values:
        i=0
        subjIDGen = ''
        for c in row[0]:
            subjIDGen += c
            if c == '-':
                i+=1
                if i == 2:
                    subjIDGen = subjIDGen[:-1]
                    try:
                        rowContent = ARNPhenotypeTable.sheet_by_index(0)._cell_values[subjIDPhenList.index(subjIDGen)]
                    except ValueError:
                        print 'SUBJID : ', subjIDGen, ' not find in the phenotype table'
                    ARNTableCopy.get_sheet(0).write(j,61,rowContent[0])
                    ARNTableCopy.get_sheet(0).write(j,62,rowContent[1])
                    ARNTableCopy.get_sheet(0).write(j,63,rowContent[2])
                    ARNTableCopy.get_sheet(0).write(j,64,rowContent[3])
                    break
        j+=1

    ARNTableCopy.save(ARNTableFileName)
    return

def writeGeneTable(nameList, descriptionList):
    '''write table (excel) which contain Gene informations'''
    geneTable = open_workbook(geneTableFileName)
    geneTableCopy = copy(geneTable)

    i=0
    while (i < len(nameList)):
        print i
        geneTableCopy.get_sheet(0).write(i+1, 0, nameList[i])
        geneTableCopy.get_sheet(0).write(i+1, 1, descriptionList[i])
        i+=1
    geneTableCopy.save(geneTableFileNameTest)

    return

def updateGeneTable(geneList, chrList, coordList):
    '''add information in the Gene table'''
    geneTable = open_workbook(geneTableFileName)
    geneTableCopy = copy(geneTable)

    rowIndex = 0
    for row in geneTable.sheet_by_index(0)._cell_values:
        print rowIndex
        try:
            # print row[0]
            listIndex = geneList.index(row[0])
            # print listIndex
            geneTableCopy.get_sheet(0).write(rowIndex, 2, chrList[listIndex])
            geneTableCopy.get_sheet(0).write(rowIndex, 3, coordList[listIndex])
        except ValueError:
            print 'GeneSymbol: ', row[0], ' not find in the gene table'

        rowIndex +=1

    geneTableCopy.save(geneTableFileNameTest)

    return

def writeTranscriptTable():
    transcriptTable = open_workbook(transcriptTableFileName)
    transcriptRPKMTable = open_workbook(transcriptRPKMFileNameTest)

    transcriptTableCopy = copy(transcriptTable)

    rowIndex = 0
    for row in transcriptRPKMTable.sheet_by_index(0)._cell_values:
        print rowIndex
        transcriptTableCopy.get_sheet(0).write(rowIndex, 0, row[0])
        transcriptTableCopy.get_sheet(0).write(rowIndex, 1, row[1])

        rowIndex +=1


    transcriptTableCopy.save(transcriptRPKMFileNameTest)
    return

def removeLast(string):
    return string[:-1]


def main():
    '''main function'''
    startTime = time.time()

    writeTranscriptTable()


    endTime = time.time()-startTime
    print 'endTime : ', endTime
    return

def processARNTable():
    writeARNTable()
    return

def processGeneTable():
    #make table
    ARNList, geneNameList, geneDescriptionList = extractGene(geneRPKMFileName)
    geneNameList = geneNameList[1:]
    cleanList(ARNList, 'ARN')
    cleanList(ARNList, 'ARN')
    writeGeneTable(geneNameList,geneDescriptionList)

    print 'ARNList: ', ARNList, ' length: ', len(ARNList)
    print 'nameList: ', geneNameList, ' length: ', len(geneNameList)
    print 'descriptionList', geneDescriptionList, 'length: ', len(geneDescriptionList)

    #update table

    gene, chr, coord = extractTranscript(transcriptRPKMFileName)


    gene = gene[1:]
    chr = chr[1:]
    coord = coord[1:]

    gene = map(removeLast, gene)

    # print 'gene : ', gene
    # print 'chr : ', chr
    # print 'coord : ', coord

    updateGeneTable(gene, chr, coord)

    return

def processTranscriptTable():
    writeTranscriptTable()
    return

main()