# VIM shortcuts

## Navigation
- `h` : Move left
- `j` : Move down
- `k` : Move up
- `l` : Move right
- `w` : Move to the beginning of the next word
- `b` : Move to the beginning of the previous word
- `0` : Move to the beginning of the line
- `$` : Move to the end of the line
- `gg` : Move to the beginning of the file
- `G` : Move to the end of the file
- `H` : Move to the top of the screen
- `M` : Move to the middle of the screen
- `L` : Move to the bottom of the screen
- `Ctrl + u` : Scroll up half a screen
- `Ctrl + d` : Scroll down half a screen

## Inserting Text
- `i` : Insert before the cursor
- `I` : Insert at the beginning of the line
- `a` : Append after the cursor
- `A` : Append at the end of the line
- `o` : Open a new line below the current line
- `O` : Open a new line above the current line

## Editing
- `x` : Delete the character under the cursor
- `dd` : Delete the current line
- `dw` : Delete from the cursor to the start of the next word
- `d$` : Delete from the cursor to the end of the line
- `d0` : Delete from the cursor to the beginning of the line
- `y` : Yank (copy) selected text
- `p` : Paste after the cursor
- `P` : Paste before the cursor
- `u` : Undo
- `Ctrl + r` : Redo

## Visual Mode
- `v` : Start visual mode, mark lines, and move the cursor to highlight
- `V` : Start visual line mode
- `Ctrl + v` : Start visual block mode

## Searching and Replacing
- `/pattern` : Search for a pattern
- `?pattern` : Search backward for a pattern
- `n` : Repeat the last search
- `N` : Repeat the last search in the opposite direction
- `:%s/old/new/g` : Replace all occurrences of 'old' with 'new' in the file
- `:s/old/new/g` : Replace all occurrences of 'old' with 'new' in the current line

## File Operations
- `:w` : Write (save) the file
- `:q` : Quit Vim
- `:wq` : Write and quit
- `:q!` : Quit without saving
- `:e filename` : Open a file
- `:sav filename` : Save as a different file
- `:wa` : Write all files
- `:qa` : Quit all files

## Buffers and Windows
- `:bn` : Go to next buffer
- `:bp` : Go to previous buffer
- `:bd` : Delete (close) buffer
- `:sp filename` : Open a file in a new horizontal split
- `:vsp filename` : Open a file in a new vertical split
- `Ctrl + w, s` : Split window horizontally
- `Ctrl + w, v` : Split window vertically
- `Ctrl + w, w` : Switch between windows

## VI Editing Commands

**Command	Description**
```
i	Insert at cursor (goes into insert mode)
a	Write after cursor (goes into insert mode)
A	Write at the end of line (goes into insert mode)
ESC	Terminate insert mode
u	Undo last change
U	Undo all changes to the entire line
o	Open a new line (goes into insert mode)
dd	Delete line
3dd	Delete 3 lines
D	Delete contents of line after the cursor
C	Delete contents of a line after the cursor and insert new text. Press ESC key to end insertion.
dw	Delete word
4dw	Delete 4 words
cw	Change word
x	Delete character at the cursor
r	Replace character
R	Overwrite characters from cursor onward
s	Substitute one character under cursor continue to insert
S	Substitute entire line and begin to insert at the beginning of the line
~	Change case of individual character
```