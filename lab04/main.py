import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
valid_records = read_valid(lines)
avg_cities = average_by_city(valid_records)
best_city = warmest_city(valid_records)

print(len(valid_records))
print(0)
print(avg_cities[best_city])
