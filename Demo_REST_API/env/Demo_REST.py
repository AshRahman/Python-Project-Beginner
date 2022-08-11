#from crypt import methods
from distutils.log import debug
from flask import Flask, jsonify
app = Flask(__name__)

courses = [{ 'name': "Python Crash course",
            'course_id': "0",
            'Description' : "This is a crash course",
            'price' : "visit the website"},
           { 'name': "Java Crash course",
            'course_id': "1",
            'Description' : "This is a crash course",
            'price' : "visit the website"}
           
    
]

@app.route("/")
def index():
    return "Welcome to REST"

@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses':courses})

@app.route("/courses/<int:course_id>",methods=['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})


@app.route("/courses", methods=['POST'])
def create():
    course = { 'name': "Data Mining Crash course",
            'course_id': "2",
            'Description' : "This is a crash course",
            'price' : "visit the website"}
    courses.append(course)
    return jsonify({'Created': course})
"""
    Commands for POST method
    Remove-item alias:curl -> this is for un-aliasing curl for windows reason
   curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/courses

"""
@app.route("/courses/<int:course_id>",methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description'] ="XYZ"
    return jsonify({'course':courses[course_id]})

if __name__=="__main__":
    app.run(debug=True)