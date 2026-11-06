from flask import Flask, jsonify, render_template

app = Flask(__name__)


'''
This is a file to load html.
this same html page will serve as a single-page application
this page will load javascript file, and it will make ajax call/jquery to call our
backend api.

Although backend apis are also coded into the same flask project but it will simulate 
a microservice project.
'''
@app.route('/')
def index():
    return render_template('index.html')



'''
Hint: What is the Restful API naming schemas? Pluras or singular?
'''
@app.route("/taxrecords/all", methods=['GET'])
def hello_microservice():
    '''
    Connect to your database and make queries, then manipulate your result into the following format 
    '''
    message = {"id": "1", "name": "Kevin Li", "score": 90}
    return jsonify(message)


if __name__ == "__main__":
    app.run(port=8000)

