class Instagram:
    def __init__(self,title,description):
     self.title=title
     self.description=description
     self.likes=0
    
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The number of likes on the reel is ",self.likes)
    def like_reel(self):
        self.likes += 1
    def unlike_reel(self):
        if self.likes > 0:
            self.likes -= 1


reel1 = Instagram("My First Reel", "This is a description of my first reel.")
reel1.display_title()
reel1.display_description()
reel1.display_likes()

reel1.like_reel()
reel1.unlike_reel()