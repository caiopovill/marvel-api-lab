from marvel import Marvel
from selenium import webdriver
from time import sleep

#! marvel api key
m = Marvel("fe14920f3b50d7a311d2597cf08e8408",
           "8420ecfe5ae763a44ff88eb8de70e89e72b316f1")


class Marvel:
    characters = m.characters
    all_characters = m.characters.all(limit=100)
    
#! show all heroes that have description
    def show_heros(self, all_characters=all_characters, offset = 0):
        for dic in all_characters['data']['results']:
            if dic['description']:
                print(dic['name'])
        offset += 100
        all_characters = m.characters.all(limit=100, offset=offset)
        self.show_heros(all_characters,offset)
        
#! show all heroes contains a description       
    def search_hero(self, hero):
        if m.characters.all(nameStartsWith=hero)['data']['results'][0]['description']:
            print(f"""{m.characters.all(nameStartsWith=hero)['data']['results'][0]['name']}
Description - {m.characters.all(nameStartsWith=hero)['data']['results'][0]['description']}""")
        else:
            print("Hero doesn't have a description")
            
#! opens an image of the selected hero     
    def image(self, hero):
        try:
            path = m.characters.all(nameStartsWith=hero)['data']['results'][0]['thumbnail']['path']
            driver = webdriver.Chrome()
            driver.get(f'{path}.jpg')
            sleep(10)
        except IndexError:
            print("Hero doesn't have ")
        
        
            
a = Marvel()

a.image('asdasd')
        
       