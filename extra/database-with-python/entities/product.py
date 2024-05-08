
from dataclasses import dataclass
from typing import Optional


@dataclass
class Product(object):
    id: Optional[int] = None
    name: str = None
    description: Optional[str] = None
    stock: int = None
    price: float = None
    
    def __repr__(self):
        return f"Id - {self.id} Nome - {self.name} Descrição - {self.description} Estoque - {self.stock} Preço - {self.price}"
