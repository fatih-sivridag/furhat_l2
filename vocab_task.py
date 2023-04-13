from psychopy import visual, event, core
import os
os.chdir("C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Sumeyye_L2")
import time, mouse

class Question:
    
    def __init__(self, options = [], path_to_folder= "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Sumeyye_L2\\images\\question_images\\"):
        self.options = options
        self.target = ""
        self.distractors = options[1:3]
        self.pics = [(path_to_folder + i + ".jpg") for i in options]
        self.no = int
        self.desc = ""
        self.story_no = int
        self.story_name = ""

question_1 = Question(options = ["artichoke", "cabbage", "kangaroo", "zebra"])
question_2 = Question(options = ["artichoke", "cabbage", "kangaroo", "zebra"])
question_3 = Question(options = ["octopus", "starfish", "motorcycle", "truck"])
question_4 = Question(options = ["octopus", "starfish", "motorcycle", "truck"])


questions = [question_1, question_2, question_3, question_4]
             #, question_4, question_5, question_6,
             #question_7, question_8, question_9, question_10]


def vocab_break(wait_pic, window, furhat_obj):
    from psychopy import visual, event, core
    import constants
    import random
    import time

    my_mouse = event.Mouse(visible=False, newPos=constants.top_right_corner, win=window)
    wait_stim = visual.ImageStim(win = window, image=wait_pic, pos=(0,0))
    wait_stim.draw()
    window.flip()
    break_start = time.time()
    furhat_obj.say(text = "I am waiting, you can take your time!", blocking = True)
    core.wait(0.5)
    furhat_obj.say(text = "I am waiting, please take your time!", blocking = True)
    my_mouse.setPos(newPos = constants.top_right_corner)

    while True:
        core.wait(0.05)
        if wait_stim.contains(my_mouse):
            break_end = time.time()
            my_mouse.setPos(newPos = constants.top_right_corner)
            break
        else:
            pass
    return break_end - break_start


def ask_question(question, window, furhat_obj, positions = [], used_items = []):
    from psychopy import visual, event, core
    import random
    import time
    import constants
    ## Show four pics for each question

    random.shuffle(positions)
    try:
        question.target = list(set(question.options).intersection(set(used_items)))[0]
        used_items.remove(question.target)
    except IndexError:
        print("An error occured. The question target is not in the used_items list.")
        question.target = question.options[0]

    my_mouse = event.Mouse(visible=False, newPos=None, win=window)

    # Make a dictionary to store the answers and results:
    answer_dict = [question.options[0], question.options[1], question.options[2], question.options[3], question.target]
    
    opt_1= visual.ImageStim(win = window, image=question.pics[0], pos=positions[0])
    opt_2= visual.ImageStim(win = window, image=question.pics[1], pos=positions[1])
    opt_3= visual.ImageStim(win = window, image=question.pics[2], pos=positions[2])
    opt_4= visual.ImageStim(win = window, image=question.pics[3], pos=positions[3])
    [i.draw() for i in [opt_1, opt_2, opt_3, opt_4]]
    window.flip()
    core.wait(0.05)
    my_mouse.setPos(newPos = constants.top_right_corner)
    furhat_obj.say(text = "Which one is {target}".format(target = question.target), blocking = True)
    start_time = time.time()

# TODO: Turn answer_dict into a dictionary

    while True:
        core.wait(0.05)
        if opt_1.contains(my_mouse):
            answer_dict.append(question.options[0])
            answer_dict.append(time.time() - start_time)
            my_mouse.setPos(newPos = constants.top_right_corner)
            core.wait(0.1)
            break
        if opt_2.contains(my_mouse):
            answer_dict.append(question.options[1])
            answer_dict.append(time.time() - start_time)
            my_mouse.setPos(newPos = constants.top_right_corner)
            core.wait(0.1)
            break
        if opt_3.contains(my_mouse):
            answer_dict.append(question.options[2])
            answer_dict.append(time.time() - start_time)
            my_mouse.setPos(newPos = constants.top_right_corner)
            core.wait(0.1)
            break
        if opt_4.contains(my_mouse):
            answer_dict.append(question.options[3])
            answer_dict.append(time.time() - start_time)
            my_mouse.setPos(newPos = constants.top_right_corner)
            core.wait(0.1)
            break
        else:
            pass
        if time.time() - start_time > 10:
            furhat_obj.say(text = random.choice(constants.question_promt).format(target = question.target), blocking = True)
            start_time = time.time() -5
        elif time.time() - start_time > 40:
            #furhat_obj.say(text = furhat_speech.question_timeout, blocking = True)
            answer_dict.append("timeout")
            answer_dict.append(time.time() - start_time)
            break
    
        else:
            pass
    my_mouse.setPos(newPos = constants.top_right_corner)    
    if answer_dict[4] == answer_dict[5]:
        answer_dict.append(1)
    else:
        answer_dict.append(0)

    return answer_dict
