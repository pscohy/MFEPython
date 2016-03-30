root = '/home/philomene/MFE/' #to modify according to the machine

GTExRoot = root + 'GTEx/v6/'

geneRoot = GTExRoot + 'geneRPKM/'
transcriptRoot = GTExRoot + 'transcriptRPKM/'

tablesRoot = GTExRoot + 'tables/'
phenotypeRoot = GTExRoot + 'subjectPhenotypes/'

disqueExterneRoot = '/media/philomene/SEAGATE/cours/MFE/'

geneRPKMFileName = geneRoot + 'All_Tissue_Site_Details_Analysis.combined.rpkm.gct'
geneRPKMFileNameTail = geneRoot + 'All_Tissue_Site_Details_Analysis.combined.rpkm-2.gct'
geneRPKMFileNameTest = geneRoot + 'All_Tissue_Site_Details_Analysis.combined.rpkm11.gct'

transcriptRPKMFileName = transcriptRoot + 'Flux_SetSummary_Merged.txt'
transcriptRPKMFileNameTest = transcriptRoot + 'Flux_SetSummary_Merged11.txt'

samplePhenotypeTableFileName = phenotypeRoot + 'GTEx_Data_V6_Annotations_SubjectPhenotypesDS.xlsx'
sampleTableFileName = tablesRoot + 'sampleTable.xlsx'
sampleTableFileNameTest = tablesRoot + 'sampleTableTest.csv'

geneTableFileName = tablesRoot + 'geneTable.csv'
geneTableFileNameTest = tablesRoot + 'geneTableTest.csv'

transcriptTableFileName = tablesRoot + 'transcriptTable.csv'
transcriptTableFileNameTest = tablesRoot + 'transcriptTableTest.csv'

geneRPKMTableFileName = tablesRoot + 'geneRPKMTable.csv'
geneRPKMTableFileNameTest = tablesRoot +'geneRPKMTableTest.csv'

transcriptRPKMTableFileName = tablesRoot + 'transcriptRPKMTable.csv'
transcriptRPKMTableFileNameTest = tablesRoot +'transcriptRPKMTableTest.csv'


transcriptRPKMTableFileNameExterne = disqueExterneRoot +'transcriptRPKMTableTest.csv'