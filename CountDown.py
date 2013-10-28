# need to add support for closing the window
# possibly want a get ready sound also
import time
import threading
from Tkinter import *
import tkMessageBox
import winsound

# will record (default) 15 minute sprints with a specified break between each sprint
# will do 3 sprints in a row and then stop

def startTimer ():
  t = ThreadClass()
  t.start()
    
class ThreadClass(threading.Thread):
  def run(self):
    self.breakMins = int(delayString.get())
    self.sprintMins = int(minutesString.get())
    print repr(self.sprintMins)
    self.loops = int(iterationsString.get())
    print repr(self.loops)
    #button.state='disable'
    for i in range(self.loops):
      winsound.PlaySound("start.wav", winsound.SND_FILENAME)
      self.sprint()
      winsound.Playsound('SystemAsterisk', winsound.SND_ALIAS)
      #erase the circle from the screen
      C.delete(ALL)
      #wait the period of the break
      time.sleep(60*self.breakMins)
      
      try:
        winsound.PlaySound("end.wav", winsound.SND_FILENAME)
      except RuntimeError:
        tkMessageBox.showinfo( "Hello Python", "stop")
      '''
      if breakMins < 5:
        time.sleep(60*breakMins)
      else:
        time.sleep(60*breakMins - 120)
        winsound.Playsound('SystemAsterisk', winsound.SND_ALIAS)
        time.sleep(120) '''
    #button.state='enable'
	
#bit broken due to recent changes. Thinking about using gridLayout instead	
  def drawCircle(self, fullness):
    coord = 30, 40, 90, 70
    if fullness == 360:
	  circle = C.create_oval(coord, fill="red")
    else:
	  arc = C.create_arc(coord, start=0, extent=fullness, fill="red")
    C.grid(row=4, rowspan=2)
	
  def sprint(self):
    print repr(self.sprintMins)
    for i in range(1, 7):
  	  time.sleep(self.sprintMins*10)
  	  self.drawCircle(i*60)


#create gui window that will always be on top
top = Tk()
top.wm_attributes("-topmost", 1)
label = Label (top, text="Break time:")
label.grid(row=0)

delayString = StringVar(master=top,value="1")
delay = Entry (top, width=3, textvariable=delayString)
delay.grid(row=0, column=1)

label1 = Label (top, text="Sprint time:")
label1.grid(row=1)

minutesString = StringVar(master=top,value="15")
timeMins = Entry (top, width=3, textvariable=minutesString)
timeMins.grid(row=1, column=1)

label2 = Label (top, text="No of loops:")
label2.grid(row=2)

iterationsString = StringVar(master=top,value="3")
time1 = Entry (top, width=3, textvariable=iterationsString)
time1.grid(row=2, column=1)

button = Button(top, text="Start", command=lambda: startTimer())
button.grid(row=3)
# canvas for to display visualisation of percentage of time elapsed
C = Canvas(top, height=100, width=100)
C.grid(row=4, rowspan=2)
top.mainloop()

