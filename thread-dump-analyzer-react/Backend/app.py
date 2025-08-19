from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import parse_thread_dump
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure CORS to allow requests from your React frontend (running on localhost:5173)
CORS(app, resources={r"/analyze": {"origins": "http://localhost:5173"}})

# Define the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/analyze', methods=['POST'])
def analyze_thread_dump():
    """
    API endpoint to upload and analyze a thread dump file.
    """
    # Check if a file was included in the request
    if 'dumpfile' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['dumpfile']

    # Check if a file was selected
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Check if the file is of an allowed type and process it
    if file and allowed_file(file.filename):
        try:
            # Read the content of the file as a string
            content = file.read().decode('utf-8')
            
            # Parse the content using the parser module
            parsed_data = parse_thread_dump(content)
            
            # In the future, this is where you would send `parsed_data` to the GenAI model.
            # For now, we just return the parsed JSON.
            
            return jsonify(parsed_data) # CORRECTED LINE: Removed extra parentheses

        except Exception as e:
            return jsonify({"error": f"An error occurred during parsing: {str(e)}"}), 500
    
    return jsonify({"error": "File type not allowed"}), 400

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(host='0.0.0.0', port=5000, debug=True)

