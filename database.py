import aiosqlite

async def init_db():
    async with aiosqlite.connect('users.db') as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE,
                username TEXT
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS finances (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER,
                category_1 TEXT,
                category_2 TEXT,
                category_3 TEXT,
                expenses_1 REAL,
                expenses_2 REAL,
                expenses_3 REAL
            )
        ''')
        await db.commit()
