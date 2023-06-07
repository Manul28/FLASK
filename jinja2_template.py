#Jinja2 template engine
'''
{%...%} -->condition,For loop Statement
{{  }} --> expression to print output
{#...#} --> this is for comment in the html file 
'''
from flask import Flask,request,url_for,redirect,render_template

app=Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if(score>=50):
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score,'res':res}    
    return render_template('result.html',result=exp)
@app.route('/failure/<int:score>')
def failure(score):
        return 'The person has failed and the marks is '+str(score)
### result checker    
@app.route('/results/<int:marks>')    
def results(marks):
    result=""
    if marks>=40:
        result='success'
    else:
        result='failure'
            
    return redirect(url_for(result,score=marks)) 
#methods can of two things--> that is POST AND GET
@app.route('/submit',methods=['POST','GET'])
##this my Result checker html page
def submit():
    totalscore=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        totalscore=(science+maths+c+datascience)/4
    res=""
    if(totalscore<50):
        res='failure'
    else:
        res='success'    
    return redirect(url_for('success',score=totalscore))

if __name__=='__main__':
    app.run(debug=True)
