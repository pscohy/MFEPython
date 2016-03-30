from xlrd import *
from xlwt import *
from xlutils.copy import *
import time
import numpy as np
import csv

import xlsxwriter as xlwriter

import openpyxl

#path
rootpath = '/home/philomene/MFE/Data/'

referencePath = rootpath + 'dataJV/'

T2DDataPath = '/home/philomene/MFE/Data/T2D/'

#references
geneReferenceT2D = referencePath + 'ctl_T2D_gene_RPKM_values.xlsx'
isoformReferenceT2D = referencePath + 'ctl_T2D_isoforms_RPKM_values.xlsx'


#to be modified
genesDownT2D = T2DDataPath + 'genes-down-001.xlsx'
genesUpT2D = T2DDataPath + 'genes-up-001.xlsx'

isoformDownT2D = T2DDataPath + 'isoforms-down-001.xls'
isoformUpT2D = T2DDataPath + 'isoforms-up-001.xls'



def fonction(referenceFile, completeFile):
    referenceTable = open_workbook(referenceFile)
    completeTable = open_workbook(completeFile)

    completeTableCopy = copy(completeTable)


    geneList =[]

    for row in completeTable.sheet_by_index(0)._cell_values:
        geneList.append('\'' + row[0])

    i = 0

    for row in referenceTable.sheet_by_index(0)._cell_values:
        print i
        if (i < len(geneList)):
            if (row[3] == geneList[i]):
                completeTableCopy.get_sheet(0).write(i,1,row[6])
                i+=1

    completeTableCopy.save(completeFile)
    return



def main():

    # fonction(isoformReferenceT2D, isoformDownT2D)

    fonction(isoformReferenceT2D, isoformUpT2D)

    #attention, il faut changer les row de la reference entre isoforme et gene

    #fonction(geneReferenceT2D, genesDownT2D)
    # fonction(geneReferenceT2D, genesUpT2D)
    return

main()