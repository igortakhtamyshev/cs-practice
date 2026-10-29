def parse_record(line: str) -> dict:
    parts = line.split(";")
    
    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей: {len(parts)}. Ожидается 3.")
    
    # ИСПРАВЛЕНО: добавляем .strip() для очистки от лишних пробелов по краям
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    if not city or not date:
        raise ValueError("Пустой город или дата.")
        
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура '{temp_str}' не является числом.")
        
    return {"city": city, "temperature": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    
    for line in lines:
        if not line:
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
            
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    
    for rec in records:
        city = rec["city"]
        totals[city] = totals.get(city, 0.0) + rec["temperature"]
        counts[city] = counts.get(city, 0) + 1
        
    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)
        
    return averages

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    
    if not averages:
        return ""
        
    best_city = ""
    best_temp = float("-inf")
    
    for city, temp in averages.items():
        if temp > best_temp:
            best_temp = temp
            best_city = city
        elif temp == best_temp:
            if best_city == "" or city < best_city:
                best_city = city
                
    return best_city



