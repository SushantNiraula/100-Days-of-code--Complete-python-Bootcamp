class User():
    def __init__(self, username):
        self.username= username
        self.is_logged_in=False
    
def is_authenticated_decorator(func):
    def wrapper(*args):
        if args[0].is_logged_in==True:
            return func(args[0])
        else:
            print(f'User {args[0].username} is not logged in. Cannot create blog post.')
            return None
    return wrapper
    
@is_authenticated_decorator
def create_blog_post(user):
    print(f'Blog post created by {user.username}')

new_user = User('John')  
new_user.is_logged_in=False
create_blog_post(new_user)