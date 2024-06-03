class Window:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print('建立Window')
    
    def show(self):
        print(f'({self.x}, {self.y}) 顯示Window')

class MyWindow(Window):
    def __init__(self, x=0, y=0, title="Untitled"):
        super().__init__(x, y)
        self.title = title

    def showTitle(self):
        print(f"我的 title 是：{self.title}")

win1 = Window()
win1.show()

win2 = Window(100, 100)
win2.show()

win3 = MyWindow()
win3.show()