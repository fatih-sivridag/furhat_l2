import os
os.chdir("C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Furhat_conda")
import constants
import glob
import numpy as np
import shutil
################################################################################################
## RESIZE IMAGES for SUMEYYE L2
def resize_pics(pic_name, width, height, path = "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Furhat_conda\\images\\"):
      from PIL import Image
      img = Image.open(path + pic_name + ".jpg")
      img = img.resize((int(width), int(height)), Image.ANTIALIAS)
      img.save(path + pic_name + ".jpg")

image_names = os.listdir("C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Sumeyye_L2\\images\\")
image_names = [i.replace(".jpg", "") for i in image_names]

[resize_pics(i, constants.object_size[0] , constants.object_size[1], path = "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Furhat_conda\\images\\") for i in constants.mountain_dict["familiar_items"]]

###############################################################################################


[resize_pics(i, constants.object_size[0] , constants.object_size[1], path = "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Sumeyye_L2\\images\\") for i in ["red", "green", "purple", "yellow"]]











# [resize_pics(i, constants.pic_width, constants.pic_height) for i in ["capybara", "tapir", "phesant", "yak", "hut", "deer"]]
# resize_pics("furhat_friend", constants.screen_size_pix[0], constants.screen_size_pix[1])

backgrounds = []
[backgrounds.append(i["background"]) for i in constants.item_dicts]
[resize_pics(i, constants.screen_size_pix[0], constants.screen_size_pix[1]) for i in backgrounds]

[shutil.copyfile(("C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Furhat_conda\\images\\"+i+".png"), 
        ("C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Share_with_Nivi\\images_shared\\backgrounds\\"+i+".png")) for i in backgrounds]
[resize_pics(i+"_half", constants.screen_size_pix[0]/2, constants.screen_size_pix[1]) for i in backgrounds]

items = []
[items.append(i["items"]) for i in constants.item_dicts]
[items.append(i["target_items"]) for i in constants.item_dicts]
items = list(np.array(items).flatten())

[shutil.copyfile(("C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Furhat_conda\\images\\"+i+".png"), 
        ("C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Share_with_Nivi\\images_shared\\"+i+".png")) for i in items]
[resize_pics(i, constants.screen_size_pix[0]*0.3 , constants.screen_size_pix[1]*0.3, path = "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Furhat_conda\\images\\question_images\\") for i in items]

[resize_pics(i, constants.object_size[0] , constants.object_size[1], path = "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Furhat_conda\\images\\") for i in ["bobinator", "detainer", "impressioner", "lishi", "tibbe"]]
[resize_pics(i, constants.screen_size_pix[0]* 0.3 , constants.screen_size_pix[1]* 0.3, path = "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Furhat_conda\\images\\question_images\\") for i in ["bobinator", "detainer", "impressioner", "lishi", "tibbe"]]
[resize_pics(i, constants.screen_size_pix[0]* 0.3 , constants.screen_size_pix[1]* 0.3, path = "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Furhat_conda\\images\\question_images\\") for i in ["chiton"]]
resize_pics("white_patch", (constants.object_size[0]+ constants.object_size[0]*0.1) , (constants.object_size[1]+ constants.object_size[0]*0.1))

resize_pics("kardan", constants.object_size[0] , constants.object_size[1], path = "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Furhat_conda\\images\\")
# constants.mountain_dict["familiar_items"  "target_items"]


[resize_pics(i, constants.object_size[0] , constants.object_size[1], path = "C:\\Users\\sivridag\\OneDrive - GWDG\\Projects\\Furhat_language\\Sumeyye_L2\\images\\") for i in image_names]

## Resize Sümeyye's images
