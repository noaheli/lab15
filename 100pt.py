#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
direction = 1
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")



class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Up", background= "green")
		self.button1.grid(row=0,column=1)
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Down", background= "green")
		self.button2.grid(row=1,column=1)
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Left", background= "green")
		self.button3.grid(row=1,column=0)
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="Right", background= "green")
		self.button4.grid(row=1,column=3)
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)
                self.button2.bind("<Button-1>", self.button2Click)
                self.button3.bind("<Button-1>", self.button3Click)
                self.button4.bind("<Button-1>", self.button4Click)
		self.animate()  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		
        def animate(self):
            global drawpad
            global direction
            global target
            global player
            didWeHit = self.collisionDetect()
            x1, y1, x2, y2 = drawpad.coords(target)
            drawpad.move(target, direction, 0)
            if x1 < 0:
                direction = 1
            if x2 > 480:
		direction = -1
            if didWeHit == True:
                return
            else:
                drawpad.after(1, self.animate)
	def button2Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global player
                x1,y1,x2,y2 = drawpad.coords(player)
                if y2 < 320:
                    drawpad.move(player, 0, 20)
		if y2 > 320:
		    return
	def button3Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global player
                x1,y1,x2,y2 = drawpad.coords(player)
		if x1 > 1:
		    drawpad.move(player, -20, 0)
		if x1 < 1:
		    return
	def button4Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global player
                x1,y1,x2,y2 = drawpad.coords(player)
		if x2 < 480:
		    drawpad.move(player, 20, 0)
		if x2 > 480:
		    return
	def button1Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global player
                x1,y1,x2,y2 = drawpad.coords(player)
                if y1 > 20:
                        drawpad.move(player, 0, -20)
		if y1 < 20:
		    return
                    # We made contact! Stop our animation!
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def collisionDetect(self):
                global oval
		global drawpad
		global target
		global player
                x1,y1,x2,y2 = drawpad.coords(player)
                tx1,ty1,tx2,ty2 = drawpad.coords(target)
                if (tx1 < x1 and tx2 > x2) and (ty1 < y1 and ty2 > y2):
                    return True
                else:
                    return False
                # Do your if statement - remember to return True if successful!
       
	    
		
myapp = MyApp(root)

root.mainloop()