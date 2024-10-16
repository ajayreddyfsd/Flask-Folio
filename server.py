from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def desired_page(page_name):
    return render_template(page_name)

def writeData(data):
    with open(r'FlaskFolio\database.txt', mode='a') as f:
      print(str(data))
      f.write(str(data) + '\n')

import csv

def writeDataCSV(data):
    # Assuming data is a dictionary with keys 'emailId', 'emailSubject', and 'emailBody'
    with open(r'FlaskFolio\database.csv', mode='a', newline='') as f:
        csv_writer = csv.writer(f, delimiter=",")
        
        # Extract the values from the dictionary
        emailId = data.get('emailId', '')
        emailSubject = data.get('emailSubject', '')
        emailBody = data.get('emailBody', '')
        
        # Write the values to the CSV file
        csv_writer.writerow([emailId, emailSubject, emailBody])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        writeDataCSV(data)
        return redirect('thankyou.html')
    else:
        return 'something wrong!'

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')










