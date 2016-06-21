# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

mkdir [dir] makes directories/folders (one layer at a time)
cd [dir or path] changes directory (if typed alone takes you home)
ls lists directories and files in current directory
touch creates a file
cp [filetocopy] [copyname] copies
mv [filetomove] [destination] moves
less [filename] displays file (q to exit)
cat [filename] streams file in terminal
rm [filename] removes file (does not work directories)
< or > take output from the file on the right/left and write it to the file on the left/right
<< or >> same as above but append
Asterisks denote "any string" in  wildcard like *.txt"
find can find list of
man [command] gives info about the command (q to exit)
apropros [keyword] scans documentation for keyword to find command you want
grep [keyword] [filename] searches for keyword in file
exit deletes


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls lists directories and files
ls -a lists directories and files in those directories(a = all)
ls -l lists directories and files with details
ls -lh same as above
ls -lah lists directories and files with details
ls -t lists directories and files by recency of modification
ls -Glp lists directories and files with details, and text of each directory that contains files highlighted

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -R list directories, files and subdirectories
ls -r list directories and files in reverse order
ls -m lists directories and files in comma delimited list
ls -d lists only directories
ls -p lists directories and files, with / after each directory
---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs is a method of combining commands.

find . -name "*a.txt" | xargs rm -- finds any text file taht ends in *"a.txt" and removes it 
 

