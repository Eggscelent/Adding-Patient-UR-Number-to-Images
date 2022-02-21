from PIL import Image, ImageDraw, ImageFont
from termcolor import colored
import glob, os, sys
from colorama import init
init()

def checkurlength():
        if len(patient_ur) == 7:
                urtoimage()
        else:
                print(colored("UR number must be 7 numbers... Please try again", "red"))
                exit()

def urtoimage():
        patient_ur_repeat = input("Confirm UR: ")
        if patient_ur == patient_ur_repeat:
                isExist = os.path.exists(path)

                if not isExist:
                        os.makedirs(path)
                        print(colored("The new directory is created!", "green"))

                for img in os.listdir(imageroot + "."):
                        if img.endswith((".jpg", ".png", ".jpeg")):
                                isoimage = Image.open(os.path.join(imageroot, img))
                                draw = ImageDraw.Draw(isoimage)
                                fontsize = 1
                                img_fraction = 0.20
                                print(colored(img, "yellow"))

                                font = ImageFont.truetype("arial.ttf", fontsize)
                                while font.getsize(patient_ur)[0] < img_fraction * isoimage.size[0]:
                                        fontsize += 1
                                        font = ImageFont.truetype("arial.ttf", fontsize)

                                fontsize -= 1
                                font = ImageFont.truetype("arial.ttf", fontsize)

                                x, y = (0, 0)

                                w, h = font.getsize(patient_ur)

                                draw.rectangle((x, y, x + w, y + h), fill="white")
                                draw.text((x, y), patient_ur, fill='black', font=font)

                                isoimage.save(path + "/Edited_" + img)
                                print(colored("UR to Image Successful!", "green"))
                os.system("pause")

        else:
                print(colored("Mismatching patientUR! Please try again...", "red"))
                os.system("pause")

print(colored("URToImage!", "yellow"))
print("-"*100)
print("- This python script was created to simplify the convoluted process of adding UR numbers to images.")
print("- This script only supports .jpg, .jpeg and .png image formats.")
print("- For support or to suggest changes, please email: jackryder1@live.com.au. Thanks and enjoy! ")
print("-"*100)

imageroot = input("Image root folder: ")
patient_ur = input("Patient UR: ")
images = glob.glob(imageroot+r"\*.jpg")
path = (imageroot+"/appended")

checkurlength()
