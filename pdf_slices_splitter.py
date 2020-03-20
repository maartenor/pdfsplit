
# pdf_slices_splitter.py

from PyPDF2 import PdfFileWriter, PdfFileReader

# PyPDF2.PageRange() ... already available

def pdf_slices_splitter(inputpdf, slice_list):
        
    if len(slice_list) < 2 :
        slice_list = [0, max(range(inputpdf.numPages))]
    
    print(slice_list)
    
    for i in range(inputpdf.numPages):
        if (i >= slice_list[0]) & (i <= slice_list[-1]):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open("document-page%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)         

if __name__ == '__main__':  
    inputpdf = PdfFileReader(open("Deuren_nl_kozijn.pdf", "rb"))
    slice_list = [0,range(inputpdf.numPages)]

    try:
        start_page_num=int(input(prompt='Please provide first page to split from PDF file. '))

        if start_page_num<1:
            start_page_num=0
    except: 
        start_page_num=0
    
    try:
        end_page_num=int(input(prompt='Please provide last page to split from PDF file. '))

        slice_list=[start_page_num, end_page_num]

    except: 
        slice_list=[start_page_num]

    
    pdf_slices_splitter(inputpdf, slice_list)
                        

