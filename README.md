# Cellular automaton

Cellular automaton is generate with the different rules stored in ```rules.py```.

To use it choose the width and the height of the canvas with -w and -h which will be also the size of the table.
Then the rule that you want to generate with -r.
The final launch will be :
```
automaton.py -w <width> -h <height> -r <the number of the rule>
```

# Game Of Life

To use ```gameOfLife.py``` put your initial draw in the file ```shapes.py```, by configuring the generation array, and by putting ones in the two dimensional array.

The arguments are: -w (width of the canvas) -h (height of the canvas) -s (speed of the generation in milliseconds) -g (grandeur of squares drawn) -n (name of the initial shape).

The shapes available are: shape1, simkinGliderGun, beeHive, stairs.

The final command should be:
```
gameOfLife.py -w < width > -h < height > -s < speed > -g < grandeurOfSquares > -n < nameOfShape >
```