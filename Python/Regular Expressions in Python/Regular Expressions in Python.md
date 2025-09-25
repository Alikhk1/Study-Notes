
#  Regular Expressions :

- A regular expression (regex) is a sequence of characters that defines a pattern for matching strings. It’s used for searching, validating, and manipulating text.

- LIBRARY : import re

- METHODS : 
	- re.findall(r"regex", string) # Return Lists of matched strings
	- re.split(r"regex", string    # Returns List of subs-strings.
	- re.sub(r"regex", new, string) # Replaces matched strings with new strings.

- MetaCharacters :

		\D : Non-Digit.
		\s : Whitespace.
		\S : Non-Whitespace.
		\w : Lette or Digit, underscores.
		\W : Non-word.
		Quantifiers : Specifies how many times a character located to its left needs to be matched. (Applies only to the character immediately to the left.
		- \w{8} # 8 Characters
		- {atleast, atmost}
		- + : 1 or more times.
		- * : 0 or more times.	
		- ? : 0 or 1 time.
		- . : Any Character, except newline.
		- ^ : Match from start of string.
		- $ : Match from end of string.
		- | : OR Operator.
		- [] : Set of Optional Characters to match.
		- Circumflex : [^] # Not from these characters.

- REPEATED CHARACTERS :
	- re.search(regex, string) # Tells us if there's a match, searchs whole string.
	- re.match(regex, string) # Matches only at beginning of the string.

- TYPES OF MATCHING IN REGEX :
	1. Greedy : Tries to match as much text as possible.
		- Backtracks when too many characters are matched. Gives up 1 at a time and tries again.
	        - Example :  re.match(".*hello", "ahelloooxxxx")
	2. Non-Greedy : Tries to match as little text as possible while still succeeding.
		- Append ? at end of greedy quantifiers to convert them to lazy/non-greedy.
		- re.match("\d+?" , 123456) # Returns "1"
		- Backtracks when so few characters matched that the rest of the pattern cannot match.

---

#  Advanced Regular Expression Concepts :


- GROUPING : Matching Specific Subpatterns in a pattern. 
		- () = grouping and capturing.
		- Each Group is numbered from 1.
		- Found = regex.match/search(regex, sentiment analysis) # Found.group(0) gives whole matched string, it can only used with match/search methods.
		- NAMED GROUPS : (?P<name>regex) # Found.group("name")

- ALTERNATION : Parenthesis with Pipe Operator : (a|b|c)

- NON-CAPTURING GROUPS : Match but don't group.
	- SYNTAX : (?:regex)

- LOOKAROUND : What is ahead and behind an expression.
	- Postive : (?=regex) # It's ahead
	- Negative : (?!regex) # It's not ahead

- LOOKBEHIND : Checks what comes before the current position
	1. Positive : (?<=regex)
	2. Negative : (?<!regex) 

- BACK REFERENCES : \<group_number>

---

#  String Manipulation :


- String[Inclusive:Exclusive:Stride]
- String[::-1] : Prints the string in reverse.

---

#  String Operations :

- .lower()
- .upper()
- .capitalize() : Capitalizes the first character of the first word.

- SPLITTING STRING :
	1. .split(sep=" ", maxsplit=2)
	2. .rsplit(sep=" ", maxsplit=2)
	3. .splitlines() : Automatically splits the string on "\n" in the string.
	4. sep.join(iterable) : " ".join(list) # Joins all elements of a element seperated by a space.
	5. strip() : Removes leading and trailing whitespace (spaces, tabs, newlines) from a string.
	
- FINDING STRINGS :
	- .find(substring, start-index ,end-index) # Returns the start index of the substring

- COUNTING OCCURANCES :
	- .count(substring, start-index ,end-index)

- REPLACE STRINGS :
	- .replace(old, new, count)

---


#  String Interpolation :


- String interpolation is the process of inserting variables or expressions into a string.

1. POSITIONAL FORMATTING :

	- "Text {}".format(value)
	- String = "{} is my {}"
	  method = "Ali name"
	  condition = "labeled"
	  print(String.format(method, conditiond))
	
	- USEFUL FOR :
		1. Quick Reordering : "{1} is my {0}".format("name", "Ali)
		2. Named Placeholders : "{country} is {year} old".format(country="Pakistan", year="78")

2. FORMATTED STRING LITERAL (F-SRINGS) :
	- Conversion flags: !s (convert to string), !r (quotes), !a (ASCII)
	
	- USEFUL FOR :
		1. Inline Operations : F"{Seven} multiplied by {Eight} is {Seven * Eight}"
		2. Calling Functions : F"The answer is {Function(2,3)}"


3. TEMPLATE METHOD : 
	- Simpler syntax, Slower than f-strings, Don't allow format specifiers.
	
	- SYNTAX :

			- from string import Template
		      my_string = Template('Date Science has been called $identifier')
		      my_string.substitute(identifier="best job")
	         	 my_string.safesubstitute(abcd="abcd") # Missing placeholders appear in resulting string instead of error

	- USEFUL FOR :
		- Working with externally formatted strings, that you don't have control over.





























