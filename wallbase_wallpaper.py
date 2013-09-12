#!/usr/bin/python
"""
This script requires Selenium, PhantomJS & feh to be installed.
"""
import urllib
import random
import commands
from selenium import webdriver

def tryFeh():
  output = commands.getoutput("feh --version")
  if 'not found' in output:
    print "\nOh Noes, you haz no feh!  apt-get install feh!\n"

def startPhantom():
  commands.getoutput("phantomjs --webdriver=9410 &")
  # This will need to be cleaned up....

def getRandomLine(afile):
  """Algorithm from: http://stackoverflow.com/questions/3540288"""
  line = next(afile)
  for num, aline in enumerate(afile):
    if random.randrange(num + 2): continue
    line = aline
  return line

def getRandomTerm():
  """Pulls Random Word from a Dictionary File."""
  f = open('nouns.txt','rb')
  term = getRandomLine(f).strip("\n")
  f.close()
  return term

def getWallpaper(term):
  """Attempts to find random image on Wallbase.cc"""
  # Replace this with Headless Browser (PhantomJS)
  #f = webdriver.Firefox()
  f = webdriver.PhantomJS()
  f.get("http://www.wallbase.cc")
  q = f.find_element_by_id("query")
  q.send_keys(term)
  try:
    q.submit()
  except:pass
  img_thumbs = f.find_elements_by_class_name('file')
  img_urls = []
  for img in img_thumbs:
    try:
      page_url = img.find_element_by_xpath("..")
      page_url = page_url.get_attribute("href")
      img_urls.append(page_url)
    except: pass
  url = img_urls[random.randrange(len(img_urls))]
  f.get(url)
  src = f.find_element_by_class_name('wall').get_attribute('src')
  f.close()
  return src

def setWallpaper(wallpaper):
  commands.getoutput("feh --bg-scale --fullscreen %s" % (wallpaper))

def saveWallpaper(wallpaper, output):
  img_name = wallpaper.split("/")[-1]
  urllib.urlretrieve(wallpaper, output+img_name)

def main():

    tryFeh()  # Make sure user has Feh installed.
    CYCLE_COUNT = 15  # Amount of Wallpapers To Find.
    print "running...."
    print "Starting Headless PhantomJS Browser..."
    startPhantom()

    for i in range(CYCLE_COUNT):
      print "Getting Term..."
      term = getRandomTerm()
      try:
        wallpaper = getWallpaper(term)
        print "Grabbing Wallpaper..."
      except:continue
      print "Setting Wallpaper..."
      print wallpaper
      setWallpaper(wallpaper)
      print "Saving Wallpaper..."
      saveWallpaper(wallpaper, './walls/')

if __name__ == '__main__':
    main()
