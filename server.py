from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def process_form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        users_text = request.form['text']
        processed_text = users_text.upper()        
        return processed_text


if __name__ == '__main__':
    app.run()
