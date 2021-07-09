from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
# from flask_assets import Bundle, Environment
import os

app = Flask(__name__)
app.secret_key = 'mysecret'

app.config['MONGO_URI'] = 'mongodb://localhost:27017/healfavor'
mongo = PyMongo(app)

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    if 'username' in session:
        #return 'You are logged in as  :' + session['username']
        return render_template('bot.html')
    test = True
    return render_template('login.html', test = test)

@app.route('/admin')
def admin():
    if 'username' in session:
        #return 'You are logged in as  :' + session['username']
        users = mongo.db.users
        chats = mongo.db.chats
        session['total'] = users.count()
        session['total_chats'] = chats.count()
        text = chats.find()
        text_count=0
        for i in text:
            text_count+= i['count']
        session['text_count'] = text_count

        return render_template('admin.html')
    test = True
    return render_template('login.html', test = test)


@app.route('/history')
def history():
    if 'username' in session:
        #return 'You are logged in as  :' + session['username']
        chats = mongo.db.chats
        text = chats.find()
        chat=''
        for i in text:
            chat= i['chat']
        session['chat'] = chat
        return render_template('history.html')
    test = True
    return render_template('login.html', test = test)


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    data = ''
    if 'username' in session:
        data =  os.listdir(os.path.join(app.config['UPLOAD_FOLDER'], session['username']))
        #return 'You are logged in as  :' + session['username']
        if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], session['username'], filename))                
                return render_template('upload.html', data=data)
        return render_template('upload.html', data=data)
    return render_template('login.html', data=data)






@app.route('/login')
def login():
    if 'username' in session:
        #return 'You are logged in as  :' + session['username']
        return render_template('index.html')
    test = True
    return render_template('login.html', test = test)


@app.route('/login_check', methods=['POST'])
def login_check():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})
    if login_user:
        if check_password_hash(login_user['password'], request.form['pass']):
            session['username'] = request.form['username']
            return redirect(url_for('login'))
    test = False
    return render_template('login.html', test=test)


@app.route('/register', methods=['POST', 'GET'])
def register():
    test = False
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})
        if existing_user is None:
            os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], request.form['username']))
            hashpass = generate_password_hash(request.form['pass'], method='sha256')
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            test = True
        return render_template('register.html', test=test)
    return render_template('register.html')




@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
    # app.run(host='192.168.132.168', port='5353')






