import sys
import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship

if os.path.exists("/data"):
    db_path = "sqlite:////data/mall.db"
    print(">>> 偵測到 Docker 環境，資料庫將儲存於 /data/mall.db")
else:
    db_path = "sqlite:///mall.db"
    print(">>> 偵測到本機環境，資料庫將儲存於當前目錄 mall.db")

engine = create_engine(db_path, echo=False)


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    gender = Column(String)
    orders = relationship("Order", back_populates="customer")


class Store(Base):
    __tablename__ = "stores"
    store_id = Column(Integer, primary_key=True, autoincrement=True)
    store_name = Column(String)
    address = Column(String)
    orders = relationship("Order", back_populates="store")


class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String)
    item_price = Column(Integer)
    orders = relationship("Order", back_populates="item")


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    store_id = Column(Integer, ForeignKey("stores.store_id"))
    item_id = Column(Integer, ForeignKey("items.item_id"))
    price = Column(Integer)
    count = Column(Integer)

    customer = relationship("Customer", back_populates="orders")
    store = relationship("Store", back_populates="orders")
    item = relationship("Item", back_populates="orders")


if __name__ == "__main__":

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        name = input("請輸入名字: ")
    except EOFError:
        print("\n[錯誤] 無法讀取輸入。如果您使用 Docker，請確認指令包含 '-it' 參數。")
        sys.exit(1)

    gender = ""
    while gender != "男" and gender != "女":
        if gender != "":
            print("性別錯誤，請輸入 '男' 或 '女'。")
        try:
            gender = input("性別(男 / 女): ")
        except EOFError:
            sys.exit(1)

    new_customer = Customer(name=name, gender=gender)
    session.add(new_customer)
    session.commit()

    print(f"成功寫入！顧客 ID: {new_customer.customer_id}, 姓名: {new_customer.name}")

    saved_customer = session.get(Customer, new_customer.customer_id)

    if saved_customer:
        print(f"資料庫內確實有：{saved_customer.name} ({saved_customer.gender})")
    else:
        print("找不到資料")
