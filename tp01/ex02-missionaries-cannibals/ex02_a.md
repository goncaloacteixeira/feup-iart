## Formulate this problem as a search problem by defining the state representation, initial state, operators (their name, preconditions, effects, and cost), and objective test. 

### State Representation

The representation for this problem can be a tuple with two variables and a number representing where the boat is at. 

So, we have `(m, c, b)`, where:

- `m` is the number of missionaries on the initial bank of the river;
- `c` is the number of cannibals on the initial bank of the river;
- `b` represents where the boat is right now. (1 for initial side, -1 for final side)

#### Restrictions

We know that, at any point of the problem, the number of cannibals on either side of the river cannot be higher than the number of missionaries; also we know that the boat needs at least one person to travel, and at most, two; finally we know that there are 3 missionaries and 3 cannibals. We can set some ground rules at this point:

- `0 <= m <= 3`

- `0 <= c <= 3`

- ```python
  # the only possible way the number of missionaries to be lower than the number of 
  # cannibals is if there are no cannibals
  # otherwise the number of missionaries must be equal or higher than the number of cannibals
  if (m - 3) < (c - 3) and c - 3 != 0
  	return false
  if m < c and c != 0
  	return false
  if m >= c and (m - 3) >= (c - 3):
     	return true
  else
  	return false
  
  ```

- `b = 1 \/ b = -1` (for the sake of simplicity we assume 1 to be the initial bank)

### Initial State

There are 6 people on the first bank, 3 cannibals and 3 missionaries, and the boat is on that same side of the river.

The initial state will then be `(3, 3, 1)`.

### Objective Test

We want the missionaries and the cannibals to get to the other bank by boat, given the rules provided above, so the goal state will be `(0, 0, -1)`, we don't really care where the boat is at the end, but we know it will be on the same side as the people. 

### Operators

| Operator                                                     | Initial State | Conditions | Final State                    | Cost |
| ------------------------------------------------------------ | ------------- | ---------- | ------------------------------ | ---- |
| Move one cannibal from the initial bank to the final         | (m, c, b)     | b = 1      | ((m1, c1 -1, m2, c2 + 1), -b)  | 1    |
| Move one cannibal from the final bank to the initial         | (m, c, b)     | b = -1     | ((m1, c1+1, m2, c2-1), -b)     | 1    |
| Move one missionary from the initial bank to the final       | (m, c, b)     | b = 1      | ((m1-1, c1, m2+1, c2), -b)     | 1    |
| Move one missionary from the final bank to the initial       | (m, c, b)     | b = -1     | ((m1+1, c1, m2-1, c2), -b)     | 1    |
| Move two missionaries from the initial bank to the final     | (m, c, b)     | b = 1      | ((m1-2, c1, m2+2, c2), -b)     | 1    |
| Move two missionaries from the final bank to the initial     | (m, c, b)     | b = -1     | ((m1+2, c1, m2-2, c2), -b)     | 1    |
| Move two cannibals from the initial bank to the final        | (m, c, b)     | b = 1      | ((m1, c1-2, m2, c2+2), -b)     | 1    |
| Move two cannibals from the final bank to the initial        | (m, c, b)     | b = -1     | ((m1, c1+2, m2, c2-2), -b)     | 1    |
| Move one cannibal and one missionary from the initial bank to the final | (m, c, b)     | b = 1      | ((m1-1, c1-1, m2+1, c2+1), -b) | 1    |
| Move one cannibal and one missionary from the final bank to the initial | (m, c, b)     | b = -1     | ((m1+1, c1+1, m2-1, c2-1), -b) | 1    |

