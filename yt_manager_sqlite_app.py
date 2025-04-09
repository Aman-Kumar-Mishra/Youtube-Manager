#youtube-manager application (using SQLite)

import sqlite3

#connect to SQLite databse
conn = sqlite3.connect("yt_videos.db")

#create cursor object
cursor = conn.cursor()

#execute database queries using cursor
#create table
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Videos (
               Id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
                )
''')

#fix conetent indexing
def fix_indices():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS New_Videos (
               Id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
                )
    ''')
    cursor.execute("INSERT INTO New_Videos (name, time) SELECT name, time FROM Videos")
    conn.commit()
    cursor.execute("DROP TABLE Videos")
    conn.commit()
    cursor.execute("ALTER TABLE New_Videos RENAME TO Videos")
    conn.commit()

#method for listing videos
def list_all_videos():
    cursor.execute("SELECT * FROM Videos")
    rows = cursor.fetchall()
    # print(rows)
    print("\n"+"*"*50+'\n')
    for row in rows:
        print(f"{row[0]}. title: {row[1]}, duration: {row[2]}\n")
    print('*'*50)

#method for adding video
def add_video():
    name = input("enter name of the video: ")
    time = input("enter time of the video: ")
    cursor.execute("INSERT INTO Videos (name, time) VALUES (?, ?)",(name, time))
    conn.commit()

#method for updating video
def update_video():
    id = int(input("enter the id the video: "))
    new_name = input("enter new name: ")
    new_time = input("enter new time: ")
    cursor.execute('''UPDATE Videos SET name = ? , time = ? WHERE Id= ?''',(new_name, new_time, id))
    conn.commit()

#method for deleting video
def delete_video():
    id = int(input("enter the video id: "))
    cursor.execute("DELETE FROM Videos WHERE Id = ?" ,(id,))
    conn.commit()
    fix_indices()

#main method: user menu
def main():
    while True:
        print("\nWelcome to the Youtube-Manager App!\nSelect one of the following options:"\
        "\n1. List all youtube videos" \
        "\n2. Add a youtube video" \
        "\n3. Update a youtube video" \
        "\n4. Delete a youtube video" \
        "\n5. Exit the app"
        )
        choice = input("\nEnter you choice: ")
        def choices(choice):
            match choice:
                case '1':
                    list_all_videos()
                case '2':
                    add_video()
                case '3':
                    update_video()
                case '4':
                    delete_video()
                case '5':
                    print("exiting the app")
                    return True
                case _:
                    print("!!please enter a valid option!!")
        if(choices(choice)):
            break
    cursor.close()

#module check
if __name__ == "__main__":
    main()
