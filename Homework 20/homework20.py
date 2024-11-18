import requests
import json

char_url = 'https://rickandmortyapi.com/api/character'


class Character:
    def __init__(self, name, char_id, episode_urls):
        self.name = name
        self.char_id = char_id
        self.episode_urls = episode_urls



class RickAndMorty:
    def __init__(self):
        self.characters = {}



    def load_and_process_characters(self):
        response = requests.get(char_url).json()
        for char in response['results']:
            name = char['name']
            char_id = char['id']
            episode_urls = char['episode']
            character = Character(name, char_id, episode_urls)
            self.characters[char_id] = character



    def write_in_json(self, filename="rick_and_morty.json"):
        character_episodes = {}
        for char_id, character in self.characters.items():
            episode_names = []
            for url in character.episode_urls:
                episode_id = int(url.split('/')[-1])  
                episode_response = requests.get(f"https://rickandmortyapi.com/api/episode/{episode_id}").json() 
                episode_names.append(episode_response['name'])
            character_episodes[character.name] = episode_names


        with open(filename, 'w') as json_file:
            json.dump(character_episodes, json_file, indent=4)



rick_and_morty = RickAndMorty()
rick_and_morty.load_and_process_characters()
rick_and_morty.write_in_json()