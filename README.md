# 🚀 Jitsi Meet Stress Test Tool 🎉

Welcome to this super cool, free-to-use, and open-source stress testing tool for Jitsi Meet, specifically designed to run on Windows operating systems. The tool leverages the power of Selenium and ChromeDriver to simulate a bunch of users joining a Jitsi Meet conference, allowing you to see how your Jitsi Meet server performs under various loads. Pretty neat, huh? 😎

## 🌟 Features

- Simulate a swarm of users joining a Jitsi Meet conference
- Customize the number of sessions and runtime to your liking
- Choose the media option (video and audio, video only, audio only, or none)
- Keep an eye on progress during the test
- Easy to use and modify, so you can make it your own!

## 🛠️ Requirements

- Python 3.x (who doesn't love Python?🐍)
- Selenium (our automation buddy)
- Google Chrome Browser
- ChromeDriver compatible with your installed Google Chrome version

## 🚀 Getting Started

### Downloading ChromeDriver

Download the right version of [ChromeDriver](https://sites.google.com/chromium.org/driver/) that plays nice with your installed Google Chrome version. Extract the `chromedriver.exe` file and place it in the same directory as the stress test script.

### Installing Python 3.x on Windows

1. Visit the official Python website at [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the latest version of Python 3.x for Windows if you havent already.

2. Run the installer, and during the setup process, make sure to check the "Add Python to PATH" checkbox before clicking on "Install Now."

3. Once the installation is complete, open the Command Prompt and run the following command to check if Python is installed successfully:

```
python --version
```

You should see the Python version in the output.

### Installing Node.js on Windows

1. Download the latest LTS version of Node.js from the official website at [https://nodejs.org/en/download/](https://nodejs.org/en/download/).

2. Run the installer, and follow the on-screen instructions. The installer will automatically add Node.js and NPM (Node Package Manager) to your PATH.

3. After the installation is complete, open the Command Prompt and run the following commands to check if Node.js and NPM are installed correctly:

```
node --version
npm --version
```

You should see the Node.js and NPM versions in the output.

## Installing PIP (Python Package Installer)

PIP should already be installed with Python 3.4 and later versions. To check if PIP is installed, open the Command Prompt and run:

```
pip --version
```

If PIP is not installed or you want to upgrade it, download the `get-pip.py` file from [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) and save it to your computer.

Then, open the Command Prompt, navigate to the folder where you saved the `get-pip.py` file, and run the following command:

```
python get-pip.py
```

PIP will be installed or upgraded to the latest version.

### Installing the Selenium Package

Now that you have Python, Node.js, and PIP installed, you can install the Selenium package. Open the Command Prompt and run:

```
pip install selenium
```

That's it! You've successfully installed Python 3, Node.js, PIP, and Selenium on your Windows machine. Time to rock. 🚀

## 🎮 Usage

1. Fire up a command prompt or terminal in the directory containing this repository.

2. Run the script using Python:

```bash
python jitsi_stress_test.py
```

3. Follow the prompts to tailor the stress test to your needs:

- Enter the Jitsi Meet server address (e.g. `https://meet.jit.si`).
- Enter the number of sessions to simulate (Don´t go wild or your CPU will Burn🔥🧯!).
- Enter the runtime in seconds for the stress test.
- Choose the media option (1 - Video and Audio [default], 2 - Video only, 3 - Audio only, 4 - None).

4. Sit back and relax as the sessions start and the progress shows up.

5. Wanna verify the test? Join the meeting with the URL provided in the output. 👀

6. The script will run for the specified duration and display the progress. Once completed, it'll close all sessions and give you a nice report to look at.

## 🛠️ Customization & Contribution

Feel free to tweak the script to better suit your needs or to add some shiny new features. Contributions are more than welcome! If you have any suggestions, improvements, or bug reports, just open an issue or submit a pull request on GitHub.

## 📜 License

This project is free to use and modify under the MIT License. Check out the [LICENSE](LICENSE) file for more information.

Happy testing! 🥳🚀
