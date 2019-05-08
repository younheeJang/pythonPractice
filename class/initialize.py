class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User()
user1.initialize("curious", "cu@gmail.com", "1dssd56")

user2 = User()
user2.initialize("jeager", "ri@gmail.com", "ab852ef")


print(user1.email)
print(user2.name)

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


user3 = User("ko", "125@gmail.com", "sadgdg")
user4 = User("fi", "oi@gmail.com", "dhjtrfktf")

print(user3.email)
print(user4.email)