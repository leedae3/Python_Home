#!/usr/bin/env python
# coding: utf-8

# In[2]:


cat test.dat


# In[5]:


pwd


# In[17]:


fread = None

try :
    fread = open('test.dat', 'r')
    #result = fread.read()
    # result = fread.readline()     #초기값
    # while result :
    #     print(result, end='')
    #     result = fread.readline()
    for line in fread.readlines():
        print(line, end='')
except :
    print('File not found.')
finally :
    fread.close()


# In[5]:


poet = """
죽는 날까지 하늘을 우러러
한 점 부끄럼이 없기를,
잎새에 이는 바람에도
나는 괴로워했다.
별을 노래하는 마음으로
모든 죽어 가는 것을 사랑해야지
그리고 나한테 주어진 길을
걸어가야겠다.

오늘 밤에도 별이 바람에 스치운다.
"""


# In[6]:


fwrite = None
try:
    fwrite = open('서시.txt', 'w')
    fwrite.write(poet)
    print("file save successfully")
except Exception as err:
    print(err)
finally :
    fwrite.close()


# In[10]:


with open('서시.txt', 'rt') as fread :
    try :
        count = 1
        for line in fread.readlines() :
            print(f'{count} : {line}', end='')
            count += 1
    except :
        print('File not found')


# In[11]:


import json


# In[13]:


list_ = ['Hello, World', 5, True, 89.5]
type(list_)


# In[14]:


str_ = json.dumps(list_)
type(str_)


# In[15]:


print(str_)


# In[17]:


obj = json.loads(str_)
type(obj)


# In[18]:


obj[2]


# In[19]:


obj[0]


# In[20]:


student = {
    "hakbun" : "2023-003",
    "name" : "강동원",
    "age" : 24,
     "address" : "서울 은평구 응암동"
}
type(student)


# In[30]:


str_ = json.dumps(student, ensure_ascii=False, indent='\t')
type(str_)


# In[22]:


cat str_


# In[23]:


student


# In[24]:


str_


# In[29]:


print(str_)


# In[31]:


with open('student.dat', 'wt') as fwrite :
    fwrite.write(str_)
    print('File save successfully')


# In[38]:


with open ('student.dat', 'rt') as fread :
    result = fread.read()
    #print(type(result))
    obj = json.loads(result)
    #print(type(obj))
    print(f"name = {obj['name']}, age = {obj['age']}")


# In[45]:


with open('sungjuk.json', 'rt') as fread :
    result = json.load(fread)     #load = read() -> loads()
    #print(type(result))     #list
    #print(len(result))
    #print(type(result[0]))    #dict
    print(result[0]['irum'])


# In[46]:


import os


# In[47]:


print(os.name)


# In[49]:


print(os.getcwd())


# In[50]:


get_ipython().system('pwd')


# In[51]:


os.chdir('/')
print(os.getcwd())


# In[52]:


import sys


# In[53]:


print(f"version : {sys.version}")
print(f"version info : {sys.version_info}")
print(f"platform : {sys.platform}")


# In[54]:


import platform


# In[55]:


print(f"Platform Architecture : {platform.uname()}")


# In[56]:


import socket


# In[58]:


print(f"Host name : {socket.gethostname()}")


# In[59]:


hostname = socket.gethostname()
print(socket.gethostbyname(hostname))


# In[64]:


print(socket.gethostbyname('www.google.com'))


# In[65]:


get_ipython().system('pip list')


# In[67]:


get_ipython().system('pip install pymysql')


# In[68]:


get_ipython().system('pip install nbconvert')


# In[73]:


get_ipython().system('jupyter nbconvert --to script ./230922.ipynb')


# In[74]:


ls


# In[75]:


get_ipython().system('pwd')


# In[76]:


cd notebook


# In[77]:


cd /home/ubuntu/notebook


# In[78]:


get_ipython().system('pwd')


# In[80]:


jupyter nbconvert --to script 230922.ipynb


# In[ ]:




