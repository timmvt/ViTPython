# # ITP Week 4 Day 1 Lecture

# What is web scraping? Web Scraping is the process of extracting data from a website.  It is done by using a program called a web scraper.  The web scraper is a program that runs on a computer and can access a website.  The web scraper can then extract data from the website.  The web scraper can then save the data to a file.  The web scraper can then use the data to make a report.

# How do web scrapers work? The web scraper must first be given a URL to access a website.  Then the scraper loads the entire HTML code, and extracts the data.   The user determines what data to extract.  The scraper then saves the data to a file, usually in CSL or Excel format (although it can be formatted in other ways, such as JSON).

# To begin working with web scrapers, we first need to understand a little bit about HTML.  HTML (hyper-text markup language) is a simple text format which is interpreted and rendered onto the user's screen by web browsers, and styled with Cascading Style Sheets (CSS).  HTML uses a system called "tags" to organize and access content, or "elements".  Tags determine where a particular element begins and ends.  We can also use tags to assign elements names, through which we can acess and begin manipulating the elements.  Some examplesYeah of some HTML tags:

# <h1>This is a heading</h1>
# <p>This is a paragraph.</p>
# <div>This is a div.</div>
# <a href="addresstolinkto.com">This is a link.</a>
# <img src="linktomyimagefile.jpg" /> This is an image tag

# HTML tags can also be assigned a 'class' and/or an 'id' to make them easier to work with.  For instance, can give a div a class of "cats" by writing a tag that looks like:

# <div class="cats">Here's some content about a cat.</div>

# Keep in mind that classes are generally used to organizing and acessing MULTIPLE elements, whereas IDs are generally reserved for an element which will only appear ONCE in the page content, such as:

# <h1 id="main_title">The title of my webpage</h1>

# Python has a built-in module called 'webbrowser' which allows Python to open the default web browser to a specified address.  The code for this is very simple:


# import webbrowser

# webbrowser.open('https://inventwithpython.com/')

# However all it does is open a browser to a specific page.  Can you see how we could use Python to open many pages based on code that we have written?

# As we saw last week, we can use the requests module to pull information from the internet and format it.  If the requests module is not installed, you may use:

# pip3 install --user requests 

# to add the library and begin using the module.

# From here we can save the web page to a file on our hard drive using the open() and write() methods we learned about last week.  However we have to use the 'wb' option to write binary data instead of text data in order to maintain the Unicode encoding of the text.

# Parsing HTML with the bs4 Module
# Beautiful Soup is a module for extracting information from an HTML page (and is much better for this purpose than regular expressions). The Beautiful Soup module’s name is bs4 (for Beautiful Soup, version 4). To install it, you will need to run pip install --user beautifulsoup4 from the command line. While beautifulsoup4 is the name used for installation, to import Beautiful Soup you run import bs4.

# For this chapter, the Beautiful Soup examples will parse (that is, analyze and identify the parts of) an HTML file on the hard drive. 

# As you can see, even a simple HTML file involves many different tags and attributes, and matters quickly get confusing with complex websites. Thankfully, Beautiful Soup makes working with HTML much easier.

# Creating a BeautifulSoup Object from HTML
# The bs4.BeautifulSoup() function needs to be called with a string containing the HTML it will parse. The bs4.BeautifulSoup() function returns a BeautifulSoup object. Enter the following into the interactive shell while your computer is connected to the internet:

# >>> import requests, bs4
# >>> res = requests.get('https://nostarch.com')
# >>> res.raise_for_status()
# >>> noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# >>> type(noStarchSoup)
# <class 'bs4.BeautifulSoup'>

# This code uses requests.get() to download the main page from the No Starch Press website and then passes the text attribute of the response to bs4.BeautifulSoup(). The BeautifulSoup object that it returns is stored in a variable named noStarchSoup.

# You can also load an HTML file from your hard drive by passing a File object to bs4.BeautifulSoup() along with a second argument that tells Beautiful Soup which parser to use to analyze the HTML.

# Enter the following into the interactive shell (after making sure the example.html file is in the working directory):

# >>> exampleFile = open('example.html')
# >>> exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
# >>> type(exampleSoup)
# <class 'bs4.BeautifulSoup'>

# The 'html.parser' parser used here comes with Python. However, you can use the faster 'lxml' parser if you install the third-party lxml module. Follow the instructions in Appendix A to install this module by running pip install --user lxml. Forgetting to include this second argument will result in a UserWarning: No parser was explicitly specified warning.

# Once you have a BeautifulSoup object, you can use its methods to locate specific parts of an HTML document.

# Finding an Element with the select() Method
# You can retrieve a web page element from a BeautifulSoup object by calling the select()method and passing a string of a CSS selector for the element you are looking for. Selectors are like regular expressions: they specify a pattern to look for—in this case, in HTML pages instead of general text strings.

# The various selector patterns can be combined to make sophisticated matches. For example, soup.select('p #author') will match any element that has an id attribute of author, as long as it is also inside a <p> element. Instead of writing the selector yourself, you can also right-click on the element in your browser and select Inspect Element. When the browser’s developer console opens, right-click on the element’s HTML and select Copy ▸ CSS Selector to copy the selector string to the clipboard and paste it into your source code.

# The select() method will return a list of Tag objects, which is how Beautiful Soup represents an HTML element. The list will contain one Tag object for every match in the BeautifulSoup object’s HTML. Tag values can be passed to the str() function to show the HTML tags they represent. Tag values also have an attrs attribute that shows all the HTML attributes of the tag as a dictionary. Using the example.html file from earlier, enter the following into the interactive shell:

# >>> import bs4
# >>> exampleFile = open('example.html')
# >>> exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# >>> elems = exampleSoup.select('#author')
# >>> type(elems) # elems is a list of Tag objects.
# <class 'list'>
# >>> len(elems)
# 1
# >>> type(elems[0])
# <class 'bs4.element.Tag'>
# >>> str(elems[0]) # The Tag object as a string.
# '<span id="author">Al Sweigart</span>'
# >>> elems[0].getText()
# 'Al Sweigart'
# >>> elems[0].attrs
# {'id': 'author'}

# This code will pull the element with id="author" out of our example HTML. We use select('#author') to return a list of all the elements with id="author". We store this list of Tag objects in the variable elems, and len(elems) tells us there is one Tag object in the list; there was one match. Calling getText() on the element returns the element’s text, or inner HTML. The text of an element is the content between the opening and closing tags: in this case, 'Al Sweigart'.

# Passing the element to str() returns a string with the starting and closing tags and the element’s text. Finally, attrs gives us a dictionary with the element’s attribute, 'id', and the value of the id attribute, 'author'.

# You can also pull all the <p> elements from the BeautifulSoup object. Enter this into the interactive shell:

# >>> pElems = exampleSoup.select('p')
# >>> str(pElems[0])
# '<p>Download my <strong>Python</strong> book from <a href="https://
# inventwithpython.com">my website</a>.</p>'
# >>> pElems[0].getText()
# 'Download my Python book from my website.'
# >>> str(pElems[1])
# '<p class="slogan">Learn Python the easy way!</p>'
# >>> pElems[1].getText()
# 'Learn Python the easy way!'
# >>> str(pElems[2])
# '<p>By <span id="author">Al Sweigart</span></p>'
# >>> pElems[2].getText()
# 'By Al Sweigart'

# This time, select() gives us a list of three matches, which we store in pElems. Using str() on pElems[0], pElems[1], and pElems[2] shows you each element as a string, and using getText() on each element shows you its text.

# Getting Data from an Element’s Attributes
# The get() method for Tag objects makes it simple to access attribute values from an element. The method is passed a string of an attribute name and returns that attribute’s value. Using example.html, enter the following into the interactive shell:

# >>> import bs4
# >>> soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
# >>> spanElem = soup.select('span')[0]
# >>> str(spanElem)
# '<span id="author">Al Sweigart</span>'
# >>> spanElem.get('id')
# 'author'
# >>> spanElem.get('some_nonexistent_addr') == None
# True
# >>> spanElem.attrs
# {'id': 'author'}

# Here we use select() to find any <span> elements and then store the first matched element in spanElem. Passing the attribute name 'id' to get() returns the attribute’s value, 'author'.

