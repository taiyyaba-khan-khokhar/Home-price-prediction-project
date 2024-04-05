from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from waitress import serve
import util
import os  # Don't forget to import the 'os' module


app = Flask(__name__, static_folder='client')
CORS(app)  # Enable CORS for all origins

# Route to serve the app.html file
@app.route('/')
def serve_app():
    print("Current working directory:", os.getcwd())
    # Print the path to the app.html file (for debugging)
    app_html_path = os.path.join(app.static_folder, 'app.html')
    print("Path to app.html:", app_html_path)

    return send_from_directory(app.static_folder, 'app.html')

# Serve static files from the client folder
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('client', filename)


@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({'locations': util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Log the incoming JSON data
        print("Received JSON data:", request.json)

        # Check if request has JSON data
        if not request.json:
            return jsonify({'error': 'No JSON data provided'}), 400

        total_sqft = float(request.json.get('total_sqft', 0))
        location = request.json.get('location', '')
        bhk = int(request.json.get('bhk', 0))
        bath = int(request.json.get('bath', 0))

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        response = {'estimated_price': estimated_price}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    print("Starting Python Flask server for home price prediction...")
    util.load_saved_artifacts()
    serve(app,host='0.0.0.0',port=8000, _quiet=False)
