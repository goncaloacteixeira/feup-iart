## Formulate this problem as a search problem by defining the state representation, initial state, operators (their name, preconditions, effects, and cost), and objective test. 

### State Representation

The representation for this problem can be a tuple of two variables `x` and `y`, where `x` represents the amount of water on the 4L bucket, and the `y` represents the amount of water on the 3L bucket. So, our state will be defined as `(x, y)`. We can set a couple of restrictions: `0 <= x <= 4` and `0 <= y <= 3`.

### Initial State

Both buckets are empty at start, so, it's only natural the initial state to be `(0, 0)`.

### Objective Test

We want the first bucket to have `n` liters of water, give a few set of operations we can perform, we don't care how many liters the second bucket has, so the goal here is `(n, y)`. In this exercise we will aim for `n=2`.

### Operators

| Operator                                                     | Initial State and Preconditions | Final State  | Cost |
| ------------------------------------------------------------ | ------------------------------- | ------------ | ---- |
| 1- Fill the 4L bucket                                        | (x, y) with x < 4               | (4, y)       | 1    |
| 2- Fill the 3L bucket                                        | (x, y) with y < 3               | (x, 3)       | 1    |
| 3- Empty the 4L bucket                                       | (x, y) with x > 0               | (0, y)       | 1    |
| 4- Empty the 3L bucket                                       | (x, y) with y > 0               | (x, 0)       | 1    |
| 5- Pour water from the 3L bucket to completely fill the 4L bucket | (x, y) with x+y >= 4 and y > 0  | (4, y-(4-x)) | 1    |
| 6- Pour water from the 4L bucket to completely fill the 3L bucket | (x, y) with x+y >= 3 and x > 0  | (x-(3-y), 3) | 1    |
| 7- Pour all the water from the 3L bucket to the 4L bucket    | (x, y) with x+y <= 4 and y >= 0 | (x+y, 0)     | 1    |
| 8- Pour all the water from the 4L bucket to the 3L bucket    | (x, y) with x+y <= 3 and x >= 0 | (0, x+y)     | 1    |

