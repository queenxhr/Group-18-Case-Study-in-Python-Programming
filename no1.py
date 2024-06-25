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
