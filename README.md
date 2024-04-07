<h1 align='center'>SkyblockPy, a simple Python API wrapper for the Hypixel Skyblock API.</h1>

[![CodeFactor](https://www.codefactor.io/repository/github/pybotdevs/skyblockpy/badge)](https://www.codefactor.io/repository/github/pybotdevs/skyblockpy)


## About
### What is SkyblockPy?
SkyblockPy is a simple Python API wrapper which is used to communicate and fetch data from the Hypixel Skyblock API endpoints.
It is based on the Python requests library, which makes it very simple to develop for and fix issues.

### How do I use SkyblockPy?
SkyblockPy works by communicating with the Hypixel API endpoints by using your **API key**. 

If no errors are returned by the API endpoint (status code 200 is returned), then the API output is returned as a `dict`.

## Setup and Usage
### Obtaining an API key
Go to the Hypixel Minecraft Java server and use `/api` command.

### Example Implementation of SkyblockPy
Here's an example snippet of retrieving the third page of the latest Skyblock auctions.

```py
import skyblockpy

skyblock = skyblockpy.Skyblock("api_key")  # Initialize the Skyblock class with a prospective Hypixel API key.

def latest_auctions_raw() -> dict:  # Make a function for returning API output, and highlight return output type as dict.
    output = skyblock.get_auctions(page=3)  # Gets the API response.
    return output

latest_auctions_raw()  # Run the actual function now.
```

Here's another example snippet on getting information on a player in Hypixel.

```py
import skyblockpy

skyblock = skyblockpy.Skyblock("api_key")  # Initialize the Skyblock class with a prospective Hypixel API key.

def get_player_info() -> dict:  # Make a function for returning API output, and highlight return output type as dict.
    output = skyblock.get_player_info("notsniped")  # Gets an API response on player info for a user "notsniped".
    return output

get_player_info()  # Run the actual function.
```

## Extra
### I found a bug/I want to add a missing feature!
Just make a new issue [here](https://github.com/PyBotDevs/skyblockpy/issues/new) and describe the bug/feature.

<hr>

### Hypixel API Documentation is given here: https://api.hypixel.net/
