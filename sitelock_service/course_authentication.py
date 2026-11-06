from flask import Flask, request, jsonify
from datetime import datetime
import json
import hashlib

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello,Blog Server running...</h1>"

pass_phrase = b'unlockme'

# API to check if the email exists in students.json
@app.route('/check_user', methods=['POST'])
def check_user():
    try:
        # Load the students.json file
        with open('students.json', 'r') as f:
            students_data = json.load(f)

        # Extract emails from the loaded students_data
        students = students_data['emails']
        
        # Get the email data from request
        data = request.json
        email = data.get('email')

        # Check if email is in the students list
        if email in students:
            return jsonify({"message": "Valid user", "status": "success"})
        else:
            return jsonify({"message": "Invalid user", "status": "failure"}), 404
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e), "status": "failure"}), 500


# API to fetch the hash of the password
@app.route('/get_hash', methods=['get'])
def get_hash():
  return hashlib.md5(pass_phrase).hexdigest()


# Not being used right now
@app.route('/get_encryption_code', methods=['get'])
def get_encryption_code():
   hr = str(datetime.now().hour)
   encode = str(hashlib.md5(b'unlockme').hexdigest()+hr).encode()
   return hashlib.md5(encode).hexdigest()
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)