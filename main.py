import requests
import pandas as pd
from time import sleep

from bs4 import BeautifulSoup
from MatchResult import MatchResult

#Grab base url
base_url = 'https://www.magyarfutball.hu/hu/merkozesek/bajnoki_merkozesek/nb_i'

results = []

#Loop through the seasons
#For example https://www.magyarfutball.hu/hu/merkozesek/bajnoki_merkozesek/nb_i/2022_2023
for years in range(1970, 2022):

    #Get url and request page
    url = f'{base_url}/{years}_{years+1}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    #Find all round (forduló) headers
    for round in soup.find_all('h3', class_='matchday-full'):

        #Extract round number from header
        round_number = round.text.split()[-2][:-1]

        #Extract round data by getting sibling table
        round_data = round.find_next_sibling('table')    

        #Extract rows of the table except for first and last, they're there for semantic reasons
        match = round_data.find_all('tr')[1:-1]

        #Loop through each row
        for match in round_data.find_all('tr')[1:-1]:
            data = match.text[1:-1].split('\n')

            #Delete two elements from the array as they are empty
            del(data[3])
            del(data[4])

            #Create new MatchResult instance and append it to our list
            results.append(MatchResult(data, f'{years}-{years+1}', int(round_number)))
    
    #Display number of rows to check on progress
    print(len(results))
    #Wait a bit so as not to run into problems for sending requests too fast
    sleep(2)

#Convert to dataframe by callin the to_dict method of the objects
df = pd.DataFrame([r.to_dict() for r in results])

#Write to csv
df.to_csv('results.csv', sep=';', header=True, encoding='utf-8', index=False)