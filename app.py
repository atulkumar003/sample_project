from flask import  Flask

app  = Flask('__name_')

@app.route('/')
def home():
    return "<div>I am home page </div>"


if __name__  == "__main__":
    app.run(debug=True)