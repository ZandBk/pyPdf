####################################################################################################
# Author: Zand Bakhtiari 
# Date: August 8, 2016
#
# Purpose:
#
###################################################################################################
#import you modules
# modules needed include os, time, dfFileWriter, PdfFileReader
import glob, time
from pyPdf import PdfFileWriter, PdfFileReader

#tell the user that the script has sratred and the time it started. 
print "Script Initiated...\n", time.ctime(),"\n"

# Creates a list (called here 'path') on the given directory
# Uses a wildecard \*.pdfto return a list of .pdf files only
path = glob.glob(r"G:\pworks\assetmanagement\GISZBakhtiari\Map_Requests\StreetSweepingAreas\*.pdf")

# Prints the list created above
print path

# Creating a routine that appends files to the output file
def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

# Creating an object where pdf pages are appended to
output = PdfFileWriter()

# Iterates through the list and appends the pdf-pages from different files
i = 0
for pdf in path:
    pdf = path[i]
    append_pdf(PdfFileReader(open(path[i],"rb")),output)
    i= i + 1

# Writing all the collected pages to a file
output.write(open(r"G:\pworks\assetmanagement\GISZBakhtiari\Map_Requests\StreetSweepingAreas\Outputs\CombindedPDF.pdf","wb"))


print "Script Complete!",time.ctime()