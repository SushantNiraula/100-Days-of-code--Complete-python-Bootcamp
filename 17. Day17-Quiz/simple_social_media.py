class User:
    def __init__(self,user_id,name):
        self.user_id=user_id
        self.user_name=name
        self.follower=0
        self.following=0
    def follow(self,user):
        user.follower+=1
        self.following+=1
user1=User('001','sushant')
user2=User('002','Sneha')
user1.follow(user2)
print(user1.following)
print(user2.follower)
