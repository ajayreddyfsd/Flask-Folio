from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# instead of writing all the routes one by one
# just extract the url slug and display that specific page accordingly
@app.route('/<string:page_name>')
def desired_page(page_name):
    return render_template(page_name)


def writeData(data):
    # Assuming data is a dictionary with keys 'emailId', 'emailSubject', and 'emailBody'
    with open(r'FlaskFolio\database.txt', mode='a') as f:
        # Extract the values from the dictionary
        emailId = data.get('emailId', '')
        emailSubject = data.get('emailSubject', '')
        emailBody = data.get('emailBody', '')
        
        # Format the data and write to the text file
        # Adjust the format string as needed
        f.write(f"Email ID: {emailId}\nSubject: {emailSubject}\nBody: {emailBody}\n\n")


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
        writeData(data)
        #writeDataCSV(data)
        return redirect('thankyou.html')
    else:
        return 'something wrong!'


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')










