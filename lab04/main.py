import sys from stats import average_by_city, read_valid, warmest_city
def main(): input_data = sys.stdin.read() if not input_data: return
lines = input_data.splitlines()


valid_records = read_valid(lines)


parsed_count = len(valid_records)
empty_count = sum(1 for line in lines if not line)
error_count = len(lines) - parsed_count - empty_count


print(parsed_count)


print(error_count)


if parsed_count > 0:
    best_city = warmest_city(valid_records)
    averages = average_by_city(valid_records)
    print(f"{averages[best_city]:.1f}")
if name == "main": main()
