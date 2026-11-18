from sqlalchemy import select, event
from sqlalchemy.orm import selectinload
from database import SessionLocal, engine
from models import User

def test_n_plus_1():
    session = SessionLocal()
    
    query_count = 0
    @event.listens_for(engine, "before_cursor_execute")
    def count_queries(conn, cursor, statement, parameters, context, executemany):
        nonlocal query_count
        query_count += 1

    print("\n--- Наивный запрос (N+1) ---")
    query_count = 0
    users = session.scalars(select(User)).all()
    for u in users:
        _ = [o.amount for o in u.orders]
    print(f"Количество запросов: {query_count}")

    print("\n--- С selectinload (Исправлено) ---")
    query_count = 0
    users = session.scalars(select(User).options(selectinload(User.orders))).all()
    for u in users:
        _ = [o.amount for o in u.orders]
    print(f"Количество запросов: {query_count}")

if __name__ == "__main__":
    test_n_plus_1()