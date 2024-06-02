## Reminder

Do the activities in the Instructions and answer these questions. Have a partner
review your answers and 'sign' his/her name here.

> By signing here I hereby attest that I read the answers and agree that they are full
> and correct. I will gladly accept their grade as my own.

### Reviewed by: Victor

# Questions:

**Question #1A**
What is the measured time complexity of your **ORIGINAL** `get_primes` algorithm?
Is it Linear or Quadratic? Does this meet your expectations as you examine
the code? Explain.

```
The measured time complexity of my original get prime algorithm was O^2. This is a quadratic function. This meets my expectations, because as N increases, the outer loop loops N times, and the nested loop also loops N times.
```

**Question #1B**
What is the measured time complexity of your **Sieve of Eratosthenes**
implementation of `get_primes`? Does it appear Linear or Quadratic?
Does this meet your expectations as you examine the code? Explain.

Feel free to do some online research of Sieve of Eratosthenes.

```
The measured time complexity of my Sieve of Eratosthenes appears to be O(N). The graph appears to fit extremely well with the linear fit. This seems to fit with my expecations as I examine the code, as the amount of steps is (N/2 + N/3 + N/5 + N/7 + ...), which would mean the complexity is O(N).
```

**Question #2**
Examine the `get_sum.png` graph. Explain what the graph is saying about the code
found in the method `get_sum`. What is the Big-O?

```
The graph of get_sum shows curved growth rather than linear growth, and the quadratic fit line is able to fit the points exactly. This means that the big O of get_sum is O(N^2).
```

**Question #3**
Examine the graphs `limit_range_fast.png` and `limit_range_slow.png`. How do the points
on each of the graphs grow on the y-axis? Does it look linear? Describe how the
graphs **look** using Big-O notation.

```
For limit_range_slow, the quadratic line of best fit fits perfectly with the data points, meaning that the time complexity is O(N^2). For limit_range_fast, the linear line of best fit fits perfectly with the data points, meaning that the time complexity is O(N).
```

**Question #4**
Examine the **code** for the `limit_range_slow`. Explain why it is so slow.
Explain the Big-O complexity as best you can. Essentially, show the work to
_derive_ the Big-O complexity. In this example, we will assume that there are n
values in the list. AND, the range will be of size n. (e.g. n = high - low).

For reference, the slow code is:

```python
return [ n for n in range(low, high) if n in items]
```

```
The slow code iterates over a range and builds a list of numbers in that range that are also in another list. This is slow because each search operation is O(N) and the outer for-loop is O(N) as well. This causes an O(N) operation to execute N times, which results in a time complexity of O(N^2).
```

**Question #5**
Look at the graphs for `get_list_slow`, `get_list_med` and `get_list_fast`.
Don't forget to look at the scale. What do you suspect is the Big-O complexity
for each? Explain the speeds of each method.

```
 For get_list_slow, the time complexity from the graph appears to be O(N^2), because the quadratic fit line fits perfectly with the data. Looking at the code, this function is quite slow because it attempts to make a list of all the values between 1 & n in decreasing order but does it inefficiently by trying to add to the beginning of the list, which is an O(N) operation, which is repeated O(N) times, making the total complexity O(N^2). For get_list_med, the time complexity appears to be O(N). This function is significantly more efficient as looking at the code the items are appended rather than inserted, which is a O(1) operation, repeated O(N) times, making it O(N). For get_list_fast, the time complexity is also O(N). It achieves the same thing in the same way that get_list_med does, except it uses a list comprehension, making it about 8% faster.
```
