from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def desired_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        
        with open('database.txt', mode='a') as f:
            emailId, emailSubject, emailBody = data
            f.write(f'{emailId},{emailSubject},{emailBody}')

        return redirect('thankyou.html')
    else:
        return 'something wrong!'


