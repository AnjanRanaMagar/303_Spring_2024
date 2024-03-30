We can access the python module that helps us with wikipedia access at the following link:

```https://thepythoncode.com/article/access-wikipedia-python```

Install package:
``` pip3 install wikipedia```

Let's get the summary of what Python programming language is:

import wikipedia

### print the summary of what python is
print(wikipedia.summary("Python Programming Language"))
This will extract the summary from this wikipedia page. More specifically, it will print some first sentences, we can specify the number of sentences to extract:

In [2]: wikipedia.summary("Python programming languag", sentences=2)
Out[2]: "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
Notice that I misspelled the query intentionally, it still gives me an accurate result.

Search for a term in Wikipedia search:
In [3]: result = wikipedia.search("Neural networks")
In [4]: print(result)
['Neural network', 'Artificial neural network', 'Convolutional neural network', 'Recurrent neural network', 'Rectifier (neural networks)', 'Feedforward neural network', 'Neural circuit', 'Quantum neural network', 'Dropout (neural networks)', 'Types of artificial neural networks']
This returned a list of related page titles, let's get the whole page for "Neural network" which is result[0]:

### get the page: Neural network
page = wikipedia.page(result[0])
Extracting the title:

### get the title of the page
title = page.title
Getting all the categories of that Wikipedia page:

### get the categories of the page
categories = page.categories
Extracting the text after removing all HTML tags (this is done automatically):

### get the whole wikipedia page text (content)
content = page.content
All links:

### get all the links in the page
links = page.links
The references:

### get the page references
references = page.references
Finally, the summary:

### summary
summary = page.summary
Let's print them out:

### print info
print("Page content:\n", content, "\n")
print("Page title:", title, "\n")
print("Categories:", categories, "\n")
print("Links:", links, "\n")
print("References:", references, "\n")
print("Summary:", summary, "\n")
Try it out!

You can also change the language in wikipedia library in Python from English to another one of your choice:

### changing language
### for a list of available languages, 
### check http://meta.wikimedia.org/wiki/List_of_Wikipedias 
link.
language = "es"
wikipedia.set_lang(language)

### get a page and print the summary in the new language
print(f"Summary of web scraping in {language}:", wikipedia.page("Web Scraping").summary)