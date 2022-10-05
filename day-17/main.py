class User:
    def __init__(self, user_id, username):
        print("new user beig created...")
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User('007', 'JB')
# user_1.id = '007'
# user_1.name = 'JB'


print('following :', user_1.following)
print('follower :', user_1.follower)

user_2 = User('00700', 'JP')
user_1.follow(user_2)

print('following :', user_1.following)
print('follower :', user_1.follower)
# user_2.id = '00700'
# user_2.name = 'JP'

print(user_2.username)

