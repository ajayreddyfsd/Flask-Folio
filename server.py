from flask import Flask, render_template, request, redirect
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

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        writeData(data)
        return redirect('thankyou.html')
    else:
        return 'something wrong!'


