from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("CREATE TABLE users(id INT PRIMARYKEY NOT NULL, name VARCHAR(10) NOT NULL)"))
    result = conn.execute(text("INSERT INTO users(id, name) VALUES(1, 'Nithish'), (2, 'Jagan'), (3, 'rhanth')"))
    result = conn.execute(text("SELECT * FROM users"))
    

    print(result.fetchall())
    #[(1, nith), (2, jag), (3, rhnth)]
    # nith
    # error