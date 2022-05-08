## What is it?
A simple password generator that allows setting the length, character exclusion and patterns. To fire up, all you gonna need is python 3.x installed.

## Arguments  

### --length, -l
  It defines how long the generated password should be. Default is 8.
  
### --exclude, -e
  Set what characters shouldn't be used for the generated password. Pass it as a single string separated by spaces like 'a b c @'.
  
### --pattern, -p
  Sets a pattern, if its longer than the defined length, override it, if is shorter, remaining will be randomly autocompleted. Special characters for setting a pattern:  
  * @ - Any character;  
  * \# - Letters;  
  * ! - Uppercase letters;  
  * & - Lowercase letters;  
  * $ - Special characters;  
  * \+ - Numbers;  
  * / - Use before a special pattern character to override it, returning the character itself;  

### --output, -o
  Save the generated to a file, first parameter is for the path, second is optional for write mode, default is (a)ppend, but can be set to (w)rite.

### Examples
    python3 pass_generator.py
    python3 pass_generator.py -l 12 -p 'foo@@@N++#'
    python3 pass_generator.py --pattern 'john/@5++
    python3 pass_generator.py -p '!###/@@@+++' --output '/home/user/pass.txt'
    python3 pass_generator.py --pattern '!&&&@#/#5' --length 32 --exclude 'a b c d' -o 'passwords.txt' 'w'