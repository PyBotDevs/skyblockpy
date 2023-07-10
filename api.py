"""Used for accessing the Skyblock API."""
# Imports
import requests
from json import loads as parse

# Functions
class Skyblock:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_uuid(self, player_name: str) -> str:
        api_request = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{player_name}")
        content = parse(api_request.content)
        return content["id"]

    # API Retrieval Commands
    def get_player_info(self, player_name: str) -> dict:
        """Fetches data of a specific player, including game stats."""
        player_uuid = self.get_uuid(player_name)
        api_request = requests.get(f"https://api.hypixel.net/player?key={self.api_key}&uuid={player_uuid}").content
        player_data = parse(api_request)
        return player_data

    def get_guild_info(self, player_name: str) -> dict:
        """Retrieve a guild by a player."""
        player_uuid = self.get_uuid(player_name)
        api_request = requests.get(f"https://api.hypixel.net/guild?key={self.api_key}&player={player_uuid}").content
        guild_data = parse(api_request)
        return guild_data

    def get_auctions(self, page: int = 0) -> dict:
        """
        Returns a `dict` of the 1000 latest auctions in Skyblock.
        
        Optional args:
        * `page`: View a specific page of auctions.
        """
        api_request = requests.get(f"https://api.hypixel.net/skyblock/auctions?key={self.api_key}&page={page}").content
        auctions = parse(api_request)
        return auctions

    def get_recentgames(self, player_name: str) -> dict:
        """Fetches the recently played games of a specific player."""
        player_uuid = self.get_uuid(player_name)
        api_request = requests.get(f"https://api.hypixel.net/recentgames?key={self.api_key}&uuid={player_uuid}").content
        player_data = parse(api_request)
        return player_data

    def get_player_status(self, player_name: str) -> dict:
        """Fetches the current online status of a specific player."""
        player_uuid = self.get_uuid(player_name)
        api_request = requests.get(f"https://api.hypixel.net/status?key={self.api_key}&uuid={player_uuid}").content
        player_data = parse(api_request)
        return player_data

    def get_player_auctions(self, player_name: str) -> dict:
        """Returns a `dict` of all Skyblock auctions from a particular player."""
        player_uuid = self.get_uuid(player_name)
        api_request = requests.get(f"https://api.hypixel.net/skyblock/auction?key={self.api_key}&player={player_uuid}").content
        player_auctions = parse(api_request)
        return player_auctions

    def get_recently_ended_auctions(self) -> dict:
        """Returns a `dict` of all the auctions that have recently ended within 60 seconds."""
        api_request = requests.get("https://api.hypixel.net/skyblock/auctions_ended").content
        recently_ended_auctions = parse(api_request)
        return recently_ended_auctions

    def get_game_info(self) -> dict:
        """Returns information about Hypixel Games."""
        api_request = requests.get("https://api.hypixel.net/resources/games").content
        games_info = parse(api_request)
        return games_info

    def get_achievements(self) -> dict:
        """Returns a `dict` of all Hypixel achievements."""
        api_request = requests.get("https://api.hypixel.net/resources/achievements").content
        games_info = parse(api_request)
        return games_info

    def get_challenges(self) -> dict:
        """Returns a `dict` of all Hypixel challenges."""
        api_request = requests.get("https://api.hypixel.net/resources/challenges").content
        games_info = parse(api_request)
        return games_info

    def get_quests(self) -> dict:
        """Returns a `dict` of all Hypixel quests."""
        api_request = requests.get("https://api.hypixel.net/resources/quests").content
        games_info = parse(api_request)
        return games_info

    def get_guild_achievements(self) -> dict:
        """Returns a `dict` of all Hypixel Guild achievements."""
        api_request = requests.get("https://api.hypixel.net/resources/guilds/achievements").content
        games_info = parse(api_request)
        return games_info

    def get_vanity_pets(self) -> dict:
        """Returns a `dict` of all Hypixel vanity pets."""
        api_request = requests.get("https://api.hypixel.net/resources/vanity/pets").content
        games_info = parse(api_request)
        return games_info

    def get_vanity_companions(self) -> dict:
        """Returns a `dict` of all Hypixel vanity companions."""
        api_request = requests.get("https://api.hypixel.net/resources/vanity/companions").content
        games_info = parse(api_request)
        return games_info

    def get_news(self) -> dict:
        """Returns a `dict` of the latest Skyblock news from Hypixel."""
        api_request = requests.get(f"https://api.hypixel.net/skyblock/news?key={self.api_key}").content
        news = parse(api_request)
        return news

    def get_bazaar_data(self) -> dict:
        """Returns a `dict` of Skyblock bazaar data."""
        api_request = requests.get(f"https://api.hypixel.net/skyblock/bazaar?key={self.api_key}").content
        bazaar_data = parse(api_request)
        return bazaar_data

    def get_player_profile(self, player_name: str) -> dict:
        """Returns a `dict` of profile data on a player."""
        player_uuid = self.get_uuid(player_name)
        api_request = requests.get(f"https://api.hypixel.net/skyblock/profiles?key={self.api_key}&uuid={player_uuid}").content
        player_profile_data = parse(api_request)
        return player_profile_data

    def get_player_bingo_data(self, player_name: str) -> dict:
        """Returns a `dict` of Bingo data for parcitipated events of the provided player."""
        player_uuid = self.get_uuid(player_name)
        api_request = requests.get(f"https://api.hypixel.net/skyblock/bingo?key={self.api_key}&uuid={player_uuid}").content
        player_bingo_data = parse(api_request)
        return player_bingo_data

    def get_firesales(self) -> dict:
        """Returns a `dict` of all currently active or upcoming Fire Sales for Skyblock."""
        api_request = requests.get("https://api.hypixel.net/resources/skyblock/firesales").content
        firesales_data = parse(api_request)
        return firesales_data

    def get_collections(self) -> dict:
        """Returns a `dict` of information related to Skyblock Collections."""
        api_request = requests.get("https://api.hypixel.net/resources/skyblock/collections").content
        collections_data = parse(api_request)
        return collections_data

    def get_skills(self) -> dict:
        """Returns a `dict` of information related to Skyblock Skills."""
        api_request = requests.get("https://api.hypixel.net/resources/skyblock/skills").content
        collections_data = parse(api_request)
        return collections_data

    def get_items(self) -> dict:
        """Returns a `dict` of information related to Skyblock items."""
        api_request = requests.get("https://api.hypixel.net/resources/skyblock/items").content
        items_data = parse(api_request)
        return items_data

    def get_mayor_information(self) -> dict:
        """Returns a `dict` of information regarding the current mayor in Skyblock."""
        api_request = requests.get("https://api.hypixel.net/resources/skyblock/election").content
        mayor_info = parse(api_request)
        del mayor_info["current"]
        return mayor_info

    def get_current_election(self) -> dict:
        """Returns a `dict` of information regarding the current election in Skyblock."""
        api_request = requests.get("https://api.hypixel.net/resources/skyblock/election").content
        election_info = parse(api_request)
        del election_info["mayor"]
        return election_info

    def get_bingo_event(self) -> dict:
        """Returns a `dict` of information regarding the current bingo event and goals in Skyblock."""
        api_request = requests.get("https://api.hypixel.net/resources/skyblock/bingo").content
        bingo_data = parse(api_request)
        return bingo_data

    def get_active_network_boosters(self):
        """Returns a `dict` of all of the active network boosters."""
        api_request = requests.get(f"https://api.hypixel.net/boosters?key={self.api_key}").content
        boosters_data = parse(api_request)
        return boosters_data

    def get_current_player_counts(self):
        """Returns a `dict` of the current player counts for all game modes."""
        api_request = requests.get(f"https://api.hypixel.net/counts?key={self.api_key}").content
        player_count_data = parse(api_request)
        return player_count_data

    def get_current_leaderboards(self):
        """Returns a `dict` of the current Hypixel leaderboards."""
        api_request = requests.get(f"https://api.hypixel.net/leaderboards?key={self.api_key}").content
        leaderboards_data = parse(api_request)
        return leaderboards_data

    def get_punishment_statistics(self):
        """Returns a `dict` of Hypixel's punishment statistics."""
        api_request = requests.get(f"https://api.hypixel.net/punishmentstats?key={self.api_key}").content
        punishment_stats_data = parse(api_request)
        return punishment_stats_data
