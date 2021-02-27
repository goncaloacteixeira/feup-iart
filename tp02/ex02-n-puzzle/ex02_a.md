## Formulate the problem as a search problem indicating the state representation, operators (their names, preconditions, effects, and cost), initial state, and objective test.

### State Representation

We can keep track of the current state by having a 2D-Array, like this (for N=15):

```python
state = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9,10,11,12],
    [13,14,15, 0]
]
```

The `0` represents the empty spot, we can naturally extend this to a N problem.

### Initial State

The initial state can be a representation where the places are all shuffled, like this:

```python
state = [
    [ 4, 1, 3, 2],
    [ 5,13,14, 8],
    [15,10, 0,12],
    [13, 6, 9,11]
]
```

### Final State

The final state is the ordered version of the state.

```python
state = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9,10,11,12],
    [13,14,15, 0]
]
```

### Operators

Instead of moving the numbers we should "move" the empty space, so, we can display a representation of the conditions on the state:

```
state = [
    [X,#,#,X],
    [#,%,%,#],
    [#,%,%,#],
    [X,#,#,X],
]
```

- X has only two moves;
- \# has three moves;
- X has four moves;

we can design a few restrictions for the moves in a *pythonic* way:

```python
if empty.x > 0 and empty.x < sqrt(N+1) - 1:
   	if empty.y > 0 and empty.y < sqrt(N+1) - 1:
        # it's on the middle, can move to the four sides
        move = moveUp | moveDown | moveLeft | moveRight
    elif empty.y == 0:
        # it's on the middle of the top
        move = moveDown | moveLeft | moveRight
    else:
        # it's on the middle of the bottom
        move = moveUp | moveLeft | moveRight
elif empty.y > 0 and empty.y < sqrt(N+1) - 1:
    if empty.x == 0:
        # it's on the middle of the left
        move = moveDown | moveUp | moveRight
    else:
        # it's on the middle of the right
        move = moveDown | moveUp | moveLeft
elif empty.y == 0:
    if empty.x == 0:
        # top left corner
        move = moveRight | moveDown
    else:
        # top right corner
        move = moveLeft | moveDown
else:
    if empty.x == 0:
        # bottom left corner
        move = moveRight | moveUp
    else:
        # bottom right corner
        move = moveLeft | moveUp
    
```





