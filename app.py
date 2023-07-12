#app
import os
from flask import *
import pickle
app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")
    
@app.route("/pred",methods=['get','post'])
def pred():
    msg=""
    pr=float(request.form["pr"])
    gl=float(request.form["gl"])
    bp=float(request.form["bp"])
    st=float(request.form["st"])
    ins=float(request.form["ins"])
    bmi=float(request.form["bmi"])
    dp=float(request.form["dp"])
    age=float(request.form["age"])
    with open("de.model","rb") as f:
            model=pickle.load(f)
    d=[[pr,gl,bp,st,ins,bmi,dp,age]]
    res=model.predict(d)[0]
    if res==0:	   
        msg="Diabetes NOT detected!!"
    elif res==1:    
        msg="Diabetes detected!!"
    return render_template("home.html",msg=msg)
    
if __name__=="__main__":
    app.run(debug=True)