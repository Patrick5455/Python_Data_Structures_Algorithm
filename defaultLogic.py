from datetime import datetime, date


class DefaultSession(object):

    def __init__(self):
        duedate = str(input("Enter Due Date (Year,Month, Day)\n"))
        borrowerid = str(input("Enter issue id\n"))
        self.borrowerid = str(borrowerid)
        self.duedate = datetime.strptime(duedate, '%Y-%m-%d').date()
        self.defaultCount = 0
        self.history = {}

    def _defaultcheck(self):
        if isinstance(self.duedate, date):
            if date.today() > self.duedate:`
                self.defaultCount += 1
                return True
        return False

    def defaulthistory(self):
        if self._defaultcheck():
            self.history[self.borrowerid] = self.defaultCount
            return self.history



patrick = DefaultSession()

print(patrick.defaulthistory())

# if __name__ == "__main__":
#     DefaultSession.defaulthistory()
