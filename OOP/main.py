# Task 1
class Backpack:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False
    
    def openBag(self):
        self.open = True
        print("backpack is open")
        
    def closeBag(self):
        self.open = False
        print("backpack is closed")
        
    def putIn(self, item):
        if self.open:
            self.items.append(item)
            print(f"{item} added to backpack")
        else:
            print("backpack is closed, open it first.")
            
    def takeout(self, item):
        if self.open:
            if item in self.items:
                self.items.remove(item)
                print(f"{item} removed from the backpack.")
            else:
                print(f"{item} not in the backpack.")
        else:
            print("backpack is closed, open it first.")

# Task 2
small_blue_backpack = Backpack("blue", "small")
medium_red_backpack = Backpack("red", "medium")
large_green_backpack = Backpack("green", "large")

# Task 3
small_blue_backpack.openBag()
small_blue_backpack.putIn("apple")
small_blue_backpack.putIn("hoodie")
small_blue_backpack.closeBag()
small_blue_backpack.openBag()
small_blue_backpack.takeout("hoodie")
small_blue_backpack.closeBag()