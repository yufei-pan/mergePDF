from PyPDF2 import PdfFileMerger
import os
from natsort import natsorted

#Create an instance of PdfFileMerger() class
merger = PdfFileMerger()


# Get the list of files in the current directory
files = natsorted(os.listdir())

# Print the files
for file in files:
    if file.rpartition('.')[2] == 'pdf':
        print(file)
        merger.append(file)

# #Write out the merged PDF file
merger.write("merged.pdf")
merger.close()