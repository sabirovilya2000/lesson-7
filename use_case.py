from decimal import Decimal
from sqlalchemy.orm import Session
from models import User, Order

def create_user(session: Session, email: str, balance: Decimal) -> User:
    user = User(email=email, balance=balance)
    session.add(user)
    session.commit()
    return user

def get_user_by_email(session: Session, email: str) -> User | None:
    return session.query(User).filter(User.email == email).first()

def get_user_by_id(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)

def create_order(session: Session, user_id: int, amount: Decimal) -> Order:
    user = session.get(User, user_id)
    if not user: raise ValueError("User not found")
    if amount <= 0: raise ValueError("Amount must be positive")
    if user.balance < amount: raise ValueError("Insufficient funds")
    
    user.balance -= amount
    order = Order(user_id=user_id, amount=amount, status="pending")
    session.add(order)
    session.commit()
    return order

def create_order_with_error(session: Session, user_id: int, amount: Decimal):
    user = session.get(User, user_id)
    user.balance -= amount
    session.add(Order(user_id=user_id, amount=amount, status="pending"))
    raise Exception("Boom! Ошибка между списанием и созданием заказа")