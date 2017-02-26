#Distract the Guards

Pairs of guards will bet bananas and thumb wrestle. The one with fewer bananas
will bet all of theirs, and the one with more matches the bet. The one with
more bananas always loses. Guards will enter an infinite loop if their banana
counts are never equal. Certain pairings will result in an infinite loop.

Write a function answer(banana_list) which, given a list of positive integers
representing the amount of bananas each guard starts with, returns the fewest
possible number of guards that will be left to watch the prisoners.

The length of banana_list will be between 1 and 100, and any guard can have
between 1 and 2 ^ 31 - 1 bananas

Examples:
<pre>
>>> answer([1, 1])
2
>>> answer([1, 7, 3, 21, 19, 13])
0
</pre>
