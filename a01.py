from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>資資資資資資資資資資</p>"

if __name__ =="__main__":
    app.run()