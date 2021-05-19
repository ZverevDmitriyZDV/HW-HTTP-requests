import requests
from pprint import pprint

class Hero_card():

    def __init__(self, url, id_hero=1):
        self.id_hero = id_hero
        self.url = url
        self.url += ('/' + str(id_hero))
        self.resource = requests.get(self.url).json()
        self.error_message = {'error': 'invalid id', 'response': 'error'}

    def get_stats(self, dict=dict(), list=list()):
        if self.isnot_error():
            self.name = self.resource["name"]
            got_intel = self.resource["powerstats"]["intelligence"]
            if got_intel != 'null':
                self.intel = int(got_intel)
            else:
                self.intel = 0
            list.append(self.intel)
            dict_value = dict.get(self.intel, [])
            dict_value.append(self.name)
            dict[self.intel] = dict_value
        return dict, list

    def isnot_error(self):
        if self.resource != self.error_message:
            return self.resource
        else:
            return False

    def max_intel(self):
        m_dict, m_list = self.get_stats()
        self.highest_intel = max(list)
        return m_dict[self.highest_intel], self.highest_intel


url = "https://superheroapi.com/api/2619421814940190"
id = 1
new_hero = Hero_card(url, id)
while new_hero.isnot_error():
    print(id)
    new_hero = Hero_card(url, id)
    new_hero.get_stats()
    print(new_hero.resource)
    id += 1



print(new_hero.get_stats())
print(new_hero.max_intel())
