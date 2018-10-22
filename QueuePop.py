Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
Traceback (most recent call last):
  File "/home/dell/StackP.py", line 26, in <module>
    Pqueue.add(10)
  File "/home/dell/StackP.py", line 10, in add
    self.stack.append(current)
AttributeError: 'queue' object has no attribute 'stack'
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
Traceback (most recent call last):
  File "/home/dell/StackP.py", line 27, in <module>
    Pqueue.remove()
  File "/home/dell/StackP.py", line 19, in remove
    self.stack.pop()
AttributeError: 'queue' object has no attribute 'stack'
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
[10, 20, 30, 40]
Traceback (most recent call last):
  File "/home/dell/StackP.py", line 28, in <module>
    Pqueue.peek()
  File "/home/dell/StackP.py", line 22, in peek
    l = len(self.stack)
AttributeError: 'queue' object has no attribute 'stack'
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
[10, 20, 30, 40]
The last element in stack: 40
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
[10, 20, 30, 40]
The last element in stack: 10
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
The last element in stack: 10
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
[10, 20, 30, 40, 50]
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
[10, 20, 30, 40, 50]
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
Traceback (most recent call last):
  File "/home/dell/StackP.py", line 23, in <module>
    Pqueue.remove()
  File "/home/dell/StackP.py", line 16, in remove
    self.queue.remove[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
Traceback (most recent call last):
  File "/home/dell/StackP.py", line 23, in <module>
    Pqueue.remove()
  File "/home/dell/StackP.py", line 16, in remove
    self.remove.queue[0]
AttributeError: 'function' object has no attribute 'queue'
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
Traceback (most recent call last):
  File "/home/dell/StackP.py", line 24, in <module>
    Pqueue.remove()
  File "/home/dell/StackP.py", line 17, in remove
    self.queue.remove[l-(l-1)]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
[10, 30, 40, 50]
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
5
[10, 30, 40, 50]
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
5
[20, 30, 40, 50]
>>> 
======================= RESTART: /home/dell/StackP.py =======================
10
20
30
40
50
[20, 30, 40, 50]
>>> 
