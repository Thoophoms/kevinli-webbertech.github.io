## NANO

`nano` is a simple and easy-to-use text editor for Unix-based systems, such as Linux and macOS. It is often preferred for its simplicity and ease of use, especially for users who are new to command-line text editing. 


## Installation

### Linux
`nano` is usually pre-installed on most Linux distributions. If it is not installed, you can install it using the package manager of your distribution. For example:

- **Debian/Ubuntu**:
  ```sh
  sudo apt-get install nano
  ```
  
- **Fedora:**
  ```sh
  sudo dnf install nano
  ```
  
- **Arch Linux:**
  ```sh
  sudo pacman -S nano
  ```

## macOS

`nano` comes pre-installed on macOS. You can use it directly from the terminal.

## Windows

On Windows, you can use `nano` within the Windows Subsystem for Linux (WSL) or through a third-party terminal emulator like Git Bash or Cygwin.

## Basic Usage

To start `nano`, open your terminal and type `nano` followed by the name of the file you want to edit:

  ```sh
  nano filename.txt
  ```

***Note:*** If the file does not exist, `nano` will create file for you.

## Interface Overview
When the file is opened with `nano`, you will see the following:

- **File Content Area:** This is where you can see and edit the contents of the file.
- **Shortcut Bar:** At the bottom of the screen, you will see a list of commands. Each command is preceded by a caret (^), which represents the `Ctrl` key.

___

## Basic Commands

- `nano filename.txt` : Open a File
- `CTRL + Z` : Suspend `nano`
- `Ctrl + X` : Exit nano permanently

## Navigation

- ARROWS (↑, ↓, ←, →) : Move the cursor up, down, left, or right
- `CTRL + P` : Move the cursor up one line
- `CTRL + N` : Move the cursor down one line
- `CTRL + B` : Move the cursor left one character
- `CTRL + F` : Move the cursor right one character
- `ALT + F` or `CTRL + →` : Move forward by one word
- `ALT + B` or `CTRL + ←` : Move backward by one word
- `CTRL + V` : Scroll page down
- `CTRL + Y` : Scroll half a page up
- `CTRL + W` : Scroll a full page up
- `CTRL + A` : Go to beginning of the line
- `CTRL + E` : Go to end of the line
- `ALT + <` : Go to beginning of the file
- `ALT + >` : Go to end of the file
- `CTRL + _` : Go to a specific line
- `ALT + ,` : Jump to a specific line or column
- `CTRL + ↑` : To previous block
- `CTRL + ↓` : To next block
- `ALT + \` : To top of buffer
- `ALT + /` : To bottom of buffer

## Regular Expressions

- `.` : Matches any single character except a newline
- `^` : Matches the start of a line
- `$` : Matches the end of a line
- `*` : Matches zero or more occurrences of the preceding character or group
- `+`: Matches one or more occurrences of the preceding character or group
- `?`: Matches zero or one occurrence of the preceding character or group
- `{n}`: Matches exactly n occurrences of the preceding character or group
- `{n,}`: Matches at least n occurrences of the preceding character or group
- `{n,m}`: Matches between n and m occurrences of the preceding character or group
- `[abc]`: Matches any single character in the given set (a, b, or c)
- `[^abc]`: Matches any single character not in the given set (not a, b, or c)
- `(abc)`: Creates a group that can be referenced or repeated
- `\`: Escapes a special character or treats it literally
- `|`: Acts as an OR operator, matches either the expression before or after it

## Search

- `CTRL + W`: Start forward search
- `CTRL + Q`: Start backward search
- `ALT + W`: Repeat the last forward search
- `ALT + Q`: Find next occurrence backward
- `ALT + R`: Repeat the last backward search
- `ALT + W + CTRL + W`: Toggle case sensitivity during search
- `ALT + W + ALT + W`: Toggle whole word search during search
- `ALT + W + ALT + R`: Toggle regular expression search during search
- `CTRL + W + CTRL + W`: Move to the next occurrence of the search pattern
- `ALT + W + ALT + V`: Move to the next occurrence of the search pattern (ignoring case)
- `ALT + W + ALT + B`: Move to the previous occurrence of the search pattern (ignoring case)
- `CTRL + W + CTRL + L`: Toggle the "Search backwards" option during search
- `CTRL + W + CTRL + O`: Toggle the "Wrap around" option during search
- `CTRL + W + CTRL + V`: Move to the previous occurrence of the search pattern
- `CTRL + W + CTRL + C`: Count the number of occurrences of the search pattern
- `CTRL + W + CTRL + G`: Cancel the search and return to editing

## Info

- `CTRL + C`: Report cursor position
- `ALT + D`: Report line/word/character count
- `CTRL + G`: Display help text

### Marking

- `CTRL + ^` or `CTRL + 6`: Set the mark at the current cursor position
- `ALT + A`: Turn the mark on/off
- `TAB`: Indent marked region
- `SHIFT + TAB`: Unindent marked region

## Case Conversion

- `ALT + L` : Convert the selected text to lowercase
- `ALT + U` : Convert the selected text to uppercase
- `ALT + C` : Capitalize the selected text or the current word

## File Handling

- `CTRL + S` : Save current file
- `CTRL + O` : Offer to write file ("Save as")
- `CTRL + R` : Insert a file into current one
- `CTRL + A` : Append the contents of another file to the current file
- `CTRL + W` : Write the current file to a different filename
- `CTRL + T` : Invoke the spell checker on the current file

## Editing

- `CTRL + K` : Cut current line into cutbuffer
- `ALT + 6` : Copy current line into cutbuffer
- `CTRL + U` : Paste contents of cutbuffer
- `ALT + T` : Cut until end of buffer
- `CTRL + SPACE` : Set a mark at the current position
- `CTRL + ]` : Indent the current line
- `ALT + ]` : Unindent the current line
- `ALT + 3` : Comment/uncomment line/region
- `ALT + U` : Undo last action
- `ALT + E` : Redo last undone action

## Operations

- `CTRL + T` : Execute some command
- `CTRL + J` : Justify paragraph or region
- `ALT + J` : Justify the entire buffer
- `ALT + F` : Run a formatter or fixer
- `ALT + B` : Run a syntax check
- `ALT + ;` : Replay macro
- `ALT + :` : Start/stop recording of macro
- `ALT + N`: Turn line numbers on/off
- `ALT + P`: Turn visible whitespace on/off
- `CTRL + L`: Refresh the screen and redraw the interface
- `CTRL + W`: Switch between smooth scrolling and line scrolling

## Getting Help

- `CTRL + G`: Show the help menu
- `CTRL + G + ?`: Get help on using the help viewer
- `CTRL + G + B`: Basic movement commands
- `CTRL + G + C`: Commonly used commands
- `CTRL + G + S`: Search and replace
- `CTRL + G + P`: Nano's preferences
- `CTRL + G + Q`: Quit the help buffer

## Deleting

- `CTRL + H`: Delete character before cursor
- `CTRL + D`: Delete character under cursor
- `ALT + BSP`: Delete word to the left
- `CTRL + DEL`: Delete word to the right
- `ALT + DEL`: Delete current line

## Buffers

- `CTRL + O`: Save the current buffer
- `CTRL + T`: Invoke the spell checker on the current buffer
- `CTRL + R`: Read a file into the current buffer
- `ALT + CTRL + P`: Switch to the previous buffer
- `ALT + CTRL + N`: Switch to the next buffer
- `CTRL + X`: Exit nano and close the current buffer
- `ALT + CTRL + L`: List and select a buffer to switch to

## Replace

- `CTRL + W + CTRL + T`: Replace the current occurrence of the search pattern
- `CTRL + W + CTRL + +`: Replace all occurrences of the search pattern
- `CTRL + W + CTRL + A`: Replace all occurrences of the search pattern interactively
- `CTRL + W + CTRL + I`: Interactive replace with confirmation for each occurrence


___

## Advanced Features
### Syntax Highlighting

`nano` supports syntax highlighting for various programming languages. This feature is enabled by default for recognized file types. To manually enable or configure syntax highlighting, edit the `~/.nanorc` file.

## Configuring nano
You can customize `nano` by editing the `~/.nanorc` file. For example, to enable line numbers, add the following line to `~/.nanorc`:

  ```sh
  set linenumbers
  ```

___