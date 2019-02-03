import MainMenu


def bezorg():
    return MainMenu.bezorg()
def time1():
    return MainMenu.time1()
def time2():
    return MainMenu.time2()
class Graf:
    def __init__(self):
        self.mainarguments=MainMenu.mainWindow().allargument
    #def main(self):
        #MainMenu.mainWindow()
       # return MainMenu.mainWindow().allargument


if __name__ == "__main__":
    app = Graf()
    print(bezorg())
    #print(app.main)