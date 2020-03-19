import os
import gtts
#from mpyg321.mpyg321 import MPyg321Player
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core('hi.png'))

tts= gtts.gTTS(ocr_core('hi.png'))
tts.save('hi.mp3')
#os.system("mpg321 hi.mp3")

#player = MPyg321Player()
#player.play_song("hi.mp3")
