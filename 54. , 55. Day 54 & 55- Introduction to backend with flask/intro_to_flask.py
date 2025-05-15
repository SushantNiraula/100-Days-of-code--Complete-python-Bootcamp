from flask import Flask
app=Flask(__name__)
def make_bold(func):
    def wrapper():
        return f'<b>{func()}<b>'
    return wrapper
def make_italic(func):
    def wrapper():
        return f'<i>{func()}<i>'
    return wrapper
def make_underline(func):
    def wrapper():
        return f'<u>{func()}<u>'
    return wrapper


@app.route('/')
def hello_world():
    return '<h1>Hello, World! How are you my boi !</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

# Creating a variable path
@app.route('/username/<name>')
def username(name):
    return f'<h1>Hello, {name}!</h1>'

## Rendering HTML in Flask
@app.route('/html')
def html():
    return '''
    <html>
        <head>
            <title>My First HTML Page</title>
        </head>
        <body>
            <h1 style="text-align:center">Hello, World!</h1>
            <p style="text-align: center ; color:red">This is my first HTML page in Flask.</p>
            <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWRyanF1aHoxeDVybG14Y3kzeWFzcWF2N3htYzdzM21teDN4a3ZvdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZcXbJQxHb5YsS2qid3/giphy.gif" alt="Flask Image" style="display: block; margin: 0 auto;">
        </body>
    </html>
    '''
@app.route('/bold')
@make_bold
@make_italic
@make_underline
def bold_italic_underline():
    return 'This is a bold, italic, underlined text!'

if __name__=='__main__':
    app.run(debug=True)