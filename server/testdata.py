# Эта функция выполняет ряд операторов SQL INSERT, помещая образцы данных в каждую из таблиц.
# это сразу же даст нам несколько записей, которые помогут разработать пользовательский интерфейс нашего клиентского приложения.

def populate_db(conn):
    cur = conn.cursor()

    # Populate lookup tables
    conditions = {'F': 'Fine/Like New',
                  'NF': 'Near Fine',
                  'VG': 'Very Good',
                  'G': 'Good',
                  'FR': 'Fair',
                  'P': 'Poor'}
    for code, cond in conditions.items():
        cur.execute(f"INSERT INTO Conditions(Code, Condition) "
                    f"values('{code}', '{cond}')")

    formats = ['Hardcover', 'Paperback', 'Oversized', 'Pamphlet', 'E-book']
    for item in formats:
        cur.execute(f"INSERT INTO Formats(Format) values('{item}')")

    categories = ['Computers & Tech',
                  'Biographies',
                  'Sci-Fi & Fantasy',
                  'Arts & Music',
                  'History',
                  'Fantasy'
                  ]
    for item in categories:
        cur.execute(f"INSERT INTO Categories(Category) values('{item}')")

    cur.execute(f"INSERT INTO Publishers(Publisher) values('No Starch Press')")
    cur.execute(f"INSERT INTO Publishers(Publisher) values('Del Rey Books')")
    conn.commit()

    # Populate main table
    cur.execute("INSERT INTO Books(Title, Author, IsFiction, "
                "Category, DateAcquired, Condition, Location) "
                "values('Harry Potter', 'Rowling', 0, "
                "'Fantasy', '2011-12-18', 'NF', 'A3')")
    cur.execute("INSERT INTO Books(Title, Author, Publisher, "
                "ISBN, IsFiction, Category, Format) "
                "values('I Robot', 'Isaac Asimov', 'Del Rey Books', "
                "'055338256X', 1, 'Sci-Fi & Fantasy', 'Paperback')")
    cur.execute("INSERT INTO Books(Title, Author, ISBN, IsFiction, Category) "
                "values('The C Programming Language', 'Kernighan & Ritchie', "
                "'0131103628', 0, 'Computers & Tech')")
    conn.commit()

    cur.execute(f"INSERT INTO Users(Username, Password) values('admin', '')")
    conn.commit()
