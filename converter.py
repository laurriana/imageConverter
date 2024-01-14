# automation script to convert webp images to png
# for every .webp file in folder, convert to png and delete webp file
import os 
from PIL import Image

# loop
def webpToPng(file):
        if file.endswith(".webp"):
            print(f"converting “{os.path.basename(file)}” to .png...")
            im = Image.open(file).convert("RGB")
            im.save(file.replace('.webp', '.png'), "PNG") 
            os.remove(file)
            print("saved file as .png\n")

def pngToIco(file):
        if file.endswith(".png"):
            print(f"converting “{os.path.basename(file)}” to .ico...")
            im = Image.open(file)
            im.save(file.replace('.png', '.ico'), "ICO")
            os.remove(file)
            print("saved file as .ico\n")
