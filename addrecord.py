from connect import *
"Objectives"
"" ''  # Import connect module
"" ''  # Create a function to add record(s) to a table in a database
"" ''  # Use try and except to handle error(s)
"" ''  # Use the execute method from the cursor object to run sql statement

"" ''  # Notes
# The SQL statement may be parametrized (i. e. placeholders instead of SQL literals).
"" ''
# A parameter specifies the value a particular field must contain when carrying out a query.
"" ''


def insert_record():
    try:
        dbCon, dbCursor = db_access()
        song_title = input("enter song title: ")
        song_artist = input("enter song artist: ")
        song_genre = input("enter song genre: ")

        dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES(?, ? ,?)",
                         (song_title, song_artist, song_genre))

        dbCon.commit()
        print(f"{song_title} inserted in the songs table")

    except sql.OperationalError as oe:
        print(f"Failed because {oe}")


if __name__ == "__main__":
    insert_record()
