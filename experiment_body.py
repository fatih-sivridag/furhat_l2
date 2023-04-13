from  furhat_remote_api import FurhatRemoteAPI as furhat
import statistics
import csv
## Next two lines are necessary so that Python can find the files we are importing:
import os
os.chdir("C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Sumeyye_L2")
import constants, images, vocab_task
from random import shuffle
import random
from psychopy import visual, monitors, core, sys, gui, event
import time


#####################  ENTER PARTICIPANT INFO  #####################
##################################################################
# Open a dialog box to enter participant info when the experiment starts:
exp_info = {u"id": u""}
# , u"name": u""}
dlg = gui.DlgFromDict(dictionary=exp_info, title="Participant Info")

## Define the Furhat object. Get IP address from constants.py
my_furhat = furhat(constants.furhat_ip)
my_furhat.set_voice(name='Matthew-Neural')
users = my_furhat.get_users()


## Define an empty list to store the selected items:
selected_items = []

## Define an empty dictionary of lists to store the data that will be written to the csv file:
to_data = {
    "trial": [],
    "condition": [],
    "left_image": [],
    "right_image": [],
    "selected_image": [],
    "trial_start": [],
    "trial_end": [],
    "trial_duration": [],
}
## Define path to data file:
data_path = images.main_folder + "data\\sub_" + exp_info["id"] + ".csv"
vocab_path = images.main_folder + "data\\sub_" + exp_info["id"] + "_vocab.csv"

# Randomise the order of conditions:
shuffle(images.conditions)
my_conditions = ["active", "passive"] + images.conditions
## Randomise the order of trials:
shuffle(images.trials)
my_trials = images.training_trials + images.trials

## Define the window for the experiment:
win_1 = visual.Window(fullscr=True,
                    size= constants.screen_size_pix,
                    screen=constants.screen_no,
                    useRetina=True,
                    allowGUI=False,
                    color=(127, 127, 127),
                    colorSpace='rgb255',
                    waitBlanking= False,
                    units='pix')

## Define mouse object:
my_mouse = event.Mouse(visible=False, newPos=constants.top_right_corner, win=win_1)

##### FURHAT GREETS THE PARTICIPANT #####



###### FURHAT GIVES THE INSTRUCTIONS ######


### Participant chooses their colour:
participant_color = constants.choose_color(furhat_object =  my_furhat, win = win_1, mouse= my_mouse, color_list = images.color_list, position= constants.question_positions)
print(participant_color)
### EXPERIMENT STARTS ###

## Start trials:
## Note that we use a loop to go through each trial. Each iteration of the loop is a trial.
## In each trial we show two pictures and either ask the user to choose one of them (active trials) or
## Furhat chooses one of them (passive trials) and then talk about it:
for ti in range(len(my_trials)):
    # Randomise the order of locations in each trial:
    shuffle(constants.positions)
    # Get the current trial:
    current_trial = my_trials[ti]

    ## Determine which image is on the left and which is on the right after randomisation:
    if constants.positions[0] == constants.pos_left:
            left_image = current_trial[0]
            right_image = current_trial[1]
            image_1 = visual.ImageStim(win=win_1, image=left_image["path"], pos=constants.positions[0])
            image_2 = visual.ImageStim(win=win_1, image=right_image["path"], pos=constants.positions[1])
            trial_images = [left_image, right_image]
    else:
            left_image = current_trial[1]
            right_image = current_trial[0]
            image_1 = visual.ImageStim(win=win_1, image=left_image["path"], pos=constants.positions[1])
            image_2 = visual.ImageStim(win=win_1, image=right_image["path"], pos=constants.positions[0])
            trial_images = [right_image, left_image]
    ## Add the names of the images which appear on the left and right to the data dictionary:
    to_data["left_image"].append(left_image["name"])
    to_data["right_image"].append(right_image["name"])

    ## Add trial number and condition to the data dictionary:
    to_data["trial"].append(ti + 1)
    to_data["condition"].append(my_conditions[ti])               

    ##Set the mouse position to the top right corner of the screen:
    my_mouse.setPos(newPos = constants.top_right_corner)

    # Show the two images on the screen:
   # image_1 = visual.ImageStim(win=win_1, image=trial_images[0]["path"], pos=constants.positions[0])
   # image_2 = visual.ImageStim(win=win_1, image=trial_images[1]["path"], pos=constants.positions[1])
    image_1.draw()
    image_2.draw()
    core.wait(0.1)

    ## Save the time when the trial starts:
    print(my_conditions[ti])
    
    if my_conditions[ti] == "active":
        ## Furhat says the instructions for active trials:

        ## Show pictures on the screen:
        win_1.flip()
        core.wait(0.1)
        to_data["trial_start"].append(time.time())
        ## Furhat gives instructions at the beginning of each trial.
        ## If it is the first or second trial, it gives instructions for the training trials:
        my_furhat.set_led(red=participant_color[0], green=participant_color[1], blue=participant_color[2])
        if ti < 2:
             my_furhat.say(text="This is the training trial! Please select one of the images by clicking on it.", blocking=True)
        else:
             my_furhat.say(text="Now it is your turn! Which picture do you want to talk about? Tap on one of the pictures.", blocking=True)
        
        

        ## Wait until the user clicks on one of the images:
        while True:
            core.wait(0.05)
            if image_1.contains(my_mouse):
                # furhat attends to the left of the screen:
                my_furhat.attend(location = constants.furhat_left)
                ## Furhat speaks about the selected image:
                my_furhat.say(text=left_image["speech"], blocking=True)
                ## furhat attends back to the participant:
                my_furhat.attend(user = "CLOSEST")
                ## Save selected item into selected item list:
                selected_items.append(left_image["name"])
                ## Save selected item and trial end time to the data dictionary:
                to_data["selected_image"].append(left_image["name"])
                to_data["trial_end"].append(time.time())
                break
            elif image_2.contains(my_mouse):
                # furhat attends to the right of the screen:
                my_furhat.attend(location = constants.furhat_right)
                # Furhat speaks about the selected image:
                my_furhat.say(text=right_image["speech"], blocking=True)
                ## furhat attends back to the participant:
                my_furhat.attend(user = "CLOSEST")
                ## Save selected item into selected item list:
                selected_items.append(right_image["name"])
                # Save selected item and trial end time to the data dictionary:
                to_data["selected_image"].append(right_image["name"])
                to_data["trial_end"].append(time.time())
                break
            else:
                pass
    ## If the condition is passive:
    ##Set the mouse position to the top right corner of the screen:
        my_mouse.setPos(newPos = constants.top_right_corner)
    else:
        
        win_1.flip()
        ## Furhat says the instructions for passive trials: Give more instructions for the first two trials (training trials):
        ## Furhat gives instructions at the beginning of each trial.
        ## If it is the first or second trial, it gives instructions for the training trials:
        ## Furhat sets light to show whuse turn it is
        my_furhat.set_led(red=0, green=255, blue=0)
        if ti < 2:
            my_furhat.say(text=" This is the training trial! Please wait while I select one of the images.", blocking=True)
        else:
             my_furhat.say(text="Now it is my turn. I will look at the pictures and choose one.", blocking=True)
        ## Show pictures on the screen:
        
        to_data["trial_start"].append(time.time())
        
        

        ## furhat looks at the images for random amount of time:
        ## It changes gaze 2 or 3 times and look at the right, middle or left of the screen
        ## Random choice of gaze and gaze duratins are weighted to make the gaze more natural
        num_looks = random.choice([2,3])
        for i in range(num_looks):
            loc_gaze = random.choices([constants.furhat_left, constants.furhat_middle, constants.furhat_right], weights=[3,0.5,3], k= 1)[0]
            dur_gaze = random.choices([1, 1.4, 1.8], weights=[5,6,7], k= 1)[0]
            my_furhat.attend(location = loc_gaze)
            time.sleep(dur_gaze)
        ## After the last gaze, furhat chooses one of the images:
            # Choose one number between 0 and 9:
            # If it is even, furhat chooses the left image:
            # else it chooses the right image:
        if(random.randint(0,9) % 2 == 0):
            my_furhat.attend(location = constants.furhat_left)
            time.sleep(1)
            my_furhat.say(text=left_image["speech"], blocking = True)
            ## furhat attends back to the participant:
            my_furhat.attend(user = "CLOSEST")
            # Save selected item into selected item list:
            selected_items.append(left_image["name"])
            # Save selected item and trial end time to the data dictionary:
            to_data["selected_image"].append(left_image["name"])
            to_data["trial_end"].append(time.time())
        else:
            my_furhat.attend(location = constants.furhat_right)
            time.sleep(1)
            my_furhat.say(text=right_image["speech"], blocking = True)
            ## furhat attends back to the participant:
            my_furhat.attend(user = "CLOSEST")
            # Save selected item into selected item list:
            selected_items.append(right_image["name"])
            # Save selected item and trial end time to the data dictionary:
            to_data["selected_image"].append(right_image["name"])
            to_data["trial_end"].append(time.time())

    ## Add trial duration to the data dictionary:
    my_furhat.set_led(red=0, green=0, blue=0)
    core.wait(0.5)
    my_furhat.attend(user = "CLOSEST")
    core.wait(1)
    to_data["trial_duration"].append(to_data["trial_end"][ti] - to_data["trial_start"][ti])


## Save data file as a csv file:
#data_file = open(data_path, "w")
#data_writer = csv.DictWriter(data_file, fieldnames=to_data.keys())
#data_writer.writeheader()
#data_writer.writerow(to_data)
#data_file.close()


################ VOCAB TASK ###############
print("vocabulary task is beginning!!!!!!!!!!!")
print("the content of seleceted list is: {selected}".format(selected = selected_items))
wait_dur = vocab_task.vocab_break(wait_pic = images.wait_pic, window = win_1, furhat_obj = my_furhat)

print("The subject waited {wait} before starting vocabulary task!".format(wait =  wait_dur))
my_answers = []
for my_question in vocab_task.questions:
    my_answers.append(vocab_task.ask_question(question = my_question, window = win_1, furhat_obj = my_furhat, positions = constants.question_positions, used_items = selected_items))

with open(vocab_path, "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(["opt_1", "opt_2", "opt_3", "opt_4", "target", "selected", "response_time", "is_correct"])
    writer.writerows(my_answers)

with open(data_path, "w", newline = "") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(to_data.keys())
    writer.writerows(zip(*to_data.values()))



#### TASK ENDED
## FURHAT SAYS THANK YOU AND GOODBYE


sys.exit()