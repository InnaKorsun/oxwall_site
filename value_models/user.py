class User:
    def __init__(self, username="", password="", real_name="", email="",is_admin=False):
        self.username = username
        self.password = password
        self.real_name = real_name
        self.email = email
        self.is_admin = is_admin



    #def __str__(self):
    #    return "User: username= {}, {}".format(
    #        self.username,
    #        "admin" if self.is_admin else "not admin"
    #    )


if __name__ == "__main__":
    user = User("Masha", "Pupkin")
    print(user)
