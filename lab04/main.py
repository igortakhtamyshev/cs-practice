import sys
from stats import average_by_city, read_valid, warmest_city

def main():
  
    lines = sys.stdin.read().splitlines()
    
 
    valid_records, error_count = read_valid(lines)
    
  
    avg_cities = average_by_city(valid_records)
    best_city = warmest_city(valid_records)
    
  
    print(len(valid_records))
    
   
    print(error_count)
    
    
    if best_city:
        print(f"{avg_cities[best_city]:.1f}")
    else:
        print("0.0")

if __name__ == "__main__":
    main()
