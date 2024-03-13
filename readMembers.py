from connect import *


def readMember():
    try:
        dbCon, dbCursor = db_access()
        dbCursor.execute("SELECT * FROM members")
        all_members = dbCursor.fetchall()

        if all_members:
            print("*" * 110)  # formated output
            print(f"MemberID{'':<3}|Firstname{'':<25}|Lastname{'':<24}|Email{'':<10}")
            print("*" * 110)

            for member in all_members:
                print(f"{member[0]:<11}|{member[1]:<34}|{member[2]:<32}|{member[3]:<10}")
                print("-" * 110)

    except sql.OperationalError as oe:
        print(f"Failed to read: {oe}")


if __name__ == "__main__":
    readMember()
