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

color_list = [image_path_maker.format(name = "red"), image_path_maker.format(name = "yellow"), image_path_maker.format(name = "green"), image_path_maker.format(name = "purple")]

wait_pic = image_folder + "green_tick.png"
## Speeches:
#Familiar vocabulary:
artichoke_speech = "This is an artichoke. An artichoke is a type of vegetable. It has thick green leaves and it looks like a flower. Artichoke has lots of vitamins."
cabbage_speech = "This is a cabbage. A cabbage is a type of vegetable. It is green or purple. Cabbage is very healthy."

kangaroo_speech = "This is a kangaroo. A kangaroo is a type of animal. It has powerful legs and a long strong tail. Kangaroos get around by hopping on their back legs."
zebra_speech = "This is a zebra. A zebra is a type of animal. It has black and white stripes around its body. Zebras live in different parts of Africa. "

octopus_speech = "This is an octopus. An octopus is a type of sea animal. It has eight long arms. An octopus can change its color to communicate with other octopuses."
starfish_speech = "This is a starfish. A starfish is a type of sea animal. It has five arms and it looks like a star. A starfish cannot swim, but it is good at crawling."

motorcycle_speech = "This is a motorcycle. A motorcycle is a type of vehicle. It has two wheels and en engine. Motorcycle is bigger and faster than bicycles."
truck_speech = "This is a truck. A truck is a type of vehicle. It has at least four wheels and a strong engine. Truck are used to transport heavy things."


#Target vocabulary:
tricycle_speech = "This is a tricycle. A tricycle is a type of vehicle. It has three wheels. It is used by children."
wheelbarrow_speech = "This is a wheelbarrow. A wheelbarrow is a type of vehicle. It is used to carry things."

rambutan_speech = "This is rambutan. A rambutan is a type of fruit. It is hairy and red. Rambutan is very sweet."
tamarind_speech = "This is tamarind. A tamarind is a type of exotic fruit. It is brown and it has bean-like pods. Tamarind is sour and has lots of vitamins."

broom_speech = "This is a broom. A broom is a type of cleaning tool. Broom is used to sweep and clean the floors."
drill_speech = "This is a drill. A drill is a type of electrical tool. Drill is used to make holes in a material, for example in a wall or in wood."

pacifier_speech = "This is a pacifier. A pacifier is an object for babies. Pacifier is made from plastic and silicon."
stapler_speech = "This is a stapler. A stapler is a type of office supply. It is used to staple papers together."

tambourine_speech = "This is a tambourine. A tambourine is a music instrument. It has small jiggles around. Tambourine makes sound when it is shaken."
sewingmachine_speech = "This is a sewing machine. A sewing machine is a tool to stich fabric. Sewing machines are used to make clothes, towels, pillowcases etc."

badger_speech = "This is a badger. A badger is a type of animal. It has black, brown, and white hairs. Badgers have a long body and short legs."
platypus_speech = "This is a platypus. A platypus is a type of animal. It has a flat body and very short legs. Platypus is a good swimmer."

peacock_speech = "This is a peacock. A peacock is a type of bird. It has blue and green fur and colorful tail feathers. Male peacock's colorful tail spreads like a fan."
dragonfly_speech = "This is a dragonfly. A dragonfly is a type of insect. It has large eyes and transparent wings. Dragonfly has six legs but it cannot walk."

muskox_speech = "This is a musk ox. A musk ox is a type of large animal. It has thick brown or black fur. Musk ox lives in very cold regions in the arctics."
porcupine_speech = "This is a porcupine. A porcupine is a type of animal. It has black, brown, or white sharp spines around its body. Porcupines are large and very slow."

lobster_speech = "This is a lobster. A lobster is a type of sea animal. It has ten legs and two large claws. Lobster lives in salt water, such as in seas and oceans."
squid_speech = "This is a squid. A squid is a type of sea animal. It has a long, tube-shaped body with a short head. Squid can change its color to confuse its enemies."

rake_speech = "This is a rake. A rake is a type of gardening tool. It has a long handle and many sharp metal or wooden points. Rake is used to loosen the soil, or to collect and remove leaves from the ground."
trowel_speech = "This is a trowel. A trowel is a type of gardening tool. It has a short handle and a flat pointed or scoop-shaped metal blade. Trowel is used to dig the soil, or to spread material on a surface."



## Define images as dictionaries which contains the name of the image, path to the image, and image's speech:
artichoke = {"name": "artichoke", "path": image_path_maker.format(name="artichoke"), "speech": artichoke_speech}
cabbage = {"name": "cabbage", "path": image_path_maker.format(name="cabbage"), "speech": cabbage_speech}

kangaroo = {"name": "kangaroo", "path": image_path_maker.format(name="kangaroo"), "speech": kangaroo_speech}
zebra = {"name": "zebra", "path": image_path_maker.format(name="zebra"), "speech": zebra_speech}

octopus = {"name": "octopus", "path": image_path_maker.format(name="octopus"), "speech": octopus_speech}
starfish = {"name": "starfish", "path": image_path_maker.format(name="starfish"), "speech": starfish_speech}

motorcycle = {"name": "motorcycle", "path": image_path_maker.format(name="motorcycle"), "speech": motorcycle_speech}
truck = {"name": "truck", "path": image_path_maker.format(name="truck"), "speech": truck_speech}

tricycle = {"name": "tricycle", "path": image_path_maker.format(name="tricycle"), "speech": tricycle_speech}
wheelbarrow = {"name": "wheelbarrow", "path": image_path_maker.format(name="wheelbarrow"), "speech": wheelbarrow_speech}

rambutan = {"name": "rambutan", "path": image_path_maker.format(name="rambutan"), "speech": rambutan_speech}
tamarind = {"name": "tamarind", "path": image_path_maker.format(name="tamarind"), "speech": tamarind_speech}

broom = {"name": "broom", "path": image_path_maker.format(name="broom"), "speech": broom_speech}
drill = {"name": "drill", "path": image_path_maker.format(name="drill"), "speech": drill_speech}

pacifier = {"name": "pacifier", "path": image_path_maker.format(name="pacifier"), "speech": pacifier_speech}
stapler = {"name": "stapler", "path": image_path_maker.format(name="stapler"), "speech": stapler_speech}

tambourine = {"name": "tambourine", "path": image_path_maker.format(name="tambourine"), "speech": tambourine_speech}
sewingmachine = {"name": "sewingmachine", "path": image_path_maker.format(name="sewingmachine"), "speech": sewingmachine_speech}

badger = {"name": "badger", "path": image_path_maker.format(name="badger"), "speech": badger_speech}
platypus = {"name": "platypus", "path": image_path_maker.format(name="platypus"), "speech": platypus_speech}

peacock = {"name": "peacock", "path": image_path_maker.format(name="peacock"), "speech": peacock_speech}
dragonfly = {"name": "dragonfly", "path": image_path_maker.format(name="dragonfly"), "speech": dragonfly_speech}

muskox = {"name": "muskox", "path": image_path_maker.format(name="muskox"), "speech": muskox_speech}
porcupine = {"name": "porcupine", "path": image_path_maker.format(name="porcupine"), "speech": porcupine_speech}

lobster = {"name": "lobster", "path": image_path_maker.format(name="lobster"), "speech": lobster_speech}
squid = {"name": "squid", "path": image_path_maker.format(name="squid"), "speech": squid_speech}

rake = {"name": "rake", "path": image_path_maker.format(name="rake"), "speech": rake_speech}
trowel = {"name": "trowel", "path": image_path_maker.format(name="trowel"), "speech": trowel_speech}


## Make a list of trials so that we can use use them in the experiment easily
## and we can import all of them at once from this file:
## Note that "trials" is a list of lists. Each list contains two items: one for the left image and one for the right image.
training_trials = [[kangaroo, zebra], [octopus, starfish]]
trials = [[artichoke, cabbage], [motorcycle, truck]]
          #, [tricycle, wheelbarrow], [rambutan, tamarind]]
          #, [broom, drill], [pacifier, stapler], [tambourine, sewingmachine], [badger, platypus], [peacock, dragonfly], [muskox, porcupine], [lobster, squid], [rake, trowel]]

## Define active and passive learning conditions in a list.

# passive = [[kangaroo, zebra], [motorcycle, truck], [rambutan, tamarind], [broom, drill], [badger, platypus], [lobster, squid], [rake, trowel]]
# active = [[artichoke, cabbage], [octopus, starfish], [tricycle, wheelbarrow], [pacifier, stapler], [tambourine, sewingmachine], [peacock, dragonfly], [muskox, porcupine]]


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
