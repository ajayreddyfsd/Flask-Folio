from flask import Flask, render_template, url_for, render_template_string, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/ajay')
def ajay():
    return render_template('./ajay.html')


#simple form handling code
#provided form tag has this method and action
#<form method="POST" action="/form"></form>
# so when button of form is hit, it hits the specific route mentioned in the form tag's action attr
@app.route('/form', methods=['POST', 'GET'])
def form():

    if(request.method == 'POST'):
        data = request.form.to_dict()
        print(data['name'], data['email'], data['message'])
        return redirect('/thankyou')
    

    return render_template('./form.html')


@app.route('/thankyou')
def thankyou():
    return render_template('./thankyou.html')



if __name__ == '__main__':
    app.run(debug=True)
