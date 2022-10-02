#from datetime import datetime
# Import the model module from the current directory
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS

#Impor the model module from the ml folder
import ml as model

app = Flask(__name__)

CORS(app)

# Create a global variable to store the input data
input_data = {}

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/api/request', methods=['POST'])
def api_request():
    print('Request for api request received')
    userInput = request.data.decode('utf-8')
    print(userInput)
    return 'ok'

@app.route('/api/predict', methods=['GET'])
def api_predict():
    print('Request for api predict received')
    userInput = request.data.decode('utf-8')
    print(userInput)
    modelAnswer = model.predict(userInput)
    return modelAnswer

@app.route('/api/response', methods=['GET'])
def api_response():
    # Check if the user has requested a response
    print('Request for api response received')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()