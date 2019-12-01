
import re
import nltk
from datetime import datetime
import pandas as pd
pd.set_option('display.max_colwidth',10000)

def extract_dates(text):
    # Open a  txt file
    File=open(text,'r', encoding='UTF-8')
    data=File.read()
    
    # Split text into a list of sentences
    firstlst=nltk.sent_tokenize(data)
    # Remove symbols
    bad_chars = ['\n'] 
    lstwopunct=[]# Clean the list of strings.
    for str in firstlst:
     str = ''.join(i for i in str if not i in bad_chars)
     lstwopunct.append(str)
    
    # Figure out the possible patterns reflecting dates
    pat=r'((\d{,2}\d{,2}\d{4})|(\d{0,2} (January|February|March|April|May|June|July|August|September|October|November|December) \d+(, \d{4})?))'
    patterns = re.compile(pat)
    
    # The lists we are going to use
    list_patt=[]
    list_sent=[]
    fixeddates=[]
    
    # Let's search in the list without punctiation for the date patterns,
    # If a pattern is found, then it goes to list_patt and the sentence goes to list_sent
      found=re.findall(pat, line)
      if found!=[]:
       for i in range(len(found)):
        list_patt.append(found[i][0])
        list_sent.append(line)
       
   
    # Turn the dates into ISO 8601 format and put it in a newlist: fixeddates
    for piece in list_patt:
     isodate=''
     element=(re.search(r'\w \d{4}', piece)==None)
     if element==False:
        isodate= datetime.strptime(piece,' %B %Y') 
     elif element==True and (re.search(r'\w \d{2}, \d{4}', piece)!=None):
        isodate= datetime.strptime(piece,' %B %d, %Y')
     elif element==True and (re.search(r'\d{4}', piece)!=None):
        isodate= datetime.strptime(piece,'%Y') 
     elif element==True and (re.search(r'\w \d{2}', piece)!=None):
        isodate= datetime.strptime(piece,' %B %d') 
     elif element==True and (re.search(r'\d{2} \d{2} \d{4}', piece)!=None):
        isodate= datetime.strptime(piece,' %m %d %Y')
        
     if isodate!='':
       fixeddates.append(isodate)
    
    # Making our data frame
    datafr= pd.DataFrame(
    {'Date': fixeddates,
     'Sentence': list_sent,
    })
    # Sorting our dataframe
    dfr_final=datafr.sort_values(by=['Date'])
    
    File.close()
    
    return dfr_final

# Calling the function.
text1="aretha.txt"
text2="bio.txt"
print(extract_dates(text2)) 
aretha=extract_dates(text1)
print(aretha)     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    
    
    

