from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Load the marks from the JSON file
with open("marks.json", "r") as f:
    marks_data = json.load(f)
    print(marks_data[:5])  # Print the first 5 records for debugging



@app.route("/api", methods=["GET"])
def get_marks():
    # Get names from the query string (?name=X&name=Y)
    names = request.args.getlist("name")
    print(f"Received names: {names}")  # Debugging log
    
    results = []
    for name in names:
        # Search for the student by name in the JSON data
        student = next((item for item in marks_data if item["name"] == name), None)
        print(f"Searching for {name}: {'Found' if student else 'Not Found'}")  # Debugging log
        
        if student:
            results.append(student["marks"])  # If found, add their marks
        else:
            results.append(None)  # If not found, append None
    
    return jsonify({"marks": results})

if __name__ == "__main__":
    app.run(debug=True)
