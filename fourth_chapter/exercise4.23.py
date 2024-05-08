from datetime import datetime, timedelta

format = '%d/%m/%Y'

diff = (datetime.strptime('01/02/2022', format) - datetime.strptime('01/01/2022', format)).days

print(f'A diferença em dias é {diff}')