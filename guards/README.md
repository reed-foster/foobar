#Distract the Guards

Pairs of guards will bet bananas and thumb wrestle. The one with fewer bananas
will bet all of theirs, and the one with more matches the bet. The one with
more bananas always loses. Guards will enter an infinite loop if their banana
counts are never equal. Certain pairings will result in an infinite loop.

Write a function answer(banana_list) which, given a list of positive integers
representing the amount of bananas each guard starts with, returns the fewest
possible number of guards that will be left to watch the bunnies.

The length of banana_list will be between 1 and 100, and any guard can have
between 1 and 2 ^ 31 - 1 bananas

Examples:
<pre>
>>> answer([1, 1])
2
>>> answer([1, 7, 3, 21, 19, 13])
0
</pre>

<b>foobarwork.py</b> is the original solution file that I abandoned after I rethought the problem.
It uses Tkinter to render a pattern of "infinite loop" pairings that I used to find a fast solution
for determining if two guards would enter an infinite loop or not.

<b>combinatorial_optimization_bruteforce.py</b> provides a brute force solution that checks all
possible combinations of guards and returns the minimum free guards

<b>combinatorial_optimization_graph.py</b> uses a graph data structure to represent the guards; each
guard is a node, and nodes are connected if the two guards represented by those nodes would enter
an infinite thumbwrestling loop. The getminguards function trims pairs of connected nodes off of
the graph and counts the total number of unconnected nodes. This count represents the number of
guards left to guard the bunnies.