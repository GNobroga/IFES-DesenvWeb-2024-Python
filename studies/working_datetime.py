from datetime import datetime as LocalDateTime, timedelta
from typing import Union, List

# birthDate = LocalDateTime(2000, 4, 10)
# diff = LocalDateTime.now() - birthDate 

# print(diff.days)


# birthDate = LocalDateTime(2001, 3, 13)
# diff = LocalDateTime.now() - birthDate 

# print(diff.days)

# def nooooooooooooooooooooooooooooooooooooooooooooooooooooooo(name: str, /) -> str:
#     print(name)


# print(nooooooooooooooooooooooooooooooooooooooooooooooooooooooo(name="GAbrile"))


print(list(filter(lambda x: x["value"] >= 50, [{ "name": "Vinho bosta e caro", "value": 50}, { "name": "Vinho bom e barato", "value": 20 }])))


print([ { "username:" f"user{n}"} for n in range(1, 11) if n % 2 == 0])