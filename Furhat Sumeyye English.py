import psychopy
from furhat_remote_api import FurhatRemoteAPI as furhat
import time
from psychopy import visual, monitors, core, sys, gui, event




my_furhat = furhat("192.168.137.38")
my_furhat.furhat_gestures_get()
my_furhat.furhat_voices_get()
 
my_furhat.say(text = "Hi there!", blocking= True)
my_furhat.gesture(name="Blink")
my_furhat.say(text = "It is nice to meet you!", blocking=True)
my_furhat.gesture(name="Smile")
my_furhat.say(text="My name is Furhat. I am a robot that can do many things.", blocking= True)
my_furhat.listen()
my_furhat.say(text="I am here today to show you who I am and what I can do. I want to show you my skills!", blocking= True)
core.wait(0.5)
my_furhat.gesture(name="BigSmile")
core.wait(0.5)
my_furhat.say(text="Do you want to see my skills?", blocking=True)
my_furhat.gesture(name="Wink")
answer= my_furhat.listen()
print(str(answer.message))
if "ready" in answer.message or "yes" in answer.message:
    my_furhat.say(text="Okay, let me show you what I can do", blocking= True)
    my_furhat.gesture(name="BigSmile")
    time.sleep(1.5)
else: 
    my_furhat.say(text="I am waiting for you to say yes. Take your time.", blocking= True)
    answer= my_furhat.listen()
    my_furhat.say(text="Okay let me show you what I can do", blocking= True)
    my_furhat.gesture(name="Smile")
my_furhat.gesture(name="BigSmile")

#Showing skills, colors, pictures, voice, language etc.

#Change the appearance:
my_furhat.say(text="Great, look at this!")
my_furhat.gesture(name="BigSmile")
my_furhat.say(text="I can change my face, for example I can wear make up." blocking= True)
my_furhat.set_face(character="Isabel", mask= "FaceCore")
core.wait(3)
my_furhat.set_face(character="Jane", mask= "FaceCore")
core.wait(3)
my_furhat.say(text="I can also look like a machine", blocking= True)
my_furhat.set_face(character= "Titan", mask= "FaceCore")
core.wait(3)
my_furhat.say(text="Or like an alien!", blocking= True)
my_furhat.set_face(character="Plavalunga", mask= "FaceCore")
core.wait(3)
my_furhat.set_face(character="Samuel", mask= "FaceCore")
core.wait(2)

#Change the voice
my_furhat.say(text="I can also change my voice.", blocking= True)
my_furhat.set_voice(name= 'Andreas22k_HQ')
core.wait(0.6)
my_furhat.say(text= "I can sound like this", blocking= True)
core.wait(0.6)
my_furhat.set_voice(name= 'Claudia22k_HQ')
core.wait(0.6)
my_furhat.say(text= "or like this", blocking= True)
core.wait(0.6)
my_furhat.set_voice(name= 'Vicki-Neural')
core.wait(0.6)
my_furhat.say(text="And how about this?", blocking= True)

#Change language
my_furhat.say(text="I can also speak many languages.", blocking= True)
my_furhat.set_voice(name= 'Emma-Neural')
core.wait(0.6)
my_furhat.say(text= "For example, I can speak English very well.", blocking= True)
core.wait(0.6)
my_furhat.say(text= "Ich kann auch auf Deutsch reden." blocking= True)
core.wait(0.6)
my_furhat.set_voice(name='Lucia-Neural')
core.wait(0.6)
my_furhat.say(text= "El espanol es como me lengua materna.", blocking= True)
core.wait(0.6)
my_furhat.set_voice(name='Lea-Neural')
my_furhat.say(text="Türkce de konusabilirim.", blocking= True)
core.wait(0.6)

#Change the light
#First define the color dictionary:
color_dict = {"red": (255, 0, 0),
              "green": (0, 255, 0),
              "blue": (0, 0, 255),
              "yellow": (255, 255, 0),
              "orange": (255, 165, 0),
              "purple": (128, 0, 128),
              "pink": (255, 192, 203),
              "brown": (165, 42, 42),
              "black": (0, 0, 0),
              "white": (255, 255, 255)}

my_furhat.say(text= "I can also change the color of my lights." blocking= True)
for i in [[0,0,0], [123, 0, 0] ,[255,0,0], [0, 123, 0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255], [255,255,255]]:
    print(i)
    my_furhat.set_led(red= i[0], green = i[1], blue = i[2])
    core.wait(0.9)
my_furhat.set_led(red= 0, green= 0, blue= 0)
#my_furhat.say(text="Tell me your favorite color.", blocking= True)
#my_furhat.listen()

#show some stuff in the screen
my_furhat.say(text="I can also use the screen in front of me to show you pictures." blocking=True)
my_furhat.gesture(name="BigSmile")
my_furhat.say(text="For example, here I have a picture of a cute cat! How sweet!" blocking=True)
visual.ImageStim(win= win_1, image= cat_pic.path, pos = (0,0)).draw()
win_1.flip()
core.wait(0.2)
my_furhat.gesture(name="Smile")
my_furhat.say(text="Or look at this, what a cute dog!" blocking= True)
visual.ImageStim(win= win_1, image= dog_pic.path, pos = (0,0)).draw()
win_1.flip()
core.wait(0.2)
my_furhat.gesture(name="BigSmile")
my_furhat.say(text="And here there is me with a friend, maybe we will meet on the weekend." blocking= True)
visual.ImageStim(win= win_1, image= furhat_pic.path, pos = (0,0)).draw()
win_1.flip()
core.wait(0.2)
my_furhat.gesture(name="Wink")


#Trials start

my_furhat.say(text="I can also show you some other pictures on the screen and we can play a game together." blocking= True)
my_furhat.gesture(name="Wink")
my_furhat.say(text="So, would you like to play a game with me now? Say yes if you want to." blocking= True)
answer= my_furhat.listen()
print(str(answer.message))
if "ready" in answer.message or "yes" in answer.message:
    my_furhat.say(text="Perfect, let's do this!", blocking= True)
    my_furhat.gesture(name="BigSmile")
    time.sleep(1.5)
else: 
    my_furhat.say(text="I am waiting for you to say yes. Take your time.", blocking= True)
    answer= my_furhat.listen()
    my_furhat.say(text="Perfect, let's do this!", blocking= True)
    my_furhat.gesture(name="Smile")
my_furhat.gesture(name="BigSmile")

my_furhat.say(text="Now you will see two pictures on the screen. When it is my turn, I will choose which one to talk about, and when it is your turn, you will choose." blocking= True)
my_furhat.gesture(name="Smile")

#Two pictures on the screen appear. 

my_furhat.say(text="Let’s start with you, tap on the picture that you want me to tell you about.")

#Tapped on the image: This is a starfish….
#Not tapped after 10 seconds: 
my_furhat.say(text="Take your time, I am waiting for you to choose which one you want me to tell you about Tap on the picture you want.” blocking= True)
#Child chooses one, and the robot speaks about it. “This is an octopus.”
#New pictures appear, 
my_furhat.say(text="Now it's my turn." blocking=True)
#Robot talks about one of the pictures: This is a …”
#We do this for 2 times for the child to learn, and then 10 rounds with 20 pictures. 
#When these end, we start the assessment part. 

#After the trial ends…
my_furhat.say(text="You did a great job! Let’s rest for a moment. Tap on the star to continue playing with me!" blocking=True)

#We give 4 pictures in each assessment part, and robot tells one word for the child to choose.

#Choose the correct image! 



def instructions(my_furhat):
    from psychopy import core
    my_furhat.say(text="You will see some objects on the screen.", blocking= True)
    core.wait(0.5)
    my_furhat.say(text="When it is my turn, I will choose which one to talk about", blocking= True)
    core.wait(0.5)
    my_furhat.gesture(name="Smile")
    my_furhat.say(text="When it is your turn, you can choose which one to talk about. You can click on the picture you want.", blocking=True)
    core.wait(0.5)
    my_furhat.say(text="At the end, we will play a memory game. I will show you some pictures and you will tap on the picture that I say the name of.", blocking=True)
    core.wait(0.5)
    return None
 
instructions(my_furhat)

## Defining monitor and related values (screen size in pixels)
mon= monitors.getAllMonitors()[0]
my_mon= monitors.Monitor(mon)
# my_mon.setSizePix()
my_mon.saveMon()
win_width = my_mon.getSizePix()[0]
win_height = my_mon.getSizePix()[1]

#redlion_pic = images.Pic (name= "redlionfish")
#tricycle_pic = images.Pic (name= "tricycle")


#Defining window
win_1= visual.Window(fullscr=True, 
                     size= [1920, 1080], 
                     screen= 1, useRetina= True, 
                     allowGUI= False,
                      color= (127, 127, 127),
                       colorSpace= 'rgb255',
                        waitBlanking= False,
                         units= 'pix' )

#Showing pictures on the screen
my_furhat.say(text="I can also use the screen in front of you to show you some pictures.", blocking= True)
visual.ImageStim(win= win_1, image= "/Users/sumeyyeoktay/Desktop/Thesis material/experiment possible items/redlionfish.jpg", pos=(0,0)).draw()
core.wait(0.3)
win_1.flip()
core.wait(3)
visual.ImageStim(win= win_1, image= "/Users/sumeyyeoktay/Desktop/Thesis material/experiment possible items/tricycle.jpg", pos=(0,0)).draw()
core.wait(0.3)
win_1.flip()
core.wait(3)
visual.ImageStim(win= win_1, image="/Users/sumeyyeoktay/Desktop/Thesis material/experiment possible items/rubikcube.jpg", pos=(0, 0)).draw()
core.wait(0.3)
win_1.flip()
core.wait(3)



#mouse
my_mouse= event.Mouse(visible=True, newPos= (0, 0), win=win_1)




    
#event.waitKeys





core.wait(10)
sys.exit()