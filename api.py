from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Load the marks from the JSON file
with open("marks.json", "r") as f:
    marks_data = json.load(f)

@app.route("/api", methods=["GET"])
def get_marks():
    # Get names from the query string (?name=X&name=Y)
    names = request.args.getlist("name")
    # Retrieve marks for each name (returns None if name not found)
    results = [marks_data.get(name, None) for name in names]
    # Return JSON response
    return jsonify({"marks": results})

if __name__ == "__main__":
    app.run(debug=True)

