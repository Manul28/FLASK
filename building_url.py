###Building-Url-Dynamically-->done
####Variable Rules And Url Building-->done
from flask import Flask,redirect,url_for

app=Flask(__name__)
#To show the different pages of result is passed or fail
# for that we use url_for
@app.route('/')
# this is the binding function
def welcome():
    return 'Welcome to Vscode'
# app.route(,<>) inside we have to provide datatype 
# if we don't provide the datatype then it will automatically will be taken as string datatype
#<> this is used for parameters
@app.route('/success/<int:score>')
def success(score):
    # if(score>=40):
        return 'The person has passed and the marks is '+str(score)
@app.route('/failure/<int:score>')
def failure(score):
    # if(score<40): 
        return 'The person has failed and the marks is '+str(score)
@app.route('/results/<int:marks>')    
def results(marks):
    result=""
    if marks>=40:
        result='success'
    else:
        result='failure'  
    # return 'The person is '+str(result)      
    return redirect(url_for(result,score=marks)) 
#url_for 1st functionality is that at what page u want to redirect 
#url_for 2nd along with the parameter we have to send in the parentheses
if __name__=='__main__':
    app.run(debug=True)