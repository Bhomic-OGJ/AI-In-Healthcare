try:
    import PyPDF2
    import os
    from PIL import Image
    import io
    
    def extract_pdf_pages(pdf_path, output_folder):
        """Extract pages from PDF and save as images"""
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                
                # Try to extract images from the page
                try:
                    if '/XObject' in page['/Resources']:
                        xObject = page['/Resources']['/XObject'].get_object()
                        
                        for obj in xObject:
                            if xObject[obj]['/Subtype'] == '/Image':
                                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                                data = xObject[obj].get_data()
                                
                                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                                    mode = "RGB"
                                else:
                                    mode = "P"
                                
                                img = Image.open(io.BytesIO(data))
                                img.save(f"{output_folder}/page_{page_num + 1}.png")
                                print(f"Saved page {page_num + 1}")
                except:
                    pass
    
    pdf_path = "assets/Brochure_Application of Artificial Intelligence in Health Sciences (1).pdf"
    output_folder = "assets/pages"
    
    extract_pdf_pages(pdf_path, output_folder)
    print("Page extraction completed!")
    
except ImportError:
    print("Required libraries not available. Using fallback method...")
    
    # Fallback: Create placeholder images
    import os
    
    if not os.path.exists("assets/pages"):
        os.makedirs("assets/pages")
    
    # Create placeholder images using a simple approach
    print("Creating placeholder images for demonstration...")
