from connect import *

# Create a function to update record(s) in a table in a database
def update_record():
    try:
        dbCon, dbCursor = db_access()

        # check if the SongID exists
        song_id = int(input("Enter SongID to update a record: "))
        dbCursor.execute("SELECT * FROM songs WHERE SongID = ?",(song_id))

        row = dbCursor.fetchone()

        if row == None:# if there is no match with the song_id provided
            print(f"No recod with SongID {song_id} exists in the table songs")

        else:# if there is a match with the song_id provided
            num_fields = input("Enter N to update one field or Y to update all fields: ").upper()

            if num_fields == "Y":
                # update all fields  
                song_title  = input("Enter value to update song title: ")
                song_artist = input("Enter value to update song artist: ")
                song_genre  = input("Enter value to update song genre: ")

                # perform update 
                dbCursor.execute("UPDATE songs SET Title =?, Artist=?, Genre=? WHERE SongID =?",(song_title,song_artist,song_genre, song_id))
                dbCon.commit()
                print(f"All fields in the record {song_id} updated in the songs table")

            elif num_fields == "N":
                #ask for the field to be updated 
                field_name = input("Enter the field (Title or Artist or Genre): ").title()
                if field_name not in ["Title", "Artist", "Genre"]:
                    print(f"Field {field_name} not a valid field name in the table")
                else:
                    #ask for the field value
                    field_value = input(f"Enter the value for the field {field_name}: ")
                    # perform update  on a specific field
                    dbCursor.execute(f"UPDATE songs SET {field_name} =? WHERE SongID =?", (field_value, song_id,))
                    dbCon.commit()
                    print(f"Record {song_id} updated in the songs table")
            else:
                print("Invalid choice, please enter Y or N")
    except sql.OperationalError as oe:
        print(f"Update failed: {oe}")
if __name__ == "__main__":
    update_record()
