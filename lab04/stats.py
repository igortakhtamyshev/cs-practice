def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}")
    city, temp_str, date = parts
    if not city or not date:
        raise ValueError("Город или дата не могут быть пустыми")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура '{temp_str}' не является числом")
    return {"city": city, "temp": temp, "date": date}

def read_valid(lines: list[str]) -> tuple[list[dict], int]:
    valid_records = []
    error_count = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            error_count += 1
    return valid_records, error_count

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for record in records:
        city = record["city"]
        total[city] = total.get(city, 0) + record["temp"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}

def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""
    averages = average_by_city(records)
    sorted_cities = sorted(averages.keys())
    best_city = sorted_cities[0]
    max_temp = averages[best_city]
    for city in sorted_cities[1:]:
        if averages[city] > max_temp:
            max_temp = averages[city]
            best_city = city
    return best_city


