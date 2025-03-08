import pdfplumber
import json

def parse_pdf(pdf_file):
    data = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                data.append(text)
    return data

def format_data(raw_data):
    formatted_data = []
    text = "\n".join(raw_data)
    lines = text.split("\n")
    for line in lines[1:]:  # Skip header line
        columns = line.split()
        if len(columns) == 5:  # Ensure correct number of columns
            year, quarter, revenue, memberships_sold, avg_duration = columns
            formatted_data.append({
                "year": int(year),
                "quarter": quarter,
                "revenue": int(revenue.replace(",", "")),  # Remove commas in the revenue
                "membershipsSold": int(memberships_sold),
                "avgDuration": int(avg_duration)
            })
    return formatted_data

# pdf_file = "../datasets/dataset3.pdf"  # Replace with your actual PDF file

# parsed_pdf = parse_pdf(pdf_file)
# print(parsed_pdf)
# formatted_data = format_data(parsed_pdf)
#
# formatted_json = json.dumps(formatted_data, indent=2)
# print("Formatted Data:", formatted_json)
