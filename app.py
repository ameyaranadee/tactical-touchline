from PIL import Image
import os

def resize_images(club_list, target_size=(360, 360)):
    current_folder = os.getcwd()

    for club in club_list:
        file_path = os.path.join(current_folder, f"{club}.png")  # Use the correct file extension here (e.g., .png, .jpg)

        if os.path.exists(file_path):
            try:
                img = Image.open(file_path)
                img_resized = img.resize(target_size, Image.ANTIALIAS)
                img_resized.save(file_path)
                print(f"{club}.png resized successfully.")
            except Exception as e:
                print(f"Error resizing {club}.png: {e}")
        else:
            print(f"{club}.png not found in the current folder.")

if __name__ == "__main__":
    club_list = ['Reims', 'Almería', 'Rayo Vallecano', 'Lecce', 'Toulouse', 'Lille', 'Augsburg', 'Valencia',
                 'Rennes', 'Lens', 'Valladolid', 'Hoffenheim', 'Empoli', 'Angers', 'Montpellier', 'Athletic Club']
    resize_images(club_list)
