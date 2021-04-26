import pdfplumber

filename = 'main.pdf'
total_number_of_spaces = 0

with pdfplumber.open(filename) as pdf:
    for page in range(len(pdf.pages)):
        page_content = pdf.pages[page].extract_text()
        splitted = page_content.split()
        words = [s for s in splitted if len(s)>2]
        counted_spaces = len(words)
        #print(page_content)
        print(counted_spaces, 'words')
        total_number_of_spaces += counted_spaces

    
print(total_number_of_spaces, 'words in total (not including math equations)')


print('\n\n')

with pdfplumber.open(filename) as pdf:
    for page in range(len(pdf.pages)):
        page_content = pdf.pages[page].extract_text()
        splitted = page_content.split()
        counted_spaces = len(splitted)
        print(counted_spaces, 'words')
        total_number_of_spaces += counted_spaces

    
print(total_number_of_spaces, 'words in total (including math equations)')


input()


