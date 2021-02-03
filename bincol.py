import requests
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup

url='https://secure.derby.gov.uk/binday/Binday?PremisesId=xxxxxxxxxx' # binday/Binday?PremisesId= need to change to the address of the site 

req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")

epd = epd2in13_V2.EPD() # get the display
epd.init(epd.FULL_UPDATE)           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear(0xFF)      # clear the display

def printToDisplay(string):
    HBlackImage = Image.new('1', (epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), 255)

    draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 17) # Create our font, passing in the font file and font size

    draw.text((0, 30), string, font = font, fill = 0)

    epd.display(epd.getbuffer(HBlackImage))

for bin in soup.select('.binresult .mainbintext', limit = 1):
  bindate=bin.find('strong').getText()
  bintype=(bin.getText()).split(":")[1]
  bin = "Next Bin Collection"
  result = os.linesep.join([bin,bindate,bintype])
  printToDisplay(result)


