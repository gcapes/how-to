# Context managers
These are used to encapsulate a setup step, doing something, and a tear down step.
You can create a class manually, using `__enter__` and `__exit__` methods
to handle the setup and tear down functionality.

The alternative is to use the `@contextmanager` decorator from `contextlib`.
This requires some code before a `yield` statement, and some code afterwards
to do the setup and teardown steps respectively.
It seems that this is normally done like this:

```
try:
  yield
finally:
  <do some tear-down>
```
