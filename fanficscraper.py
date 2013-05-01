# import html5lib
import urllib2
"""
Steps:
#Create a new file txt file holding the story
#Add the title of the book and the author to the ouput file
#Get teh URL corresponding to the Chapter
#Access teh URL and idenitfiy the HTML tags containing the relevant text
#Add the Chapter number and title to teh output File
#Add the chapter text to the output file
#repeat for each chapter

ToDo:
adjust this so that it works without asking for input.  AMybe jst the url of chpater one have it sense when the chapter numbers have gone too far by when it receives a 404 page.
"""


#Don't judge me.  
#It's for my Gf's kindle, she's likes her HarryPotter on the Go

Title = 'Written in Sand'
Author = 'Cheeky Rose B'
total_chapters = 56

f = open('%s.html' %(Title), 'wb')

#Copy in URl replace chapter number with with %d
url_base = 'http://www.fanfiction.net/s/4956275/%d/Written-in-Sand'

#flag to let code know that we found what we wanted
text_target = 0
#Header
f.write("%s <p> by: %s" %(Title, Author))
#Chapters
for current_chapter in range(0,total_chapters,1):
    f.write('<h1>CHAPTER %d </h1>' %(current_chapter + 1))
    url = url_base %(current_chapter)  
    results = urllib2.urlopen(url)
    for l in results.readlines():
    #div Identifier in HTML source preceding the story text
        if l.count("<div class='storytext xcontrast_txt' id='storytext'>") > 0:
            text_target = 1
        elif l.count("</div>") > 0:
            text_target = 0
        if text_target == 1:
            f.writelines(l)
f.close()

