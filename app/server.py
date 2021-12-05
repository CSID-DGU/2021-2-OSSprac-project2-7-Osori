from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
data = {
   500211204: {'기종':'12 pro max','색상':'스톤','문구':'Hello'},
   500211205: {'기종':'12 mini','색상':'블랙','문구':'OSSprac'},
   500211208:{'기종':'13 pro','색상':'레몬','문구':'Apple'}
}

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
         return redirect(url_for('orderList'))
   
   return render_template('login.html', error = error)

@app.route('/orderList', methods = ['POST', 'GET'])
def orderList():
   return render_template('orderList.html', data=data)

@app.route('/order', methods=['POST', 'GET'])
def order():
   return render_template('order.html')

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
   uname=request.form.get('uname')
   type=request.form.get('type')
   color=request.form.get('color')
   number=request.form.get('number')   
   return render_template('submit.html',uname=uname, type=type, color=color, number=number)

@app.route('/check/<int:orderNum>')
def check(orderNum):
   return render_template("check.html", orderNum=orderNum, data=data.get(orderNum))

if __name__ == '__main__': 
    app.run(host="0.0.0.0", debug=True, port=80)
