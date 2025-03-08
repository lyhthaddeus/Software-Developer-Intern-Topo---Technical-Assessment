from ingest.ParseJson import parse_json
from ingest.ParseCsv import parse_csv
from ingest.ParsePptx import parse_pptx
from ingest.ParsePdf import parse_pdf, format_data
import json

def get_json():
    json_file = "datasets/dataset1.json"
    parsed_data = parse_json(json_file)
    return parsed_data
    
def combine_csv(json_file):
    csv_file = "datasets/dataset2.csv"
    parsed_data = parse_csv(csv_file)
    for company in json_file['companies']:
        if company['name'] == "FitPro":
            company['activity_data_Jan24'] = parsed_data
    return json_file

def combine_pdf(json_file):
    pdf_file = "datasets/dataset3.pdf"  
    parsed_data = parse_pdf(pdf_file)
    performance_data = format_data(parsed_data)
 
    for company in json_file['companies']:
        if company['name'] == "FitPro":
            performance = company.get('performance', {})
            for entry in performance_data:
                year = entry['year']
                quarter = entry['quarter']
                key = f"{year}_{quarter}"

                if key in performance:
                    performance[key]['revenue'] = entry['revenue'] 
                    performance[key]['membershipsSold'] = entry['membershipsSold']
                else:
                    performance[key] = {
                        'revenue': entry['revenue'],
                        'membershipsSold': entry['membershipsSold']
                    }


               
    return json_file

def unify():
    json_data = get_json()
    activity_data_added = combine_csv(json_data)
    performance_data_added = combine_pdf(activity_data_added)
    for company in performance_data_added['companies']:
        del company['revenue']
    return performance_data_added

