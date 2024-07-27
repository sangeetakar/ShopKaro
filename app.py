from flask import Flask,render_template

app = Flask(__name__) #    https://www.youtube.com/watch?v=4dkNn93DIx4

@app.route('/')
def index():
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True)
