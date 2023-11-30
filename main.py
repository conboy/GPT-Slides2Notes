import fitz
import os

def convert_pdf_to_images(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    output_folder = pdf_path[:-4]

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert each page to an image
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)  # number of page
        pix = page.get_pixmap()
        output_file = f"{output_folder}/{output_folder}_slide_{page_number + 1}.png"
        pix.save(output_file)
    
    doc.close()
    return f"Converted PDF into images. Check the folder: {output_folder}"

# Example usage
pdf_path = 'Chapter6.pdf'
output_folder = 'C:\\Users\\conja\\GPT-Slides2Notes\\Chapter6'
convert_pdf_to_images(pdf_path)
