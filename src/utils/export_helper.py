from docx import Document
from docx.shared import Pt
import pdfkit
import tempfile
import os

def export_to_docx(content, filename="business_strategy"):
    doc = Document()
    
    # Add title
    doc.add_heading('Business Strategy Report', 0)
    
    # Process content sections
    sections = content.split('## ')
    for section in sections:
        if section.strip():
            heading, _, body = section.partition('\n')
            if heading:
                doc.add_heading(heading.strip(), level=2)
                doc.add_paragraph(body.strip())
    
    # Save to temporary file
    temp_path = f"{filename}.docx"
    doc.save(temp_path)
    return temp_path

def export_to_pdf(content, filename="business_strategy"):
    # Create temporary HTML file
    html_content = f"<h1>Business Strategy Report</h1>{content.replace('## ', '<h2>').replace('\n', '<br>')}"
    
    options = {
        'encoding': 'UTF-8',
        'quiet': ''
    }
    
    temp_path = f"{filename}.pdf"
    pdfkit.from_string(html_content, temp_path, options=options)
    return temp_path