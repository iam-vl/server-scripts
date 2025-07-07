# Learn Linux

Case-sensitive. 
Find filetype:

```
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