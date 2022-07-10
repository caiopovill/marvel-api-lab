# importing the marvel module
from marvel import Marvel
from selenium import webdriver
from time import sleep

# chave pra ter acesso
m = Marvel("fe14920f3b50d7a311d2597cf08e8408",
           "8420ecfe5ae763a44ff88eb8de70e89e72b316f1")

class Marvel:
    characters = m.characters
    all_characters = m.characters.all(limit=100)
           
# imprime todos os heróis que possuem uma descrição
    def show_heros(self, all_characters=all_characters, offset = 0):
        for nome in all_characters['data']['results']:
            if nome['description']:
                print(nome['name'])
        offset += 100
        all_characters = m.characters.all(limit=100, offset=offset)
        self.show_heros(all_characters,offset)

# imprime a descrição do herói solicitado   
    def search_hero(self, hero):
        if m.characters.all(nameStartsWith=hero)['data']['results'][0]['description']:
            print(f"""{m.characters.all(nameStartsWith=hero)['data']['results'][0]['name']}
Description - {m.characters.all(nameStartsWith=hero)['data']['results'][0]['description']}""")
        else:
            print("Hero doesn't have a description")
# Abre a imagem do herói solicitado
    def image(self, hero):
        try:
            path = m.characters.all(nameStartsWith=hero)['data']['results'][0]['thumbnail']['path']
            driver = webdriver.Chrome()
            driver.get(f'{path}.jpg')
            sleep(10)
        except IndexError:
            print("Hero doesn't have an image")
              
a = Marvel()
a.image('Captain America')
        
       
