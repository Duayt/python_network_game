# python_network_game
learning server/client via python



# Installation
require python 3.9.5

``` pip install -r requirements.txt```

# Usage
1. Setup port and ip address (ipv4) in .env file
2. Run server with `python server.py`
3. Run client for player 1 with `python client.py`
4. Run client for player 2 again with `python client.py`


# Mac m1 issue
https://github.com/pygame/pygame/issues/2452


try methods below instead

```
brew update
brew install python@3.9
brew install pkg-config xquartz
brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf

python3 -m venv pygame2
source ./pygame2/bin/activate

pip install --upgrade pip setuptools

pip install wheel
pip install venvdotapp
venvdotapp

pip install --no-cache-dir git+https://github.com/nelsonlove/pygame
```



# Reference
https://www.youtube.com/watch?v=McoDjOCb2Zo&t=3714s&ab_channel=freeCodeCamp.org
