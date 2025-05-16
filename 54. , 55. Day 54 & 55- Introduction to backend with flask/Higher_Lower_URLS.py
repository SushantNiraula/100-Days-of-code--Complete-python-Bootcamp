from flask import Flask
import random
app=Flask(__name__)
random_no=random.randint(0,9)
@app.route('/')
def show_user():
    return '''
    <h1>Guess a number between 0 and 9.</h1>
    <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='giphy.gif'>
    '''
@app.route('/<int:user_guess>')
def check_user_guess(user_guess):
    user_guess=int(user_guess)
    if user_guess == random_no:
        return """
        <h1 style='text-align: center; color: green;'>You Found me</h1>\
         <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='giphy.gif'>\
        """
    elif user_guess > random_no:
        return '<h1 style="text-align:center; color: red;">Too High, Try Again</h1> <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return """
        <h1 style="text-align:center; color: blue;>Too Low, Try Again</h1>\
        <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'\
        """


if __name__=='__main__':
    app.run(debug=True)
