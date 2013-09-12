# Wallbase Wallpaper Cycle 


**NOTE:** The following dependencies must be installed:
- **feh** - (apt-get install feh ... etc.) - [Feh](https://github.com/derf/feh)
- **PhantomJS** - needs Webdriver Support (1.92 and above) - [PhantomJS](http://phantomjs.org)
- **Selenium** - Python Webdriver (pip install selenium) - [Selenium](https://pypi.python.org/pypi/selenium)

## Description: 
This is an wallpaper changer, it pulls random wallpapers from ([Wallbase](http://wallbase.cc)) and displays them on your desktop.
Another part of the script is to save all wallpapers found under the current directory "./walls"

---
## Usage:
To run, simply run the python file included like so: ```python wallpaper_cycle.py```

---
#### @TODO:
- Doesn't cycle forever.... (Change Count / While True)
- Needs arguments for file saving & interval etc.
- Faster solution for grabbing images, currently this is being limited by browsing speed.
- Small bug running Phantom, it complains about semi-colon....
- Grab from other Wallpaper repositories / Flickr / Google / etc.
- Cross-Platform Support
