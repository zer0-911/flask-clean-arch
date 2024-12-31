from flask import Blueprint, jsonify, request, render_template

page_bp = Blueprint('page_bp', __name__)

@page_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')