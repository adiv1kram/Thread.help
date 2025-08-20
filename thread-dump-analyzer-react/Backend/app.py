from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import parse_thread_dump
from analyzer import analyze_with_genai 
import os

app = Flask(__name__)
CORS(app, resources={r"/analyze": {"origins": "http://localhost:5173"}})

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/analyze', methods=['POST'])
def analyze_thread_dump():
    if 'dumpfile' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['dumpfile']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        try:
            content = file.read().decode('utf-8', errors='ignore')
            
            
            parsed_data = parse_thread_dump(content)
            
            
            analysis_result = analyze_with_genai(parsed_data)
            
           
            return jsonify({"analysis": analysis_result})

        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
    
    return jsonify({"error": "File type not allowed"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)