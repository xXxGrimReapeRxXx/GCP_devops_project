from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, World! This is the home page.'

# Define a route for another page
@app.route('/about')
def about():
    return 'This is the about page.'

# Define a route that renders an HTML template
@app.route('/template')
def template_example():
    # Create a dictionary to pass data to the template
    data = {'title': 'Flask Template Example', 'content': 'This is content from the Flask app.'}
    return render_template('template_example.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
