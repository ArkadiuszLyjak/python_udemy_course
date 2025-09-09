def analyse_temperature(temp_list: list[float]) -> tuple[float, float, float]:
    """Calculate average, minimum and maximum temperatures.
    
    Args:
        temp_list: List of temperature values
        
    Returns:
        Tuple containing (average, minimum, maximum) temperatures
    """
    avg = sum(temp_list) / len(temp_list)
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    return avg, min_temp, max_temp


temperatures = []

while True:
    temp = input("Podaj temperature (lub 'exit' aby zakończyć): ")
    if temp.lower() == "exit":
        break
    try:
        temperatures.append(float(temp))
    except ValueError:
        print("Proszę podać poprawną liczbę")

if temperatures:
    avg_temp, min_temp, max_temp = analyse_temperature(temperatures)
    print(f"\nStatystyki temperatur:")
    print(f"Średnia: {avg_temp:.2f}°C")
    print(f"Minimalna: {min_temp}°C")
    print(f"Maksymalna: {max_temp}°C")
else:
    print("Brak wprowadzonych temperatur.")
