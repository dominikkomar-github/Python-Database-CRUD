from connect import *


def addMember():
    try:
        dbCon, dbCursor = db_access()
        name = input("enter new member name: ")
        surname = input("enter new member surname: ")
        email = input("enter new member email: ")

        dbCursor.execute("INSERT INTO members (Firstname, Lastname, Email) VALUES(?, ? ,?)",
                         (name, surname, email))

        dbCon.commit()
        print(f"{name} {surname} inserted in the Members table")

    except sql.OperationalError as oe:
        print(f"Failed because {oe}")


if __name__ == "__main__":
    addMember()
