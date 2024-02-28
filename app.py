from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Software Engineer',
    'location': 'Chennai, India',
    'salary' : 'Rs. 23,00,000'
  },
  {
    'id': 3,
    'title': 'Cloud Solutions Architect',
    'location': 'Delhi, India',
    'salary' : 'Rs. 18,00,000'
  },
  {
    'id': 4,
    'title': 'UI/UX Designer',
    'location': 'Remote',
    'salary' : 'Rs. 7,00,000'
  },
  {
    "id": 5,
    "title": "Business Intelligence Analyst",
    "location": "London, UK",
    "salary": "£50,000"
  }
    ]

@app.route("/")
def hello_User():
  return render_template('home.html', 
                         jobs = JOBS,
                         company_name='Talent Quest Hub')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
