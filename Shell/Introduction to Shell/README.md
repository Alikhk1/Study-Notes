


- SHELL : A shell is a program that takes commands from the user and passes them to the operating system for execution.

	The central idea of the shell: simple tools that produce 
	and consume lines of text can be combined in a wide variety of ways 
	to solve a broad range of problems.

- .. : Directory above one you're currently in.
- .  : Current working directory.
- ~  : Home Directory.
- cp : Copy Files.
- mv : Move Files & Rename Files/Directory.
- rm : Delete Files.
- rmdir : Delete Directory. (Must be empty)
- mkdir : Make Directory.
- cat : Print Contents of a file.
- less : View Files as pages or multiple files 1 by 1.
- heads: Prints First 10 lines/rows of a file.
- tails: Prints Last 10 lines/rows of a file.
- cut : Select Columns from a file.
- wc : Count Characters, Words and Lines.
- uniq : It removes adjacent duplicated lines
- echo : Get Variables value with $.

- grep : Takes a piece of text followed by one or more filenames and prints all of the lines in those files that contain that text.
		1. -c: print a count of matching lines rather than the lines themselves
		2. -h: do not print the names of files when searching multiple files
		3. -i: ignore case (e.g., treat "Regression" and "regression" as matches)
		4. -l: print the names of files that contain matches, not the matches
		5. -n: print line numbers for matching lines
		6. -v: invert the match, i.e., only show lines that don't match

- RERUN COMMAND :
		1. History
		2. !Command name

- TAB KEY : Use to autocomplete commands and file names.

- FLAGS : 
	1. -n : Number of lines to display.
	2. -R : Shows every file and sub directory.
	3. -F : Prints a / after the name of every directory and a * after the name of every runnable program.
	4. -d : Specifies the delimiter.
	5. -f : Fields/Columns to select.

- WILDCARDS :
	1. * : 0 or More Matches.
	2. ? : Matches single character.
	3. [...] : Matches any 1 character inside, not words.
	4. {...} : Includes comma-seperate search patterns and matches them.

- man : Prints commands documentation 
	- The one-line description under NAME tells you briefly what the command does, 
	  and the summary under SYNOPSIS lists all the flags it understands. 
	  Anything that is optional is shown in square brackets [...], 
	  either/or alternatives are separated by |, 
	  and things that can be repeated are shown by ...

- REDIRECT : > Sign tells to redirect output to that file.

- PIPE : | The pipe symbol tells the shell to use the output of the command on the left as the input to the command on the right.

- sort : Puts data in order.
	1. -n : sort numerically 
	2. -r : reverse the order of its output, 
	3. -b tells it to ignore leading blanks 
	4. -f tells it to fold case (i.e., be case-insensitive)

- ENVIRONMENT VARIABLES : Shell stores information in variables, variables' names are conventionally written in upper case.
	1. HOME
	2. PWD
	3. SHELL - Which shell program is being used
	4. USER - User's ID.

- SHELL VARIABLE : name=value.

- FOR LOOPS : for filetype in gif jpg png; do echo $filetype; done
	      for f in seasonal/*.csv; do echo $f; head -n 2 $f | tail -n 1; done

	1. The structure is for …variable… in …list… ; do …body… ; done
	2. The list of things the loop is to process (in our case, the words gif, jpg, and png).
	3. The variable that keeps track of which thing the loop is currently processing (in our case, filetype).
	4. The body of the loop that does the processing (in our case, echo $filetype).

- bash : Run script.
- $@ : All command line parameters given to script.
- $1, $2 : positional parameters written in script.
- \# : Comments.


























