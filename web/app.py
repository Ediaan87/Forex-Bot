from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    # Code to display the home page
    return render_template('home.html')

@app.route('/override', methods=['POST'])
def override():
    # Code to handle manual override
    return render_template('override.html')

if __name__ == '__main__':
    app.run(debug=True)