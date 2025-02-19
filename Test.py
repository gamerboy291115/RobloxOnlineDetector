import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

# Function to check if the player is online using Selenium
def is_player_online(driver, user_id):
    # Open the player's profile page
    url = f"https://www.roblox.com/users/{user_id}/profile"
    driver.get(url)

    try:
        # Check for the presence of the online or game status
        presence_icon = driver.find_element(By.CSS_SELECTOR, "span[data-testid='presence-icon']")

        # If either the 'online' or 'game' class is present, the player is online
        if "online" in presence_icon.get_attribute("class") or "game" in presence_icon.get_attribute("class"):
            return True  # Player is online
    except:
        # If the element is not found, player is offline
        pass

    return False  # Player is offline

# Function to delete the friends carousel list container element from the page
def delete_friends_carousel(driver):
    try:
        # Execute JavaScript to remove the friends carousel container
        driver.execute_script("document.querySelector('.friends-carousel-list-container').remove();")
        print("Deleted friends carousel container")
    except Exception as e:
        print(f"Error while deleting element: {e}")

# Function to monitor player status
def monitor_player_status(user_id):
    options = Options()
    options.headless = False  # Set to False if you want to see the browser window

    # Provide the correct path to chromedriver
    service = Service(executable_path='C:/path/to/your/chromedriver.exe')  # Adjust this path accordingly
    driver = webdriver.Chrome(service=service, options=options)

    # Go to Roblox login page
    driver.get("https://www.roblox.com/Login")

    # Wait for 60 seconds while you're on the login page
    print("Waiting for login... Please login manually if not already done.")
    time.sleep(60)

    last_status = None
    video_file_path = r"C:\Users\Hudson\Downloads\video.mp3"  # Replace with your video path

    while True:
        current_status = is_player_online(driver, user_id)

        # If the current status has changed from the last status, print a message
        if current_status != last_status:
            if current_status:
                print(f"Player {user_id} is online now. Playing video...")
                # Open the local video file
                if os.path.exists(video_file_path):
                    webbrowser.open(f'file:///{video_file_path}')
                else:
                    print("Video file not found!")
            else:
                print(f"Player {user_id} is offline now.")

        # Call the delete function to remove the friends carousel container
        delete_friends_carousel(driver)

        last_status = current_status  # Update the last status
        time.sleep(60)  # Check every 60 seconds

# Example usage: Replace the user ID with the actual ID you want to monitor
monitor_player_status(7191965735)  # Replace with the actual user ID
