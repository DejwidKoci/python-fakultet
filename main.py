import time

# Liczba sekund od 1 stycznia 1970 roku, czyli tzw. Unix timestamp
timestamp = time.time()

# Przekształcanie timestamp na lokalny czas
local_time = time.localtime(timestamp)

# Sformatuj czas w czytelny sposób
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

print("Aktualna data i godzina:", formatted_time)
