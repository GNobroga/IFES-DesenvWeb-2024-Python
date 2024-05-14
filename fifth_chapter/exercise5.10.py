from typing import List, Any, Callable

class Stream:
    
    @classmethod
    def of(cls, *initialState: List[Any]):
        return cls(*initialState)
    
    def __init__(self, *initialState: List[Any]):
        self._initialState = initialState

    def transform_list(self, callback: Callable[[Any], Any]) -> 'Stream':
       self._initialState = list(map(callback, self._initialState))
       return self
       
    def filter(self, callback: Callable[[bool], Any]) -> 'Stream':
        self._initialState = list(filter(callback, self._initialState))
        return self
    
    def get_state(self):
        return self._initialState

stream = Stream.of(1, 2, 3, 4, 5)   

def por_extenso(n: int) -> str:
   names = { 0: 'Zero', 1: 'Um', 2: 'Dois', 3: 'Três', 4: 'Quatro', 5: 'Cinco', 6: 'Seis', 7: 'Sete', 8: 'Oito', 9: 'Nove' }
   if n in names:
       return names[n]
   return n

print(stream.transform_list(por_extenso).get_state())

