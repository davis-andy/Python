'''
This assignment merges two files together.
'''
import PyPDF2 as pdf


# Main function to put it all together
def main():
    # Set up merger
    merger = pdf.PdfFileMerger()
    output_name = 'CorrectedFile.pdf'

    # Get both pdf files
    needing_pages = pdf.PdfFileReader('pythonlearn_ch8MissingPages.pdf')
    missing_pages = pdf.PdfFileReader('From_pythonlearn_ch8.pdf')

    # Merge pages in correct place
    merger.append(needing_pages)
    merger.merge(4, missing_pages)


    # Save extracted pages to new file
    with open(output_name, 'wb') as out:
        merger.write(out)


# Run the program
main()
