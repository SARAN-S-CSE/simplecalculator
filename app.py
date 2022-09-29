from flask import Flask,render_template,request,jsonify
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/submit",methods=["POST","GET"])
def cal():
    if(request.method=="POST"):
        operation=request.form["operation"]
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if(operation=="add"):
            r=num1+num2
            result=r
        if (operation == "sub"):
            r = num1 - num2
            result = r
        if (operation == "mul"):
            r = num1 * num2
            result = r
        if (operation == "div"):
            r = num1 // num2
            result = r
        return render_template("submit.html",result=result)
if __name__=='__main__':
    app.run(debug=True,)