from connect import *


def deleteMember():
    try:
        dbCon, dbCursor = db_access()
        member_id = int(input("Enter the member ID to delete a member: "))
        dbCursor.execute(
            "SELECT * FROM members WHERE MemberID = ?", (member_id,))

        row = dbCursor.fetchone()

        if row == None:
            print(f"No record with {member_id} exists")

        else:
            dbCursor.execute(
                "DELETE FROM members2 WHERE MemberID = ?", (member_id,))
            dbCon.commit()
            print(f"The record with the MemberID {member_id} has been removed")

    except sql.OperationalError as oe:
        print(f"Error due to: {oe}")


if __name__ == "__main__":
    deleteMember()
