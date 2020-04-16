from flask import Flask, render_template
 
app = Flask(__name__)
 
 
@app.route('/')
def home():
    return render_template("login.html")
 
if __name__ == '__main__':
    app.run(debug=True, host='18.217.234.114')
    
    
 