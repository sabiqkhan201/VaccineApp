from flask import *
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'cards/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'key'
app.config['SESSION_TYPE'] = 'filesystem'

vaxcode = ""


@app.route('/')
def home():
    return render_template("index.html", vax_code=vaxcode)

@app.route('/add', methods=["POST", "GET"])
def add():
    global vaxcode
    vaxcode = "Your code is: 5862"
    if request.method == "POST":
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('add',
                                    filename=filename))
        
    return render_template("add.html")

@app.route('/business')
def business():
    return render_template("business.html")

if __name__ == '__main__':
    
    app.run(debug=True)
