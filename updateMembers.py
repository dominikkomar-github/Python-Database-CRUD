from connect import *

def updateMember():
    try:
        dbCon, dbCursor = db_access()

        member_id = int(input("Enter member ID to update: "))

        # Check if the member exists before updating
        dbCursor.execute("SELECT * FROM members WHERE MemberID = ?", (member_id,))
        row = dbCursor.fetchone()

        if not row:  # Check if row is empty (no record found)
            raise ValueError(f"Member with ID {member_id} not found.")

        field_choices = {"1": "Firstname", "2": "Lastname", "3": "Email"}

        choice = input(f"Update (First Name, Last Name, email) (1/2/3): ")
        if choice in field_choices:
            new_value = input(f"Enter new {field_choices[choice]}: ")
            dbCursor.execute(f"UPDATE members SET {field_choices[choice]} = ? WHERE MemberID = ?",
                             (new_value, member_id))
            dbCon.commit()
            print("Member information updated successfully.")
        else:
            print("Invalid choice. Please try again.")

    except (ValueError, sql.OperationalError) as oe:
        print(f"Error: {oe}")


if __name__ == "__main__":
    updateMember()