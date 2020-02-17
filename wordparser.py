#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import docx
import requests


# In[ ]:





# In[ ]:


def getdoc(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    alltext = ''.join(fullText)
    
    return alltext


# In[ ]:





# In[ ]:


def word_to_pdf(docfile):
    with open(docfile, 'rb') as docx:
        res = requests.post(url='http://converter-eval.plutext.com:80/v1/00000000-0000-0000-0000-000000000000/convert',
                          data=docx,
                          headers={'Content-Type': 'application/octet-stream'})
        f = open('./some.pdf', 'wb')
        f.write(res.content)
		f.close()

