def parse_record(line: str) -> dict:
    city, temp, date = line.split(";")
    return {"city": city, "temp": float(temp), "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        valid_records.append(parse_record(line))
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for record in records:
        city = record["city"]
        total[city] = total.get(city, 0) + record["temp"]
        count[city] = count.get(city, 0) + 1
    return {city: total[city] / count[city] for city in total}

def warmest_city(records: list[dict]) -> str:
    best = ""
    for record in records:
        city = record["city"]
        if best == "" or record["temp"] > 0: 
            best = city
    return best
