## Python generator functions

When a function contains the `yield` keyword in python,
it is called a generator function.
In contrast to `return` which exits a function,
the `yield` keyword pauses a function until you ask the generator
for the next value, whereupon it resumes and gives the next value
(i.e. from the next time the `yield` keyword is encountered).

When you call a generator function, it returns a generator,
whereas a normal function is more likely to return a list.
You then have to iterate over the generator to do something with the values.

Here's a fibonacci example:

```python
def fibonacci(length):
    # edge cases
    if length < 1:
        return
    if length == 1:
        yield 1
        return

    left = right = 1
    yield left
    yield right

    for _ in range(length - 2):
        left, right = right, left + right
        yield right

the_generator = fibonacci(9)
for num in the_generator:
  print(num)
```
