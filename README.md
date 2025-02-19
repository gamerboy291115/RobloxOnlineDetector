# Roblox Online Detector Documentation

If you have just found this link and don't know how to download and install RobloxOnlineDetector, watch this video: "YouTube link here."

Roblox Online Detector is an open-source GitHub repository that shows you how to install and set up this tool. This script allows you to choose any profile on the Roblox platform, and it will notify you with a loud warning sound when that player is online. If the player is offline, it will indicate that as well. Ever wanted to join one of your favorite Roblox YouTubers, but when you visit their Roblox profile, you never seem to catch them online? With this tool, you can run it in the background while playing games, or simply let it run. Once the Roblox player you chose is online, it will notify you with a loud sound.

**In this document, we will cover:**

- Installing Python
- Installing PyCharm
- Installing Chrome WebDriver
- How to install RobloxOnlineDetector

### Supported Devices:
- Win64 (Windows-64bit)

### Python Installation:
[Link to Install Python](https://www.python.org/downloads/)

### PyCharm Installation:
[Link to Install PyCharm](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)

Chrome WebDriver Installation:

## Open Chrome

Once you have opened Chrome click on the three dots on the top right a dropdown menu should appear form there click Help then about googel chrome

Once you have clicked that you should see a page on that page somewhere it should say Version: "Chrome Version Here"
this is a image of what it should look like:

![Picture Of About Chrome](https://th.bing.com/th/id/R.3020f66fa850d84b71fb792004036d7b?rik=MDBTLLcc31qg%2fA&pid=ImgRaw&r=0)

As you can see it says Version 86.0.Etc.. Yours will look something like it yours may be a newer version as this is a old photo so your might say
Version 133.0.6943.98 
And could be higher by the time your seeing this.

Now navigate to this link in your chrome browser: 

Chrome driver link:
[Link to ChromeDrivers](https://googlechromelabs.github.io/chrome-for-testing/)

Once you have opened the link click on the version that matched your version of chrome
After that it should open a new window with different links
click the one that matches like this:

> Binary:       Platform:

> chromedriver	win64


Copy the link once you have found the one that matches
After you have copied the link paste it into a seperate browser and hit enter it should then download chromedriver.exe

### Placing ChromeDriver in the correct path

Now you need to place this newly downloaded chrome driver in the correct path first extract the zip file then enter the extracted file and there should be a chromedriver.exe copy it.

Once you have copied it navigate to Your PyCharm project with the python script.

The path should look something like this:

> C:\Users\LOGGEDINUSER\PycharmProjects\PROJECTFILE

Paste the chromedriver.exe into this new path.

#### Installing Pip on python

To install pip on python

	python get-pip.py

[^1]: This is the footnote.


##### Installing Basic requirements

**Now that you have installed pip you will need to install some more software using these commands**

Install Requests and beautifulsoup4:

	pip install requests beautifulsoup4

[^1]: This is the footnote.

Install selenium:

	pip install selenium

[^1]: This is the footnote.


###### Make python script

Now you are going to need to add the RobloxOnlineDetector script to your PyCharm project folder
To do this first make a new pycharm folder and name it whatever make a new python script and name it whatever also

**Time to add the script**

Copy and paste the script in RobloxOnlineDetector file








