#!/usr/bin/env python
# coding: utf-8

# # First Case Study : Miles Per Gallon

# In[ ]:

def main():
    total_miles = 0
    total_gallons = 0

    while True:
        gallons_used = float(input("Enter the gallons used (-1 to end): "))
        if gallons_used == -1:
            break

        miles_driven = float(input("Enter the miles driven: "))
        
        mpg = miles_driven / gallons_used
        print(f"The miles/gallon for this tank was {mpg:.6f}")

        total_miles += miles_driven
        total_gallons += gallons_used

    if total_gallons != 0:
        overall_avg_mpg = total_miles / total_gallons
        print(f"The overall average miles/gallon was {overall_avg_mpg:.6f}")
    else:
        print("No data to calculate overall average miles/gallon.")

if __name__ == "__main__":
    main()


# # Second Case Study : A Game of Chance - Crap

# In[ ]:





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

