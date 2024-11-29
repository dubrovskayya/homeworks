
from sqlalchemy import create_engine, text
import sqlalchemy

# connecting to database
my_connection = "mssql+pyodbc://DESKTOP-PS54808\\SQLEXPRESS/master?driver=ODBC+Driver+17+for+SQL+Server"
eng = create_engine(my_connection)

try:
    #adding new database
    with eng.connect() as connect:
        connect.execution_options(isolation_level="AUTOCOMMIT")
        connect.execute(text("CREATE DATABASE NEWLibrary"))
        print('DB Library added!')

    # connecting to new database
    new_connection = "mssql+pyodbc://DESKTOP-PS54808\\SQLEXPRESS/NEWLibrary?driver=ODBC+Driver+17+for+SQL+Server"
    eng = create_engine(new_connection)

    # sql script for creating tables
    add_books = """
    CREATE TABLE Books (
        BookID INT PRIMARY KEY, 
        Title VARCHAR(255) NOT NULL,
        Author VARCHAR(255) NOT NULL,
        PublishedYear INT CHECK (PublishedYear > 1800)
    );
    """

    add_borrowers = """
    CREATE TABLE Borrowers (
        BorrowerID INT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Email VARCHAR(255) UNIQUE
    );
    """

    add_loans = """
    CREATE TABLE Loans (
        LoanID INT PRIMARY KEY,
        BookID INT NOT NULL,
        BorrowerID INT NOT NULL,
        LoanDate DATE NOT NULL,
        ReturnDate DATE ,
        FOREIGN KEY (BookID) REFERENCES Books(BookID),
        FOREIGN KEY (BorrowerID) REFERENCES Borrowers(BorrowerID)
    );
    """

    # transaction for creating tables
    with eng.connect() as connect:
        with connect.begin():  # начинаем транзакцию
            connect.execute(text(add_books))
            connect.execute(text(add_borrowers))
            connect.execute(text(add_loans))
            print("Tables added!")

    #sql script for adding data
    inserting_books = """
    INSERT INTO Books (BookID, Title, Author, PublishedYear)
    VALUES
        (1, 'The Sorrows of Satan', 'Marie Corelli', 1895),
        (2, 'The Man Who Laughs', 'Victor Hugo', 1869),
        (3, 'Moby-Dick', 'Herman Melville', 1851);
    """

    inserting_borrowers = """
    INSERT INTO Borrowers (BorrowerID, Name, Email)
    VALUES
        (1, 'Alice', 'alice@example.com'),
        (2, 'Bob', 'bob@example.com'),
        (3, 'Charlie', 'charlie@example.com');
    """

    inserting_loans = """
    INSERT INTO Loans (LoanID, BookID, BorrowerID, LoanDate, ReturnDate)
    VALUES
        (1, 1, 1, '2024-10-10', '2024-10-20'),
        (2, 2, 2, '2024-10-12', '2024-10-22'),
        (3, 3, 3, '2024-10-15', '2024-10-25');
    """
    #transaction for adding data
    with eng.connect() as connect:
        with connect.begin():

            connect.execute(text(inserting_books))
            connect.execute(text(inserting_borrowers))
            connect.execute(text(inserting_loans))
            print('Data added!')

except sqlalchemy.exc.OperationalError as e:
    print(f'OperationalError: {e}')
except sqlalchemy.exc.ProgrammingError as e:
    print(f'ProgrammingError: {e}')
except sqlalchemy.exc.IntegrityError as e:
    print(f'IntegrityError: {e}')

