'''
This assignment concatenates three PDF files together and name merged file as "MergedFile.pdf".
'''
import PyPDF2 as pdf
import glob


# Main function to put it all together
def main():
    # Set up merger
    merger = pdf.PdfFileMerger()
    output_name = 'MergedFile.pdf'

    # Get list of .pdf files in path
    pdf_list = list(glob.glob('*.pdf'))
    pdf_list.sort()

    # Merge PDFs
    for file in pdf_list:
        merger.append(str(file))

    # Save extracted pages to new file
    with open(output_name, 'wb') as out:
        merger.write(out)


# Run the program
main()
