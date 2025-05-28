import os
import openai
from fpdf import FPDF

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_property_insights_and_pdf(address):
    prompt = f"""You are a helpful assistant. Provide property insights and negotiation tips for this address: {address}"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    content = response.choices[0].message["content"]

    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.split("\n"):
        pdf.cell(200, 10, txt=line.strip(), ln=True)
    pdf_output_path = "/mnt/data/property_report.pdf"
    pdf.output(pdf_output_path)

    return {
        "text": content,
        "download_link": "https://drive.google.com/file/d/your_pdf_link_here/view"
    }