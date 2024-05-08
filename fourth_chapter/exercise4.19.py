from datetime import datetime
date_string = "2022-01-15T12:00"

print(datetime.strptime(date_string, '%Y-%m-%dT%H:%M'))