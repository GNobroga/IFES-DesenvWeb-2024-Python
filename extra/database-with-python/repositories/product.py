from sqlite3 import Connection
from typing import Optional, List
from entities import Product
from sql import *


class ProductRepository(object):
    
    def __init__(self, connection: Connection):
        self.connection = connection
        
    def create(self, product: Product) -> Optional[Product]:
        try:
            result = self.connection.execute(CREATE_PRODUCT_SQL, (product.name, product.description, product.stock, product.price))
            self.connection.commit()
            if result.rowcount:
                product.id = result.lastrowid
                return product 
            else:
                raise Exception()
        except:
            print('Não foi possível salvar o produto')
            self.connection.rollback()
            
    def findAll(self) -> List[Product]:
        return [Product(*values) for values in self.connection.execute(GET_PRODUCT_SQL).fetchall()] 
     
     
    def findById(self, id: int) -> Optional[Product]:
        return Product(*self.connection.execute(GET_PRODUCT_BY_ID_SQL, tuple([id])).fetchone())
    
    def deleteByid(self, id: int) -> bool:
       try:
            result = self.connection.execute(DELETE_PRODUCT_BY_ID_SQL, tuple([id]))
            self.connection.commit()
            return result.rowcount > 0
       except:
            self.connection.rollback()
            return False
        
    def update(self, product: Product) -> bool:
        try:
            result = self.connection.execute(UPDATE_PRODUCT_SQL, (product.name, product.description, product.stock, product.price, product.id))
            self.connection.commit()
            return result.rowcount > 0
        except:
            self.connection.rollback()
            return False
            
    def count(self):
        return self.connection.execute(GET_PRODUCT_COUNT_SQL).fetchone()[0]