from flask import Flask, request, jsonify

app = Flask(__name__)

# POST endpoint to receive and print POST data
@app.route('/receive_post_data', methods=['POST'])
def receive_post_data():
    data = request.get_json()  # assuming JSON data in the POST request
    print(f"Received POST data: {data}")
    return "POST data received successfully!"

# GET endpoint to provide a sample response
@app.route('/sample_get_endpoint', methods=['GET'])
def sample_get_endpoint():
    response = {"message": "Hello, this is a sample GET endpoint!"}
    return jsonify(response)

if __name__ == '__main__':
    # Bind to '0.0.0.0' to make it accessible externally
    # Use a specific port, for example, 5000
    app.run(host='0.0.0.0', port=8000, debug=True)
