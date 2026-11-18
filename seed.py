from decimal import Decimal
from database import SessionLocal
from use_case import create_user, create_order

session = SessionLocal()

# Создаем 3-х пользователей
u1 = create_user(session, "alice@example.com", Decimal("1000.00"))
u2 = create_user(session, "bob@example.com", Decimal("500.00"))
u3 = create_user(session, "charlie@example.com", Decimal("200.00"))

# Создаем заказы для них
create_order(session, u1.id, Decimal("100.00"))
create_order(session, u1.id, Decimal("150.00"))
create_order(session, u2.id, Decimal("50.00"))

session.close()
print("Данные добавлены: 3 пользователя и 3 заказа")