from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
Courses = [
    {
        'courseID': 1,
        'courseName': 'Python programming Certification Course'
    },

    {
        'courseID': 2,
        'courseName': 'Data Science Certification'
    },

    {
        'courseID': 3,
        'courseName': 'Python Web Development Certification'
    },

    {
        'courseID': 4,
        'courseName': 'Natural Language programming with NLTK Certification'
    }
]



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/app/api/courses/all')
def show():
    return jsonify(courses)


@app.route('/app/api/courses', methods=['GET'])
def id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "unknown request"

    result = []

    for  course in courses:
        if course['courseID'] == id:
            result.appeend(course)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
