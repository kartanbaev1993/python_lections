from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# driver://user:password@host:port/db_name
db_url = 'postgresql://user:1@127.0.0.1:5432/sqlalchemy_test'
engine = create_engine(db_url)
# podklyuchenie k baze dannyh

Base = declarative_base()
# bazovyi klass dlya tablic

# sozdaem tablicu
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"({self.id} -> {self.title})"

Base.metadata.create_all(bind=engine)
# zapisyvaem tablicu v bazu dannyh

SessionLocal = sessionmaker(bind=engine)
# sozdaem klass dlya sessii (odin ob'ekt ot dannogo klassa - odna sessiya)

session = SessionLocal()
# sozdaem sessiyu

new_product = Product(title='product1', price=120)
# sozdaem produkt (zapis' v tablicu)
# dlya ORM sozdaem zapros na zapis' v tablicu

session.add(new_product)
# dobavlyaem zapros v sessiyu

session.commit()
# otpravlyaem nabor zaprosov  bazu dannyh

products = session.query(Product).all()
# poluchaem vse zapisi iz tablicy bazy product
print(products)

res = session.query(Product).filter(Product.price > 100).all()
# poluchaem vse zapisi iz tablicy product u kotoryh cena bol'she 100
print(res)


product3 = session.query(Product).get(3)
# poluchaem product pod id 3
print(product3)

product4 = session.query(Product).get(4)
# poluchaem produkt pod id 4 
session.delete(product4)
# udalyaem product
session.commit()
# sohranyaem izmeneniya v baze dannyh

product3.title = 'new title'
product3.price = 100
# izmenyaem produkt
session.commit()
# sohranyaem izmeneniya v baze dannyh