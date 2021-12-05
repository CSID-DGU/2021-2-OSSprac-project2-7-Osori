from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   if request.method =='POST':
      if request.form['username'] != 'ossp' or request.form['password'] != 'ossp1234' :
            error = 'Incorrect authentication credentials! Please try again. '
      else:
         return render_template('orderList.html')
   
   return render_template('login.html', error = error)

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
   uname=request.form.get('uname')
   type=request.form.get('type')
   color=request.form.get('color')
   number=request.form.get('number')

   
   return render_template('submit.html',uname=uname, type=type, color=color, number=number)

if __name__ == '__main__': 
    app.run(host="0.0.0.0", debug=True, port=80)

   