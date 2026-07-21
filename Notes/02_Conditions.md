## Conditions 

What is a Condition?
A condition is simply a question whose answer is either:
✅ True
❌ False


# if Statement

- Used to make decisions.
- Runs only when the condition is True.

Syntax:

if condition:
    statement

Remember:
- Condition returns True or False.
- Indentation is mandatory.

## if...else

Used when there are two possible outcomes.

Syntax:

if condition:
    statement
else:
    statement

Only one block executes.

## elif

Used when there are multiple conditions.

Syntax:

if condition:
    ...
elif condition:
    ...
else:
    ...

Python executes only the first True condition.
Order of conditions is important.


## Logical Operators

and  -> Both conditions must be True.
or   -> At least one condition must be True.
not  -> Reverses True/False.

## Nested if

- if inside another if.
- Used when one condition depends on another.

Syntax:

if condition1:
    if condition2:
        ...