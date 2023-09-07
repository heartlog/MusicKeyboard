import os
import random
from pynput.keyboard import Key, Listener
import winsound

# List of available sounds For onpress in "sounds"
sounds_list_onpress = []
# List of available sounds For onrelease in "sounds_release"
sounds_list_onrelease = []


def list_files(folder_path, sound_list):
    for filename in os.listdir(folder_path):
        if filename.endswith(".wav"):
            full_path = os.path.join(folder_path, filename)
            sound_list.append(full_path)

def play_random_sound(sounds):
    try:
        sound_file = random.choice(sounds)
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    except Exception as e:
        print(f"Error playing sound: {e}")

def on_press(key):
    if key == Key.esc:  # Add a key combination to exit the program (e.g., 'esc')
        return False  # Stop the listener
    if is_empty(sounds_list_onpress) == False:
        play_random_sound(sounds_list_onpress)
    else:
        print("There is no files | sounds folder is Empty.")

def on_release(key):
    if is_empty(sounds_list_onrelease) == False:
        play_random_sound(sounds_list_onrelease)
    else:
        pass

def is_empty(alist):
    return len(alist)==0


def main():
    # Load onpress sounds from "sounds"
    list_files("sounds", sounds_list_onpress)
    print("Loded OnPress files:",sounds_list_onpress)
    # Load onrelease sounds from "sounds_release"
    list_files("sounds_release", sounds_list_onrelease)
    print("Loded OnRelease files:",sounds_list_onrelease)
    with Listener(on_press=on_press, on_release=on_release) as listener:    # start Listener 
        print("Listening for key presses. Press 'esc' to exit.")
        listener.join()


if __name__ == "__main__":
    main()