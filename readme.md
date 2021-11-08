**SoundCloud Data Challenge**

**Github Link :** 

**Solution:**
----

The solution to completing this challenge is Map Reduce. The solution consist of 3 part :

- `mapper.py` , to get an adjacency list from the file input.txt
- `mapper_iteration.py` + `reducer_iteration.py` to aggregate list from previous mapper based on N
- `reducer.py` which assembles the result and writes to file output.txt.

**Execution**
----

``
python social_network.py N
``

**N** = degree

Example for N = 3
```
brendan davidbowie kim omid torsten
davidbowie brendan kim mick omid torsten ziggy
kim brendan davidbowie mick omid torsten ziggy
mick davidbowie kim omid ziggy
omid brendan davidbowie kim mick torsten ziggy
torsten brendan davidbowie kim omid ziggy
ziggy davidbowie kim mick omid torsten

```