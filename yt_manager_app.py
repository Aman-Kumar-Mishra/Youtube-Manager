#youtube-manager application

import json

ytvideos = 'ytvideos.txt'

#method for loading data onto 'videos' list
def load_data():
    try:
        with open(ytvideos, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#method for saving data
def save_data(videos):
    with open(ytvideos, 'w') as file:
        json.dump(videos, file)

#method for listing videos
def list_all_videos(videos):
    print("\n" + "*"*50 + "\n")
    for index, vid in enumerate(videos, start= 1):
        print(f"{index}. title: {repr(vid['name'])}, duration: {repr(vid['time'])}\n")
    print("*"*50)

#method for adding a video to the 'videos' list
def add_video(videos):
    name = input("Enter name of the video: ")
    time = input("Enter length of video: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)
    print("videos added successfully!")

#method for updating the name or/and time of a video
def update_video(videos):
    list_all_videos(videos)
    prev_video = input("name the video you want to update: ")
    not_found = True
    for i in videos:
        if prev_video == i['name']:
            not_found = False
            def update_name(new_name):
                i['name'] = new_name
            def update_time(new_time):
                i['time'] = new_time
            update_choice = input("what do you want to update?\n1. Name \n2. Time\n3. Both" \
            "\nEnter your choice: ")
            match(update_choice):
                case '1':
                    new_name = input("enter the newe name: ")
                    update_name(new_name)
                case '2':
                    new_time = input("enter the new time: ")
                    update_time(new_time)
                case '3':
                    new_name = input("enter the newe name: ")
                    new_time = input("enter the new time: ")
                    update_name(new_name)
                    update_time(new_time)
                case _:
                    print("please enter a valid choice!!")
                    break
            save_data(videos)
            print("videos updated!")
            break
    if not_found:
        print("video not found!")

#method for deletig a video from the list
def delete_video(videos):
    list_all_videos(videos)
    name = input("name the video you want to delete: ")
    not_found = True
    for i in videos:
        if name == i['name']:
            not_found = False
            videos.remove(i)
            save_data(videos)
            print("video deleted!")
            break
    if not_found:
        print("video not found!")

#main method: user menu
def main():
    videos = load_data()
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
                    list_all_videos(videos)
                case '2':
                    add_video(videos)
                case '3':
                    update_video(videos)
                case '4':
                    delete_video(videos)
                case '5':
                    print("exiting the app")
                    return True
                case _:
                    print("!!please enter a valid option!!")
        if(choices(choice)):
            break

#module checking
if __name__ == "__main__":
    main()
