"""Used for accessing the Skyblock API."""
# Imports
import requests
import json

# Functions
class Skyblock:
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def get_uuid(self, player_name: str) -> str:
        api_request = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{player_name}")
        return api_request.text
    
    # API Retrieval Commands
    def get_auctions(self, *, page: int = 0):
        """
        Returns a `dict` of the 1000 latest auctions in Skyblock.
        
        Optional args:
        * `page`: View a specific page of auctions.
        """
        api_request = requests.get(f"https://api.hypixel.net/skyblock/auctions?key={self.api_key}&page={page}")
        auctions = json.loads(api_request)
        return auctions
    
    def get_player_auctions(self, player_name: str):
        """
        Returns a `dict` of all Skyblock auctions from a particular player.
        """
        player_uuid = self.get_uuid(player_name)
        api_request = requests.get(f"https://api.hypixel.net/skyblock/auction?key={self.api_key}&player={player_uuid}")
        player_auctions = json.loads(api_request)
        return player_auctions
    
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
    
    def get_collections(self):
        """
        Returns a `dict` of information related to Skyblock Collections.
        """
        api_request = requests.get("https://api.hypixel.net/resources/skyblock/collections")
        collections_data = json.loads(api_request)
        return collections_data
    
    def get_skills(self):
        """
        Returns a `dict` of information related to Skyblock Skills.
        """
        api_request = requests.get("https://api.hypixel.net/resources/skyblock/skills")
        collections_data = json.loads(api_request)
        return collections_data
