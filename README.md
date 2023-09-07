# Musickeyboard

**MusicKeyboard** is a Python program that allows you to play random sound files when you press and release keys on your keyboard. The program uses the pynput.keyboard library to listen for key events and the winsound library to play the sound files.

## Installation

To use **MusicKeyboard**, you need to have **Python** installed on your computer. You can download Python from the official website: <https://www.python.org/downloads/>

You also need to install the **pynput** library. You can install it using **pip**:

```shell
pip install pynput
```

## Usage

```py
## Clone the MusicKeyboard repository to your local machine:
git clone https://github.com/your-username/MusicKeyboard.git

# Navigate to the project folder:
cd MusicKeyboard
```

Create two folders named `"sounds"` and `"sounds_release"` in the project folder. Place your sound files (in .wav format) in the respective folders. Make sure the files have the __.wav extension__ .

Open the `main.py` file in a text editor and modify the key combination to exit the program if needed. By default, the program will exit when the `Esc` key is pressed.

## Run the program

```py
python main.py
```

The program will start listening for key presses. Press any key to play a random sound from the "sounds" folder.
Release the key to play a random sound from the `"sounds_release"` folder.

> To exit the program, press the key `Esc`.

## Contributing

If you have any suggestions or improvements for MusicKeyboard, feel free to open an issue or submit a pull request on the GitHub repository: <https://github.com/heartlog/MusicKeyboard> .
