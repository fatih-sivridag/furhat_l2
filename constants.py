import os
os.chdir("C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Sumeyye_L2")
from psychopy import visual, event, core

## Write the IP number of the Furhat that you are using:
#furhat_ip = "127.0.0.1"
# furhat_ip = "192.168.43.62"
# furhat_ip = "134.76.136.30"
#furhat_ip = "192.168.43.184"
furhat_ip = "192.168.137.38"

## Define sreen info here so that you change it once and it is used everywhere:
screen_no = 1 ## which screen to use if multiple screens are connected
screen_size_pix = (1920, 1080)

## Left and right positions for the stimuli. They are relative to the screen size;
## so if you change the screen you only change the screen_size_pix variable above.
pos_left = (-screen_size_pix[0]/2+0.25*screen_size_pix[0], 0)
pos_right = (screen_size_pix[0]/2-0.25*screen_size_pix[0], 0)
# Put the positions into list so that we can import boht of them at the same time and shuffle them for randomization:
positions = [pos_left, pos_right]

## Attention positions for Furhat. Defining them here to keep the other file clean.
furhat_left = "-0.4, -0.8, 1.0"
furhat_right = "0.4, -0.8, 1.0"
furhat_middle = "0, -0.8, 1.0"

top_right_corner = [screen_size_pix[0]/2, screen_size_pix[1]/2]

object_size = (0.3*screen_size_pix[0], 0.3*screen_size_pix[1])

top_left_screen = (-screen_size_pix[0]/2 + screen_size_pix[0]*0.25, screen_size_pix[1]/2-screen_size_pix[1]*0.25)
top_right_screen = (screen_size_pix[0]/2 - screen_size_pix[0]*0.25, screen_size_pix[1]/2-screen_size_pix[1]*0.25)
bottom_left_screen = (-screen_size_pix[0]/2 + screen_size_pix[0]*0.25, -screen_size_pix[1]/2+screen_size_pix[1]*0.25)
bottom_right_screen = (screen_size_pix[0]/2 - screen_size_pix[0]*0.25, -screen_size_pix[1]/2+screen_size_pix[1]*0.25)
object_positions = [pos_left, pos_right]
question_positions = [top_left_screen, top_right_screen, bottom_left_screen, bottom_right_screen]

## Add a few more variations of the prompt here:
question_promt = ["Which one is the {target}?"]



def choose_color( win, color_list, mouse, furhat_object, position):
    red_img = visual.ImageStim(win=win, image= color_list[0], pos=position[0])
    yellow_img = visual.ImageStim(win=win, image= color_list[1], pos=position[1])
    green_img = visual.ImageStim(win=win, image= color_list[2], pos=position[2])
    purple_img = visual.ImageStim(win=win, image= color_list[3], pos=position[3])

    mouse.setPos(newPos = (540, 860))

    [i.draw() for i in [red_img, yellow_img, green_img, purple_img]]
    win.flip()
    furhat_object.say(text = "Choose your color", blocking = True)

    while True:
        core.wait(0.1)
        if red_img.contains(mouse):
            rgb_chosen = [255, 0, 0]
            furhat_object.set_led(red = rgb_chosen[0], green = rgb_chosen[1], blue = rgb_chosen[2])
            break
        elif yellow_img.contains(mouse):
            rgb_chosen = [255, 255, 0]
            furhat_object.set_led(red = rgb_chosen[0], green = rgb_chosen[1], blue = rgb_chosen[2])
            break
        elif green_img.contains(mouse):
            rgb_chosen = [0, 255, 0]
            furhat_object.set_led(red = rgb_chosen[0], green = rgb_chosen[1], blue = rgb_chosen[2])
            break
        elif purple_img.contains(mouse):
            rgb_chosen = [255, 0, 255]
            furhat_object.set_led(red = rgb_chosen[0], green = rgb_chosen[1], blue = rgb_chosen[2])
            break
        
    return rgb_chosen





