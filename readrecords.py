from connect import *

def read_all_songs():
    try:
        dbCon, dbCursor = db_access()

        dbCursor.execute("SELECT * FROM songs")
        all_songs = dbCursor.fetchall()

        if all_songs:
            print("*" * 100)  # formated output
            print(f"SongID{'':<3}|Title{'':<25}|Artist{'':<24}|Genre{'':<10}")
            print("*" * 100)

            for aSong in all_songs:
                # print(f"{aSong[0]:<9}|{aSong[1]:<30}|{aSong[2]:<30}|{aSong[3]:<10}")
                print(aSong)
                print("-" * 100)

    except sql.OperationalError as oe:
        print(f"Failed to read: {oe}")


if __name__ == "__main__":
    read_all_songs()
