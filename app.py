from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the expected format of the JSON data
expected_format = {
    "location": str,
    "area_sqft": float,
    # Add more fields as per your requirements
}


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    # Parse the incoming JSON data
    data = request.json

    # Check if the incoming JSON data matches the expected format
    if all(field in data and isinstance(data[field], expected_format[field]) for field in expected_format):
        # Proceed with further processing
        # Call utility functions to predict home price, etc.
        # Example:
        location = data['location']
        area_sqft = data['area_sqft']
        # Perform prediction using the provided data

        # Return the predicted result
        return jsonify({"predicted_price": predicted_price})
    else:
        # Return an error response if the data format is incorrect
        return jsonify({"error": "Invalid data format"}), 400


if __name__ == '__main__':
    app.run(debug=True)
