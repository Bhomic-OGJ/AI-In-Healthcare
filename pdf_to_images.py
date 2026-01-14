import fitz  # PyMuPDF
import os

def convert_pdf_to_images(pdf_path, output_folder):
    """Convert PDF pages to high-quality images"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    # Get total number of pages
    total_pages = len(pdf_document)
    print(f"PDF has {total_pages} pages")
    
    # Convert each page to image
    for page_num in range(total_pages):
        # Get the page
        page = pdf_document.load_page(page_num)
        
        # Render page to an image (high quality)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for better quality
        
        # Save the image
        image_path = os.path.join(output_folder, f"page{page_num + 1}.jpg")
        pix.save(image_path)
        print(f"Saved: {image_path}")
    
    pdf_document.close()
    print(f"Successfully converted {total_pages} pages to images!")

# Try to install PyMuPDF if not available
try:
    import fitz
except ImportError:
    print("Installing PyMuPDF...")
    os.system("pip install PyMuPDF")
    import fitz

# Convert the brochure PDF
pdf_path = "assets/Brochure_Application of Artificial Intelligence in Health Sciences (1).pdf"
output_folder = "assets/pages"

if os.path.exists(pdf_path):
    convert_pdf_to_images(pdf_path, output_folder)
else:
    print(f"PDF file not found: {pdf_path}")
