from connect import *
"Objectives"
"" ''  # Import connect module
"" ''  # Create a function to delete record(s) in a table in a database
"" ''  # Use try and except to handle error(s)
"" ''  # Use the execute method from the cursor object to run sql statement
"" ''  # Notes
# The SQL statement may be parametrized (i. e. placeholders instead of SQL literals).
"" ''
# A parameter specifies the value a particular field must contain when carrying out a query.
"" ''


def delete_song():
    try:
        dbCon, dbCursor = db_access()
        song_id = int(input("Enter the song ID to delete a song: "))
        dbCursor.execute("SELECT * FROM songs WHERE SongID = ?", (song_id,))

        row = dbCursor.fetchone()

        if row == None:
            print(f"No record with {song_id} exists")

        else:
            dbCursor.execute("DELETE FROM songs WHERE SongID = ?", (song_id,))
            dbCon.commit()
            print(f"The record with the SongID {song_id} has been removed")

    except sql.OperationalError as oe:
        print(f"Error due to: {oe}")


if __name__ == "__main__":
    delete_song()
