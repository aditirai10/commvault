from flask import Flask, request, render_template, send_file
import os

app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    email = request.form['email']
    filename = request.form['filename']
    file = request.files['file']

    if email and filename and file:
       
        unique_filename = f"{email}_{filename}.txt"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        return 'File uploaded successfully'
    else:
        return 'Invalid input data'

@app.route('/search', methods=['GET'])
def search():
    email = request.args.get('email')
    query = request.args.get('query')

    if email and query:
       
        results = [filename for filename in os.listdir(app.config['UPLOAD_FOLDER']) if email in filename and query in filename]
        return render_template('search_results.html', results=results)
    else:
        return 'Invalid input data'

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
