"""Load Imports
    """
import requests
import json
"""Load Variables
    """
URL = 'https://api.kanye.rest/'

class kanye:
    def answer(self):
        """Get Kanye's Answer
        """
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()['quote']
        else:
            return 'Kanye is not responding'
    def ask(self):
        """Ask Kanye
        """
        return self.answer()
    
input("press enter to ask kanye")
print("so you got a question for the kayne bot...")
useri =  input("What is your question? ")
print('Kanye says: ' + kanye().ask())
print(kanye().answer())
