iAuto
========
<a href="iauto.netlify.app" alt="iAuto"/></a>

## Before Running `iAuto.py` 

* Open iAuto.py File and Edit The Following Lines: 

1) `username = 'USERNAME'  # Enter your username here` [line:24]

2) `password = 'PASSWORD'  # Enter your password here` [line:25]

3) `timee = "21:44"  # Specific Time When The message will be send` [line:91] ( optional )

4) `txt_box.send_keys(f"Hi @{usrnames} ! What's up ?")  # Messege that you want to send` [line:53]

5) `usrnames = ['instagram', 'twitter']  # username whom you will send the message` [line:11]


Ensure that you have the latest version of Chrome installed and the
[`chromedriver` ](https://chromedriver.chromium.org/downloads) that matches
your Chrome version available on your `$PATH`. You may have to update this from time to time.

## Requirements
 
* [Python](https://www.python.org/)
* `python` on the PATH
* [The Requests Library](http://python-requests.org) for Python: `pip install requests`

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