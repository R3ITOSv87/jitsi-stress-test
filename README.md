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
- ChromeDriver compatible with your installed Google Chrome version

## 🚀 Getting Started

1. Install Python 3.x from the [official website](https://www.python.org/downloads/) if you haven't already.

2. Install the Selenium package using pip like a boss:

```bash
pip install selenium
```

3. Download the right version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that plays nice with your installed Google Chrome version. Extract the `chromedriver.exe` file and place it in the same directory as the stress test script.

## 🎮 Usage

1. Fire up a command prompt or terminal in the directory containing the stress test script.

2. Run the script using Python:

```bash
python jitsi_stress_test.py
```

3. Follow the prompts to tailor the stress test to your needs:

- Enter the Jitsi Meet server address (e.g. `https://meet.jit.si`).
- Enter the number of sessions to simulate (go wild!).
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
