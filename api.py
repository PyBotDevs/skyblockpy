"""Used for accessing the Skyblock API."""
import requests
import json

class Skyblock:
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def get_uuid(self, player_name: str) -> str:
        api_request = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{player_name}")
        return api_request.text
    
    # Make API retrieval commands here
    def get_auctions(self, *, player_name: str = None):
        """
        Returns a `dict` of the 1000 latest auctions in Skyblock.
        
        Optional args:
        * `player_name`: Shows auctions only from that player.
        """
        if player_name is not None:
            player_uuid = self.get_uuid(player_name)
            api_request = requests.get(f"https://api.hypixel.net/skyblock/auction?key={self.api_key}&player={player_uuid}")
            return api_request.text
        else:
            api_request = requests.get(f"https://api.hypixel.net/skyblock/auctions?key={self.api_key}")
            auctions = json.loads(api_request)
            return auctions
    
    def get_news(self):
        """
        Returns a `dict` of the latest Skyblock news from Hypixel.
        """
        api_request = requests.get(f"https://api.hypixel.net/skyblock/news?key={self.api_key}")
        news = json.loads(api_request)
        return news

    def get_bazaar_data(self):
        """
        Returns a `dict` of Skyblock bazaar data.
        """
        api_request = requests.get(f"https://api.hypixel.net/skyblock/bazaar?key={self.api_key}")
        bazaar_data = json.loads(api_request)
        return bazaar_data
    
    def get_player_profile(self, player_name: str):
        """
        Returns a `dict` of profile data on a player.
        """
        player_uuid = self.get_uuid(player_name)
        api_request = requests.get(f"https://api.hypixel.net/skyblock/profiles?key={self.api_key}&uuid={player_uuid}")
        player_profile_data = json.loads(api_request)
        return player_profile_data
