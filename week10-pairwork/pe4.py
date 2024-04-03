'''
Paiwork Exercise No.4
Name: Anjan and Roberta
Date: April 2 - 2024
'''
import wikipedia
import time
from  concurrent.futures import ThreadPoolExecutor

# Answers to questions from XR_Pair_Exercise_4.pdf

# PartA
# 1. Use the wikipedia.search method to return a list of topics related to 'generative artificial intelligence'.

start_time = time.perf_counter()

wiki_search_title = wikipedia.search('Generative Artificial Intelligence')

# 2. Iterate over search and do following:
for article in wiki_search_title:
    page = wikipedia.page(article, auto_suggest=False) #a.
    title = page.title
    references = page.references
    
    with open(f'{title}.txt','w') as text_file:
        for ref in references:
            text_file.write(ref + "\n\n")

end_time = time.perf_counter()
time_taken = end_time - start_time
print(f'Time taken: {time_taken:.2f} seconds.')

# PartB
# 1. Done in PartA.1

# 2. Create a function def wiki_dl_and_save(topic): that:
# retrieves the wikipedia page for the topic

start_time2 = time.perf_counter()
def wiki_dl_and_save(title):
    for article in wiki_search_title:
        page = wikipedia.page(article, auto_suggest=False) #a.
        title = page.title
        references = page.references
    
    with open(f'{title}.txt','w') as text_file:
        for ref in references:
            text_file.write(ref + "\n\n")
with ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save,wiki_search_title)

end_time2 = time.perf_counter()

time_taken2 = end_time2 - start_time2
print(f'Time taken: {time_taken2:.2f} seconds')