class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("make a call")
    def play_game(self):
        print("play a game")

p2=Phone()
p2.set_color("red")
p2.set_cost(10000)
p2.show_color()
p2.show_cost()
p2.make_call()
p2.play_game()


