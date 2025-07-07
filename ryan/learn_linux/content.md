# Learn Linux


## Intro 

Interesting: tab completion 
Case-sensitive. 
Find filetype:

```sh
$ file comments.md
comments.md: ASCII text$
```

Spaces in names:

```sh
mkdir 'Holiday Photos'
# option 1
cd 'Holiday Photos'
# option 2 - Escape char - ignore special meaning of next char
cd Holiday\ Photos
```

## Man pages
 
Look up a command: `man <command>`
You don't the command, but you know what you want -> use: `man -k <search_term>`

```sh
$ man -k 'file type'
[ (1)                - check file types and compare values
file (1)             - determine file type
grub-file (1)        - check file type
test (1)             - check file types and compare values
```

## Use vi(m) 

```
vi file1
``` 

Always start in edit mode.  You need to switch to insert mode. 

Operation | Command
---|---  
To start, switch to insert mode | `i` 
Go back to edit mode  | `ESC`  
Save and exit | `ZZ`
Discard changes since the last save & exit: | `:q!`   
Save file, but dont exit | `:w`
Save and exit | `:wq`  

Some more controls in edit mode: 

Operation | Command
---|---  
Move cursor | Arrow keys, `jklh`  
Move cursor to line start | `^` 
Move cursor to line end | `$`  
Move cursor to line N | `NG` Example: `5G` (line 5) 
Move cursor to last line | `G`  
Move c. to beginning next word | `w`  
Move forward N words | `Nw`. Ex: `2w`  
Move c. to beginning prev. word | `b` 
Move forward 1 para | `{` 
Move backwds 1 para | `}`  

> To enable line numbers: `:set nu`  

## TBD VI: 

Basics: 

* Deleting 
* Undoing  

More: 

* Copy and paste 
* Search & replace 
* Buffers 
* Markers 
* Ranges 
* Settings  





