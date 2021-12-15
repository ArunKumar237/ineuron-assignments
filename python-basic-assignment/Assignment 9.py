#!/usr/bin/env python
# coding: utf-8

# Solutions for Python Basic Assignment - 9
# *****************************************

# In[ ]:


get_ipython().set_next_input('1. To what does a relative path refer');get_ipython().run_line_magic('pinfo', 'refer')

Ans:
    Relative path refers to the current working directory.


# In[ ]:


get_ipython().set_next_input('2. What does an absolute path start with your operating system');get_ipython().run_line_magic('pinfo', 'system')

Ans:
    "C:\" in windows operating system.
    "/" in Linux operating system.


# In[ ]:


get_ipython().set_next_input('3. What do the functions os.getcwd() and os.chdir() do');get_ipython().run_line_magic('pinfo', 'do')

Ans:
    os.getcwd() -  reponsible for getting the path of current working directory.
    os.chdir() - responsible for changing the path from current working directory to other directory.


# In[ ]:


get_ipython().set_next_input('4. What are the . and .. folders');get_ipython().run_line_magic('pinfo', 'folders')

Ans:
    Both are comes under relative path.
    '.' refers to present working directory i.e current directory's relative path.
    '..' refers to parent directory(folder) of relative path.


# In[ ]:


get_ipython().set_next_input('5. In C:\\bacon\\eggs\\spam.txt, which part is the dir name, and which part is the base name');get_ipython().run_line_magic('pinfo', 'name')

Ans:
    'C:\bacon\eggs' - is the dir name.
    'spam.txt' - is the base name.


# In[ ]:


get_ipython().set_next_input('6. What are the three “mode” arguments that can be passed to the open() function');get_ipython().run_line_magic('pinfo', 'function')

Ans:
    'r' for read mode, 'w' for write mode, and 'a' for append mode. 
        these are the three "mode" arguments that can be passed to open() function.


# In[ ]:


get_ipython().set_next_input('7. What happens if an existing file is opened in write mode');get_ipython().run_line_magic('pinfo', 'mode')

Ans:
    An existing file opened in write mode will get erased and completely overwritten.


# In[ ]:


8. How do you tell the difference between read() and readlines()?

Ans:
    read() - used to read the contents of the file and return it in a single line string.
    readlines() - used to read the contents of the file and return it in a line after line manner as it is in original file.


# In[ ]:


get_ipython().set_next_input('9. What data structure does a shelf value resemble');get_ipython().run_line_magic('pinfo', 'resemble')

Ans:
    It resembles as a dictionary data type value.

