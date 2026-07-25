import numpy as np

rainfall_mm = np.array([
    [45, 60, 120, 210, 180, 90],    # Bogota
    [70, 95, 160, 240, 200, 110],   # Medellin
    [10, 15, 30, 60, 40, 20],       # Cali
    [90, 130, 200, 260, 220, 150],  # Barranquilla
])

# 1. Boolean mask over the whole 2D array
above_100 = rainfall_mm > 100

# 2. Row slicing — one city, all months
medellin_row = rainfall_mm[1, :]

# 3. Column slicing — one month, all cities
month_4 = rainfall_mm[:, 3]

# 4. Row-wise mean, then broadcast subtraction to center each row
row_means = rainfall_mm.mean(axis=1, keepdims=True)
centered = rainfall_mm - row_means

# 5. Row-wise std dev — one number per city
row_std = rainfall_mm.std(axis=1)

#EXERCISE
"""
Build a rainfall array like the one above for 4 Colombian cities over 6 months.
#1 Use a boolean mask to flag every city-month combination above 200mm.
#2 Slice out just one city's row and compute its 6-month average.
#3 Center each city's row by subtracting that city's own row-wise mean, using broadcasting.
#4 Open: which city has the most volatile rainfall (highest std dev)? If you were building a 
crop-insurance risk model, would that matter — and why?
"""
rainfall_mm = np.array([
    [45, 60, 120, 210, 180, 90],    # Bogota
    [70, 95, 160, 240, 200, 110],   # Medellin
    [10, 15, 30, 60, 40, 20],       # Cali
    [90, 130, 200, 260, 220, 150],  # Barranquilla
])
#1
above_200 = rainfall_mm > 200

#2
avg_bogota_row = rainfall_mm[0,:].mean()
print(f"The average mm reinfall in Bogotá is:\n{avg_bogota_row}")

#3
rain_avg = rainfall_mm.mean(axis=1, keepdims=True)
centered_mm = np.round(rainfall_mm - rain_avg, 2)
print(f"Centered rainfall:\n{centered_mm}")

#4
cities = ["Bogota", "Medellin", "Cali", "Barranquilla"]
rain_dev = np.round(rainfall_mm.std(axis=1),2)
most_volatile = cities[np.argmax(rain_dev)]
print(f"Most volatile city:\n{most_volatile} ({rain_dev.max()} mm std dev)")
"""
It would matter because a city with high std dev has unpredictable rainfall,
meaning crops could face both droughts and floods in the same year.
A risk model would charge higher premiums for volatile cities like Barranquilla
compared to stable ones like Cali.
"""