# Metoda ala cron, zadanie ma wykonać się o określonej godzinie.


from datetime import datetime
from datetime import timedelta
import time

# Pobieram godzinę z pliku o której ma wykonać się zadanie
test = '23:01:10'
hour = int(test.split(":")[0])
minute = int(test.split(":")[1])
seconds = int(test.split(":")[2])


# Metoda sprawdza czy czas jest w przyszłości (w zakresie 24h)
# Jeżeli tak to zwraca czas w sekundach, jeżeli nie to dodaje dzień.
def future(current_time, time_to_check, DEBUG=False):
    if current_time > time_to_check :
        if DEBUG: print("DEBUG [ Time is in the past   ] >>> Current time: ",current_time, ", Time to check: ", time_to_check )
        return future(current_time, time_to_check.replace(day=current_time.day+1),DEBUG)
    else:
        seconds = time_to_check - current_time
        if DEBUG: print("DEBUG [ Time is in the future ] >>> Current time: ",current_time, ", Time to check: ", time_to_check)
        return seconds.total_seconds()

now = datetime.today()
# Podstawiamy aktualny czas względem godziny który chcemy sprwadzać jak się okaże żę godzina
# jest w czasie przesłym to ją uaktualnimy aż bedzie czasem aktualnym, tzn w przysłosci.
delay = datetime(now.year, now.month, now.day, hour, minute, seconds)

sec = future(now,delay,True)

time.sleep(sec)
print ("zakończenie skryptu: ",  datetime.today())