def parse_record(line: str) -> dict:

    parts = line.split(';')
    
  
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}")
        
    city, temp_str, date = parts
    
    # Проверка на пустые город или дату
    if not city.strip() or not date.strip():
        raise ValueError("Город или дата не могут быть пустыми")
        
    # Проверка температуры на число
    try:
        # strip() на всякий случай убирает лишние пробелы вокруг числа
        temp = float(temp_str.strip())
    except ValueError:
        raise ValueError(f"Температура '{temp_str}' не является числом")
        
    return {"city": city.strip(), "temp": temp, "date": date.strip()}


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
            # Если parse_record выдал ошибку — увеличиваем счетчик
            error_count += 1
            
    return valid_records, error_count


def average_by_city(records: list[dict]) -> dict:
   
    total = {}
    count = {}
    
    for record in records:
        city = record["city"]
        temp = record["temp"]
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1
        
    averages = {}
    for city in total:
        averages[city] = round(total[city] / count[city], 1)
        
    return averages


def warmest_city(records: list[dict]) -> str:
   
    if not records:
        return ""
        
    averages = average_by_city(records)
    
   
    
    best_city = sorted_cities[0]
    max_temp = averages[best_city]
    
    for city in sorted_cities[1:]:
        if averages[city] > max_temp:
            max_temp = averages[city]
            best_city = city
            
    return best_city


