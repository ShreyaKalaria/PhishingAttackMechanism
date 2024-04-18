class CapturedData:
    def __init__(self, usrname, passwrd):
        self.username = usrname
        self.password = passwrd
        self.timestamp = get_current_timestamp()
