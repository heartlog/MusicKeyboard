import os

from pynput.keyboard import Key, Listener

import winsound
import random

# List of available sounds
sounds_list_onpress = []

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

# 
def on_press(key):
    if key == Key.esc:  # Add a key combination to exit the program (e.g., 'esc')
        return False  # Stop the listener
    play_random_sound(sounds_list_onpress)


def on_release(key):
    pass  # You can add additional functionality for key releases here if needed


def main():
    list_files("sounds", sounds_list_onpress)
    print(sounds_list_onpress)
    play_random_sound(sounds_list_onpress)
    with Listener(on_press=on_press, on_release=on_release) as listener:
        print("Listening for key presses. Press 'esc' to exit.")
        listener.join()


if __name__ == "__main__":
    main()