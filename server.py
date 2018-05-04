from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    fruitFiles = os.listdir("static/img")
    print(fruitFiles)
    return render_template("fruits.html", fruitFiles = fruitFiles)

if __name__=="__main__":   
    app.run(debug=True)
