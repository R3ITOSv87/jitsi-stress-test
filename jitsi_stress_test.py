## Jitsi Meet Stress Test Tool
##
## https://github.com/Strange-Panda/jitsi-stress-test/
##
## This software is released into the public domain under the terms of the
## Unlicense. For more information, please refer to <http://unlicense.org/>.
##
## SPDX-License-Identifier: Unlicense
##

import os
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Check and install dependencies
try:
    import selenium
except ImportError:
    subprocess.check_call(["python", "-m", "pip", "install", "selenium"])

# Ask for server address, number of sessions, runtime, and media options
server_address = input("Please enter the server address (http(s)//jitsi.meet): ")
num_sessions = int(input("Please enter the number of sessions: "))
runtime = int(input("Please enter the runtime in seconds: "))
media_option = int(input("Choose the media option (1 - Video and Audio [default], 2 - Video only, 3 - Audio only, 4 - None): ") or 1)

# ChromeDriver configuration
chrome_options = Options()

if media_option in [1, 2]:
    chrome_options.add_argument(f"--use-file-for-fake-video-capture={os.path.abspath('test_video.y4m')}")
if media_option in [1, 3]:
    chrome_options.add_argument(f"--use-file-for-fake-audio-capture={os.path.abspath('test_audio.wav')}")

chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Automatically allow access to audio and video devices
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--log-level=3")  # Disable console output from Chrome instances
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Redirect stderr to os.devnull to further suppress console output

# Function to start a session
def start_session(username):
    url = f"{server_address}/StressTestJitsi#userInfo.displayName=%22{username}%22&config.prejoinConfig.enabled=false&config.notifications=[]"
    
    # Use the ChromeDriver in the current directory
    service = Service(executable_path="chromedriver.exe")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    return driver

# Start sessions and display a counter
sessions = []
started_sessions = 0
for i in range(num_sessions):
    username = f"Test{str(i).zfill(3)}"
    session = start_session(username)
    sessions.append(session)
    started_sessions += 1
    print(f"\rStarted sessions: {started_sessions}", end="")

checker_url = f"{server_address}/StressTestJitsi#userInfo.displayName=%22Checker%22&config.prejoinConfig.enabled=false&config.notifications=[]"
print(f"\n\nTo verify the test, join the meeting with the following URL:\n{checker_url}\n")

# Wait time and display progress percentage
start_time = time.time()
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time >= runtime:
        break
    progress_percentage = (elapsed_time / runtime) * 100
    print(f"\rProgress: {progress_percentage:.2f}%", end="")
    time.sleep(1)

# Close sessions simultaneously and output a report
def close_session(session, index):
    session.quit()

with ThreadPoolExecutor() as executor:
    executor.map(close_session, sessions, range(len(sessions)))

print("\n\nStress test completed!")
os._exit(0)
