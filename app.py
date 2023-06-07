from flask import Flask
#WSGI Application is used here
#create flask app object
app=Flask(__name__)
#decorator --> @
#decorator is used for differiation of url
@app.route('/')
# your binding function should be diiferent
def welcome():
    return 'WELCOME TO DELOITTE My name is MANUL RASTOGI'

@app.route('/premium_employees')
#next function should be different from the binding function
def premium_employees():
    return 'HR Manager'

if __name__=='__main__':
     # debug =True means that if we make changes in the application then it will automatically change the application without re-run
    app.run(debug=True)