# Strings

- A string is a sequence of characters.
- Strings are written inside quotes.
- Indexing starts from 0.
- Every character has its own index.
- Access a character using square brackets [].

## Negative Indexing

- Starts from the end of the string.
- -1 = Last character.
- -2 = Second last character.
- Useful when you don't know the string length.


## Slicing

Syntax:
string[start:end]

- Start index is included.
- End index is excluded.
- [:] → Whole string.
- [:n] → Beginning to n-1.
- [n:] → n to end.

## Slicing with Step

Syntax:
string[start:end:step]

- Step = 1 → Default.
- Step = 2 → Every second character.
- Step = 3 → Every third character.
- Step = -1 → Reverse the string.
- Step = -2 → Reverse every second character.


## String Case Methods

upper()       -> Converts to uppercase.
lower()       -> Converts to lowercase.
capitalize()  -> First letter uppercase.
title()       -> First letter of every word uppercase.
swapcase()    -> Reverses uppercase and lowercase.

## split()

Converts a string into a list.

Example:
text.split(",")

------------------------

## join()

Converts a list into a string.

Example:
",".join(list)

------------------------

## startswith()

Returns True if the string starts with the given text.

------------------------

## endswith()

Returns True if the string ends with the given text.





| Method         | Purpose                              | Returns |
| -------------- | ------------------------------------ | ------- |
| `upper()`      | Uppercase                            | String  |
| `lower()`      | Lowercase                            | String  |
| `capitalize()` | First letter uppercase               | String  |
| `title()`      | First letter of every word uppercase | String  |
| `swapcase()`   | Reverse case                         | String  |
| `strip()`      | Remove leading/trailing spaces       | String  |
| `replace()`    | Replace text                         | String  |
| `find()`       | Find first index                     | Integer |
| `count()`      | Count occurrences                    | Integer |
| `split()`      | String → List                        | List    |
| `join()`       | List → String                        | String  |
| `startswith()` | Starts with?                         | Boolean |
| `endswith()`   | Ends with?                           | Boolean | 
