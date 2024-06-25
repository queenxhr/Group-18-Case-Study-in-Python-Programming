# # Third Case Study : COVID 19 Infection Statistic

# In[1]:


import statistics


# In[2]:


# Data on the number of newly infected patients per day
data = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]


# In[3]:


minimum = min(data)
maximum = max(data)
range = maximum - minimum
mean = statistics.mean(data)
median = statistics.median(data)
variance = statistics.variance(data)
standard_deviation = statistics.stdev(data)


# In[4]:


# Output
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standarad Deviation: {standard_deviation}")

