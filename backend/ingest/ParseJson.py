import json

def parse_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data 
    # standardized_data = []
    # for company in data.get("companies", []):
    #     company_id = company.get("id")
    #     company_name = company.get("name")
    #     industry = company.get("industry")
    #     revenue = company.get("revenue")
    #     location = company.get("location")
    #
    #     for employee in company.get("employees", []):
    #         standardized_data.append({
    #             "company_id": company_id,
    #             "company_name": company_name,
    #             "industry": industry,
    #             "location": location,
    #             "revenue": revenue,
    #             "employee_id": employee.get("id"),
    #             "employee_name": employee.get("name"),
    #             "role": employee.get("role"),
    #             "salary": employee.get("cashmoneh"),
    #             "hired_date": employee.get("hired_date")
    #         })
    #
    #     for quarter, metrics in company.get("performance", {}).items():
    #         standardized_data.append({
    #             "company_id": company_id,
    #             "company_name": company_name,
    #             "industry": industry,
    #             "location": location,
    #             "revenue": revenue,
    #             "quarter": quarter,
    #             "quarterly_revenue": metrics.get("revenue"),
    #             "profit_margin": metrics.get("profit_margin")
    #         })
    #
    # return standardized_data

# Example usage
# json_file = "../datasets/dataset1.json"  # Replace with your actual JSON file
# parsed_data = parse_json(json_file)
# for entry in parsed_data:
    # print(entry)
