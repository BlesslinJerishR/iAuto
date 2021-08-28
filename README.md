<p align="center">
<kbd style="border-radius: 8px; border: 3px solid #FF0000;">
  <img src="https://pbs.twimg.com/profile_images/1232518700/Endhiran-Movie-Wallpapers-6_1_.jpg" width="154"
</kbd>
  <a href="iauto.netlify.app"><h1 align="center">iAuto</h1></a>
  <p align="center"> <b>Automate your Instagram private messages 24/7 using our iAuto .
  </p>
  <p align="center">
    </a>
    <a href="https://github.com/SeleniumHQ/selenium">
      <img src="https://img.shields.io/badge/built%20with-Selenium-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
  </p>
</p>

## Before Running `iAuto.py` 

* Open iAuto.py File and Edit The Following Lines: 

```sh
username = 'USERNAME'  # Enter your username here [line:27]
 
password = 'PASSWORD'  # Enter your password here` [line:28]

timee = "Now"  # Specific Time When The message will be send` [line:83] ( optional )

txt_box.send_keys(f"Hi @{usrnames} ! What's up ?")  # Messege that you want to send` [line:56]

usrnames = ['user 1', 'user 2']  # username whom you will send the message` [line:12]

```

Ensure that you have the latest version of Chrome installed and the
[`chromedriver` ](https://chromedriver.chromium.org/downloads) that matches
your Chrome version available on your `$PATH`. You may have to update this from time to time.

## Requirements
 
* [Python](https://www.python.org/)
- `python` on the PATH

* [The Requests Library](http://python-requests.org) :
```sh
pip install requests
```

* Install Selenium:
```sh
pip install selenium
```

* Install Schedule:
```sh
pip install schedule
```

## Modus Operandi

* Execute the program using:
```sh
python iAuto.py
```

#### Developer : Mastermindx33