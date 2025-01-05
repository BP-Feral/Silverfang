import requests
from PIL import Image

saved_images = 0

# read champion names
with open('utils/champions.txt') as f:
    d = f.readlines()
    for i in d:
        champ_name = str(i).strip()
        url = "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/champion/" + champ_name + ".png"
        file_name = champ_name

        # Request the image from the URL
        res = requests.get(url, stream=True)

        if res.status_code == 200:
            # Open the image using PIL after downloading
            img = Image.open(res.raw)

            # Resize the image to 512x512 (used for Discord Activity)
            img_resized = img.resize((512, 512))

            # Save the resized image
            img_resized.save(f"utils/champs/lol_{file_name}.png")

            saved_images += 1

print(f"Saved {saved_images} images.") # 169 total images as of patch 14.24
