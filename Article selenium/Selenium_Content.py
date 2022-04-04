#!/usr/bin/env python
# coding: utf-8

# ### Media Realease Article 

# In[47]:


import selenium
from selenium import webdriver as wb


webd = wb.Chrome('chromedriver.exe')

webd.get('https://www.credit-suisse.com/about-us/en.html')


# In[48]:


cookies = webd.find_element_by_id('onetrust-accept-btn-handler')


# In[49]:


cookies.click()


# In[50]:


menu = webd.find_element_by_xpath('/html/body/section/div[1]/div[2]/div/div/a')


# In[51]:


menu.click()


# In[55]:


media_news = webd.find_element_by_xpath('/html/body/section/div[1]/div[4]/nav/div[4]/div[2]/ul/li[2]')


# In[56]:


media_news.click()


# In[57]:


media = webd.find_element_by_xpath('/html/body/section/div[1]/div[4]/nav/div[4]/div[2]/div/ul/li[1]')


# In[58]:


media.click()


# In[59]:


discover = webd.find_element_by_xpath('/html/body/section/div[1]/div[4]/nav/div[4]/div[1]/div/a')


# In[60]:


discover.click()


# In[ ]:





# In[ ]:





# In[23]:


# for trial

#import selenium
#from selenium import webdriver as wb


#webd = wb.Chrome('chromedriver.exe')

#webd.get('https://www.credit-suisse.com/about-us-news/en/articles/media-releases/csg-appoints-head-corp-comms-202203.html')


# In[24]:


#big = webd.find_element_by_class_name('mod_text_component')


# In[31]:


#cig = big.text.split('\n')


# In[32]:


#cig


# In[28]:


#cig.split('\n')


# In[29]:


#small = webd.find_element_by_class_name('component_standard_content')


# In[30]:


#small.text


# In[156]:



#tiles = webd.find_elements_by_class_name('m-article-listing__article')


# In[48]:


#list_of_links = []



#for i in tiles:
#    t2 = t1.find_element_by_class_name('a-link')
#    list_of_links.append(t2.get_property('href'))


# In[49]:


# for checking

#t2.text


# In[50]:


# for checking

#t2.get_property('href')


# In[61]:


list_of_links = []
condition = True
while condition:
    tiles = webd.find_elements_by_class_name('m-article-listing__article')
    for i in tiles:
        t2 = i.find_element_by_class_name('a-link')
        list_of_links.append(t2.get_property('href'))
    try:
        webd.find_element_by_xpath('/html/body/main/div[1]/section[2]/div[3]/div[2]/a').click()
                                    
    
    except:
        condition = False
    


# In[62]:


#webd.find_element_by_xpath('/html/body/main/div[1]/section[2]/div[3]/div[2]/a').click()


# In[63]:


list_of_links


# In[64]:


len(list_of_links)


# In[65]:


len(list_of_links)


# In[66]:


from tqdm import tqdm

alldetails = []

for i in tqdm(list_of_links):
    try:
        webd.get(i)
        Title = webd.find_element_by_class_name('mod_media_release_title').text
        Subtitle = webd.find_element_by_class_name('mod_page_abstract').text
        Location = webd.find_element_by_class_name('mod_media_release_article_byline_location').text
        Date = webd.find_element_by_class_name('mod_media_release_article_byline_date').text
        Content = webd.find_element_by_class_name('mod_text_component').text
        #Contact_Names = webd.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[2]/div/div/div/address/p[1]/text()[1]').text 
        #Contact_Number = webd.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[2]/div/div/div/address/p[1]/text()[2]').text.split('Tel:') 
        #Email = webd.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[2]/div/div/div/address/p[1]/text()[3]').text.lsplit('Email:') 
    
        tempJ = {'Title': Title, 'Subtitle': Subtitle, 'Location': Location, 'Date': Date, 'Content' : Content, 'Link': i}
    
    
        alldetails.append(tempJ)
    
    except Exception as e:
        print("Exception", e)


# In[ ]:





# In[67]:


import pandas as pd


# In[68]:


df = pd.DataFrame(alldetails)
df.head()


# In[69]:


df.to_csv('content_article.csv') 

