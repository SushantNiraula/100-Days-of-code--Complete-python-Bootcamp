from flask import Flask,render_template
import datetime
import requests
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',year=datetime.datetime.now().year)

@app.route('/guess/<name>')
def guess(name):
    url_genderize=f'https://api.genderize.io/?name={name}'
    url_agify=f'https://api.agify.io/?name={name}'
    response_genderize=requests.get(url_genderize)
    response_agify=requests.get(url_agify)
    data_gender=response_genderize.json()
    data_agify=response_agify.json()
    return render_template('guess.html', name=name,age=data_agify['age'],gender=data_gender['gender'])
@app.route('/blog')
def blog():
    url='https://api.npoint.io/7ec7036ab01725abb41d'
    response=requests.get(url)
    blog_posts=response.json()
    return render_template('blog.html', blog_posts=blog_posts)

if __name__=='__main__':
    app.run(debug=True)