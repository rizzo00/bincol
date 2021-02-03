# Bin Collection 

First time building something like this by no means perfect. 

This script scrapes the page to find the next date and bin then disaplying this on a e-paper disaply attached to a pi zero w. 

Currently on the side of my fridge. 

![alt text](https://github.com/rizzo00/bincol/blob/main/bincolimg.png)

Then a cron job to runs on boot and once a day. Seems that the Derby gov site only changes the data on a Sunday. So maybe need to look at further improvement to pull the next day before they refresh. 

I'd like to also get this to be upside down, so the power cable comes out of the top. Seesm a bit tricky with the eink display, I tried but didn't get very far with this.

Credit to [Martin Rothe](https://github.com/mrrothe) for the beauitful soup help. 

Also [link](https://dev.to/ranewallin/getting-started-with-the-waveshare-2-7-epaper-hat-on-raspberry-pi-41m8) which helped me getting this running for some of this code for the eink display.


[Link](
https://www.amazon.co.uk/gp/product/B07Q5PZMGT/ref=ppx_yo_dt_b_asin_image_o06_s00?ie=UTF8&th=1) to the display used
