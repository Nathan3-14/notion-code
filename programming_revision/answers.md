# Answers

## Programming Constructs
1. Sequence
2. Selection
3. Iteration
4. Iteration
5. Selection
6. Sequence
7. Iteration, Selection
8. Iteration

## Sequence
1. float
2. string
3. int
4. string
5. bool

1. 2
2. string
3. False
4. 5 (integer) is not equal to "5" (string) as they're different data types

1. strings can't be divided
2. inputs may not be castable to ints
3. can't add an int to a string

## Selection
1. A
2. D
3. B
4. B

1. != check for not equal to zero, >0 would be correct instead
```python
while answer > 0:
    answer = int(input())
```
2. or should be used instead as and checks for both being true
```python
if has_card or has_cash:
    print("you can buy it!")
```
3. number < 10 means less than and number > 1 means greater than
```python
if 1 < number < 10:
    print("valid number")
```

## Iteration
1. for
2. for
3. while
4. while

### For Loops
```python
for _ in range(3):
    print("looping...")
print("complete")
```
```python
num = 5
for _ in range(10):
    num += 1
```
```python
cost = 200
discount = 0.5
discounted_cost = cost
for _ in range(3):
    discounted_cost *= discount
print(discounted_cost)
```
```python
total = 0
for _ in range(8):
    total += 10
if total > 60:
    print("PASS")
else:
    print("FAIL")
```
```python
cost_adult = 15
cost_kid = 8
num_adult = 4
num_kid = 7
total = cost_adult * num_adult + cost_kid * num_kid
```
### While Loops
1. first line under the while loop
2. so name changes

1. `break` in while loop
2. `break` in while loop
3. `break` in while loop
4. `break` in while loop

```python
_input = ""
while _input != "password123":
    _input = input("Enter the password! ")
print("WELCOME USER123")
```
## PPQs
```python
if A == "yes" and (B == "yes" or C == "YES"):
    print("You can!")
else:
    print("You can'! :(")
```
```python
input("enter first number")
if num1 > num2 then
    print(num1)
else
    print(num2)
```
```python
num = 0
while num >= 0:
    num = int(input())
    print(2 * num)
```
```python
miles = int(input("miles? "))
age = int(input("age? "))
if miles < 10000 and age <= 5:
    print("True")
else:
    print("False")
```
```python
votes = {"A": 0, "B": 0, "C": 0}
total_votes = 0
_input = ""
while _input != "END":
    if _input in list(votes.keys()):
        total_votes += 1
        votes[_input] += 1
    _input = input("who vote for\n>> ")
print(total_vote)
print("A:", votes["A"])
print("B:", votes["B"])
print("C:", votes["C"])
```