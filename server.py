from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
  title = 'Home Page'
  return render_template('index.html',title=title)

@app.route('/about')
def about():
  title = 'About Page'
  name = 'Alex'
  email = 'std.67122420324@ubru.ac.th'
  mobile = '0610513288'
  age = 21
  return render_template('about.html',title=title,name=name,email=email,mobile=mobile,age=age)

@app.route('/favorite/foods')
def favorite_foods():
  title = 'favoritefoods Page'
  foods = ['ก๋วยเตี๋ยว','ข้าวมันไก่','ปิ้งไก่']

  return render_template('favorite_foods.html',title=title,foods=foods)

@app.route('/favorite/sports')
def favorite_sports():
  title = 'favorite sports Page'
  sports = ['ฟุตบอล','บาสเกตบอล','แบดมินตัน','วิ่งมาราทอน']

  return render_template('favorite_sports.html',title=title,sports=sports)
  
  
