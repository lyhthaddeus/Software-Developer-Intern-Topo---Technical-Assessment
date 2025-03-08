import re
from flask import Blueprint, jsonify
from ingest.ParseJson import parse_json
from ingest.ParseCsv import parse_csv
from ingest.ParsePptx import parse_pptx
from ingest.ParsePdf import parse_pdf, format_data
from utils.Unified import unify

api = Blueprint('api', __name__)

@api.route('/get_json_data', methods=['GET'])
def get_json_data():
    json_file = "datasets/dataset1.json"
    parsed_data = parse_json(json_file)
    return jsonify(parsed_data)


@api.route('/get_csv_data', methods=['GET'])
def get_csv_data():
    csv_file = "datasets/dataset2.csv"  # Replace with your actual CSV file path
    parsed_data = parse_csv(csv_file)
    return jsonify(parsed_data)

@api.route('/get_pptx_data', methods=['GET'])
def get_pptx_data():
    pptx_file = "datasets/dataset4.pptx"  # Replace with your actual PowerPoint file path
    parsed_data = parse_pptx(pptx_file)
    return jsonify(parsed_data)

@api.route('/get_pdf_data', methods=['GET'])
def get_pdf_data():
    pdf_file = "datasets/dataset3.pdf"  # Replace with your actual PDF file path
    parsed_data = parse_pdf(pdf_file)
    formatted_data = format_data(parsed_data)
    return jsonify(formatted_data)

@api.route('/get_unified_data', methods=['GET'])
def get_unified_data():
    unified = unify()
    return jsonify(unified)
