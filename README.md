<div align="center">
  
# AndroSploit
  
### Android Exploitation Toolkit with Metasploit Integration.

An all-in-one hacking tool written in `Python` to remotely exploit Android devices using `ADB` (Android Debug Bridge) and `Metasploit-Framework`.

![GitHub release (latest by date)](https://img.shields.io/github/v/release/YourUsername/AndroSploit)
![Python](https://img.shields.io/badge/python-v3.10%2B-blue)
![GitHub Release Date](https://img.shields.io/github/release-date/YourUsername/AndroSploit?logo=github)
![GitHub last commit](https://img.shields.io/github/last-commit/YourUsername/AndroSploit?logo=github)
![GitHub Repo stars](https://img.shields.io/github/stars/YourUsername/AndroSploit?style=social)
![GitHub forks](https://img.shields.io/github/forks/YourUsername/AndroSploit?style=social)

</div>

#### Complete Automation to get a Meterpreter session in One Click

This tool can automatically __Create__, __Install__, and __Run__ payloads on target devices using __Metasploit-Framework__ and __ADB__ to gain control over Android devices with an open ADB port `TCP 5555`.

The goal of this project is to simplify penetration testing and vulnerability assessment on Android devices. Now you don't have to learn complex commands—AndroSploit automates the process for you.

> [!TIP]
> __AndroSploit__ can also function as a complete ADB Toolkit, allowing various operations on Android devices over Wi-Fi as well as USB. 

# Screenshots

![Screenshot Page 1](docs/Screenshot-1.PNG)
![Screenshot Page 2](docs/Screenshot-2.PNG)
![Screenshot Page 3](docs/Screenshot-3.PNG)

# Features

* Connect devices using ADB remotely.
* List connected devices.
* Disconnect all devices.
* Access connected device shell.
* Stop ADB Server.
* Take screenshots and automatically pull them to the computer.
* Screen record target device and retrieve the video.
* Transfer files and folders between computer and target device.
* Install and uninstall APK files.
* Run applications remotely.
* List all installed apps.
* Restart/Reboot the target device into various modes (`System`, `Recovery`, `Bootloader`, `Fastboot`).
* __Exploit Device Completely__:
  - Automatically fetch `LHOST`.
  - Create, install, and execute payloads using `msfvenom`.
  - Launch and set up __Metasploit-Framework__ for a `meterpreter` session.
  - Gain full control over the device through Metasploit.
* List and manage files/folders on the target device.
* Copy WhatsApp data, screenshots, and camera photos to the computer.
* Take anonymous screenshots and recordings (auto-delete from target device).
* Open links, display images, and play media remotely.
* Retrieve device and battery information.
* Use keycodes to control the device remotely.
* Send and dump SMS messages.
* Unlock and lock the device remotely.
* Extract APKs from installed apps.
* Mirror and control the target device.
* Power off the target device.
* Scan the local network for connected devices.
* Record and stream audio from the microphone and device.

# Requirements  
* [`python3`](https://www.python.org/) : Python 3.10 or newer
* [`pip`](https://pip.pypa.io/en/stable/installation/) : Python package manager
* [`adb`](https://developer.android.com/studio/command-line/adb) : Android Debug Bridge
* [`metasploit-framework`](https://www.metasploit.com/) : Metasploit-Framework
* [`scrcpy`](https://github.com/Genymobile/scrcpy) : Scrcpy
* [`nmap`](https://nmap.org/) : Nmap

# Run AndroSploit

__AndroSploit__ runs directly using `python3`.

> [!IMPORTANT]
> Ensure you have Python __3.10 or higher__ before running the program.

#### On Linux / macOS :
```
git clone https://github.com/YourUsername/AndroSploit.git
cd AndroSploit/
pip install -r requirements.txt
python3 androsploit.py
```
#### On Windows :
```
git clone https://github.com/YourUsername/AndroSploit.git
cd AndroSploit/
pip install -r requirements.txt
python androsploit.py
```

# Disclaimer

* This project is for educational purposes only.
* The developer is not responsible for any misuse or damage caused by this project.
* Please use this tool ethically and responsibly on devices you own.
* The end-user is responsible for obeying all local, state, and international laws.

# Developer

**Tejas Mahajan** - [@TejasMahajan](https://github.com/Tejas-beep)

# Support Me
If you like my work, consider supporting me via:

<a href="https://paypal.me/Tejasmahajan18" target="_blank"> <kbd> <img src="https://github.com/AzeemIdrisi/AzeemIdrisi/blob/main/docs/paypal-button-blue.png" alt="PayPal" width="147"></a>
