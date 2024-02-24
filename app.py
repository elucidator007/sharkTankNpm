from flask import Flask, jsonify
import requests

app = Flask(__name__)

# GitHub URL to the raw JSON file
github_json_url = 'https://github.com/elucidator007/sharkTankNpm/blob/main/sharkTankData.json'

# API endpoint to get the JSON data
@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # Fetch JSON data from GitHub
        response = requests.get(github_json_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        json_data = response.json()
        return jsonify(json_data)
    except requests.RequestException as e:
        return f"Error fetching data from GitHub: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
