'''
This assignment asks for the file names for input and output and then starting and ending pages to extract.
'''
import PyPDF2 as pdf


# Main function to put it all together
def main():
    # Loop for correct file name input
    while True:
        fname = input('Please enter a file name: ')
        try:
            fhand = pdf.PdfFileReader(fname)
            break
        except:
            print(f'File {fname} does not exist.')

    # Loop to get pages to extract
    while True:
        fpage = input('Please enter the beginning page number to extract: ')
        spage = input('Please enter the ending page number to extract: ')

        # Attempt string to int conversion
        try:
            first_page = int(fpage)
            second_page = int(spage)
        except:
            print('Inputs are not numbers')
        else:
            # Determine if page range is correct
            if first_page >= second_page:
                print('Your beginning and ending page numbers are not correct.')
            elif second_page > fhand.getNumPages():
                print('Your ending index is out of range, please enter correct ending page.')
            elif first_page < second_page:
                break

    # Get pages to extract
    writer = pdf.PdfFileWriter()
    for page in range(first_page, second_page):
        writer.addPage(fhand.getPage(page-1))

    # Save extracted pages to new file
    output = input('Please enter output file name: ')
    with open(output, 'wb') as out:
        writer.write(out)


# Run the program
main()
