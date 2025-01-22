import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML page (index.html) when the root URL is accessed
    return render_template('index.html')

if __name__ == '__main__':
    # Generate a random port number between 5000 and 6000
    port = random.randint(5000, 6000)
    # Run the app on localhost with the random port
    app.run(debug=True, port=port)
