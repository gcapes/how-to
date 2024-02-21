## Deleting lines matching a pattern containing slashes

I want to delete a line from a file, matching a string.
This is a simplified example.

    $ string='a line with spaces and a $variable substitution'
    $ echo $string
    a line with spaces and a $variable substitution
    $ echo $string > temp.txt
    ~ $ sed "/$the_string/d" temp.txt
    ~ $ 

So far so good.

However, the actual string in the real problem is this:
`export PATH="$PATH:/home/mbexegc2/.local/share/hpcflow/links"`

So I can't use forward slash as the delimiter without escaping all the slashes
in the string.
I thought I could just use a different delimiter (which I've done in the past with 
sed (search/replace) substitutions).
However, it doesn't work:

    ~ $ sed "#$the_string#d" temp.txt
    a line with spaces and a $variable substitution

Turns out, you *can* use a different delimiter, but you need to escape it with a backslash
at the start:

    ~ $ sed "\#$the_string#d" temp.txt
    ~ $ 


