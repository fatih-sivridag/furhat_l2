from random import shuffle
from PIL import Image
import os, glob, time
os.chdir("C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Sumeyye_L2")
from psychopy import visual, monitors, core, sys

## Define path to the main folder:
main_folder = "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Sumeyye_L2\\"

## Define the path for images folder so if it changes you change it once here:
image_folder = main_folder + "images\\"
## make a image path maker so that you can use it to make the path to the images easily:
image_path_maker = image_folder + "{name}.jpg"

## Speeches:

redlionfish_speech = "This is a redlionfish. A redlionfish is a type of fish. It is red. It has a long tail."
stapler_speech = "This is a stapler. A stapler is a type of office supply. It is used to staple papers together."

tricycle_speech = "This is a tricycle. A tricycle is a type of vehicle. It has three wheels. It is used by children."
turnip_speech = "This is a turnip. A turnip is a type of vegetable. It is white. It is round."

vulture_speech = "This is a vulture. A vulture is a type of bird. It is black. It has a long neck."
wheelbarrow_speech = "This is a wheelbarrow. A wheelbarrow is a type of vehicle. It is used to carry things."


## Define images as dictionaries which contains the name of the image, path to the image, and image's speech:
redlionfish = {"name": "redlionfish", "path": image_path_maker.format(name="redlionfish"), "speech": redlionfish_speech}
stapler = {"name": "stapler", "path": image_path_maker.format(name="stapler"), "speech": stapler_speech}

tricycle = {"name": "tricycle", "path": image_path_maker.format(name="tricycle"), "speech": tricycle_speech}
turnip = {"name": "turnip", "path": image_path_maker.format(name="turnip"), "speech": turnip_speech}

vulture = {"name": "vulture", "path": image_path_maker.format(name="vulture"), "speech": vulture_speech}
wheelbarrow = {"name": "wheelbarrow", "path": image_path_maker.format(name="wheelbarrow"), "speech": wheelbarrow_speech}

## Make a list of trials so that we can use use them in the experiment easily
## and we can import all of them at once from this file:
## Note that "trials" is a list of lists. Each list contains two items: one for the left image and one for the right image.
trials = [[redlionfish, stapler], [tricycle, turnip], [vulture, wheelbarrow]]

## Define active and passive learning conditions in a list.
## Note that this list has to be the same size as the number of trials.
## We have to define this list so that we have equal number of trials for each condition.
## We will randomize the order of the trials later.
## We make the conditions list in a loop to make sure that we have equal number of trials for each condition.
## and we don't have to write the list manually each time we change the number of trials. But first we have to
## we have to define an empty list to store the conditions in:
conditions = []
for ci in range(len(trials)):
    if ci % 2 == 0:
        conditions.append("active")
    else:
        conditions.append("passive")
