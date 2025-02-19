# Roblox Online Detector Documentation

If you have just found this link and don't know how to download and install RobloxOnlineDetector, watch this video: "YouTube link here."

Roblox Online Detector is an open-source GitHub repository that shows you how to install and set up this tool. This script allows you to select any profile on the Roblox platform, and it will notify you with a loud warning sound when that player is online. If the player is offline, it will indicate that as well. Have you ever wanted to join one of your favorite Roblox YouTubers, but when you visit their Roblox profile, you never seem to catch them online? With this tool, you can run it in the background while playing games or simply let it run. Once the Roblox player you selected is online, it will notify you with a loud sound.

**In this document, we will cover:**

- Installing Python
- Installing PyCharm
- Installing Chrome WebDriver
- How to install RobloxOnlineDetector

### Supported Devices:
- Win64 (Windows-64bit)

### Python Installation:
[Link to Install Python](https://www.python.org/downloads/)

Or run command prompt as admin and type python

### PyCharm Installation:
[Link to Install PyCharm](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)

Chrome WebDriver Installation:

## Open Chrome

Once you have opened Chrome, click on the three dots in the top right. A dropdown menu should appear. From there, click on 'Help,' then select 'About Google Chrome.

Once you have clicked that, you should see a page where somewhere on the page it will say 'Version: [Chrome Version Here].' This is an image of what it should look like:'

![Picture Of About Chrome](https://th.bing.com/th/id/R.3020f66fa850d84b71fb792004036d7b?rik=MDBTLLcc31qg%2fA&pid=ImgRaw&r=0)

As you can see, it says 'Version 86.0.' Yours will likely look similar, but it may be a newer version since this is an old screenshot. For example, it might say 'Version 133.0.6943.98' or even higher by the time you're seeing this.

Now navigate to this link in your chrome browser: 

Chrome driver link:
[Link to ChromeDrivers](https://googlechromelabs.github.io/chrome-for-testing/)

Once you have opened the link click on the version that matched your version of chrome
After that it should open a new window with different links
click the one that matches like this:

> Binary:       Platform:

> chromedriver	win64


Copy the link once you have found the one that matches. After you’ve copied the link, paste it into a separate browser and hit enter. It should then download 'chromedriver.zip.'

## Placing ChromeDriver in the correct path

Now, you need to place the newly downloaded ChromeDriver in the correct path. First, extract the ZIP file, then enter the extracted folder, where you should find 'chromedriver.exe.' Copy it.

Once you’ve copied it, navigate to your PyCharm project that contains the Python script.
The path should look something like this:

> C:\Users\LOGGEDINUSER\PycharmProjects\PROJECTFILE

Paste the chromedriver.exe into this new path.

## Installing Pip on python

	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

[^1]: This is the footnote.


	

install:

	python get-pip.py

[^1]: This is the footnote.


Please watch the YouTube video on how to use pip, which is listed at the start of the page.


## Installing Basic requirements

**Now that you have installed pip you will need to install some more software using these commands**

**Install Requests and beautifulsoup4:**

	pip install requests beautifulsoup4

[^1]: This is the footnote.

**Install selenium:**

	pip install selenium

[^1]: This is the footnote.


## Make python script

Now, you need to add the RobloxOnlineDetector script to your PyCharm project folder. To do this, first create a new folder in PyCharm and name it whatever you like. Then, create a new Python script and name it whatever you prefer as well.

**Time to add the script**

Copy and paste the script in [Link to Script](https://github.com/gamerboy291115/RobloxOnlineDetector/blob/main/UpdatedRobloxOnlineDetector) into the Python script you created


### Execute the script

Open command prompt as a Administrator

Run this command:

	cd "Delete the parentheses and add the path to the folder where you Python script is stored"

[^1]: This is the footnote

Once you have navigated to that path and ran that command type:

	dir

[^1]: This is the footnote

You should beable to see the python script you created if you did you did this step succesfully

**Run Command**

To execute this Python script type


	python ScriptNameHere.py

[^1]: This is the footnote

Replace scriptnamehere with the name of your Python script

Then click enter.
A Roblox login page should pop up. Log in to your Roblox alt account, which is essentially a dummy account used to check if the user is online.

**You only have 50 seconds to login so do it quickly**

After you have logged in, nothing may happen immediately. You will need to wait for about 50 seconds for it to start. Please watch the YouTube video listed at the top for further instructions.
