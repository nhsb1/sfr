# sfr
Simple Find and Replace

Takes a file (sfr.py -f filename.txt), searches each line for the string identified in the script (",") and does a replace ("|") on that string.  To use - change the line "newline = newline + stringline.replace(",", "|")" such that ",", and "|" fit the need.  

Example 
-------
Input file has lines that look like this:

"Bob Smith, email@address.com" 

The output becomes:

"Bob Smith| email@address.com"

Install
-------

    Download a copy of sfr.py and run it

Usage
-----

    sfr.py -f filename.txt

See Also
--------

NA
