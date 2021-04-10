import PyPDF2

filename = 'main.pdf'

pdf_file = open(filename, 'r')

read_pdf = PyPDF2.PdfFileReader(filename)
number_of_pages = read_pdf.getNumPages()

print(number_of_pages, "pages found")

pattern = ' '
total_number_of_spaces = 0

for page in range(number_of_pages):
    read_page = read_pdf.getPage(page)
    page_content = read_page.extractText()
    counted_spaces_per_page = len(page_content.split())
    #print(page_content)
    print(counted_spaces_per_page, 'words')
    total_number_of_spaces += counted_spaces_per_page

print(total_number_of_spaces, 'words in total')

input()

