#!/usr/bin/env python
# coding: utf-8

# # Import required libraries

# In[11]:


from PIL import Image,ImageFilter,ImageOps
import numpy as np
import matplotlib.pyplot as plt


# # Image loading

# In[12]:


image=Image.open('buddha pfp.png')
image.show()


# # Image manipulation 

# In[13]:


out1=image.resize((200,200))
out1.save("resize.jpg")


# In[14]:


out2=ImageOps.grayscale(image)
out2.save("grayscale.jpg")


# In[15]:


out3=out2.filter(ImageFilter.GaussianBlur(radius=2))
out3.save('GaussianBlur.jpg')


# In[16]:


out4=image.filter(ImageFilter.FIND_EDGES)
out4.save("EdgeDetection.jpg")


# # Histogram analysis

# In[17]:


image=image.convert('RGB')
red,green,blue=image.split()
def calculate_histogram(channel):
    histogram, bin_edges = np.histogram(np.array(channel).flatten(), bins=256, range=(0, 255))
    return histogram

# Calculate histograms for each channel
red_hist = calculate_histogram(red)
green_hist = calculate_histogram(green)
blue_hist = calculate_histogram(blue)

# Plotting the histograms in a single graph
plt.title("Colour Histogram")
plt.xlabel("bins")
plt.ylabel("# of Pixels")

# Plot each channel with different colors
plt.plot(red_hist, color='red', label='Red')
plt.plot(green_hist, color='green', label='Green')
plt.plot(blue_hist, color='blue', label='Blue')

plt.xlim([0, 255])
plt.legend()
plt.show()


# In[18]:


plt.hist(red_hist,color='red',label='red')
plt.hist(blue_hist,color='blue',label='blue')
plt.hist(green_hist,color='green',label='green')
plt.title("Colour Histogram")
plt.xlabel("Colour Value Range")
plt.ylabel("# of Pixels")
plt.legend()
plt.show()

