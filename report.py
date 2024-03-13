from connect import *

# Create a function to run sql statements to generate different type of reports
def report():
    try:
        dbCon, dbCursor = db_access()

        search_field = input("Search by SongID, Title, Artist, or Genre: ")

        if search_field == "SongID":
            try:
                song_id = int(input("Enter SongID: "))
                dbCursor.execute("SELECT * FROM songs WHERE SongID = ?", (song_id,))
                row = dbCursor.fetchone()

                if row is None:
                    print(f"No record with SongID {song_id} exists in the songs table")
                else:
                    print(row)  # Print the single record found as per song_id
            except ValueError:
                print("Invalid input. Please enter a numeric SongID.")

        elif search_field in ["Title", "Artist", "Genre"]:
            search_term = input(f"Enter the value for the field {search_field}: ")
            dbCursor.execute(f"SELECT * FROM songs WHERE {search_field} LIKE '%{search_term}%'")
            rows = dbCursor.fetchall()

            if not rows:
                print(f"No record with field {search_field} matching {search_term} in the songs table")
            else:
                # Display all matched records from the songs table
                for record in rows:
                    print(record)

    except sql.OperationalError as oe:
        print(f"Search error: {oe}")


if __name__ == "__main__":
    report()