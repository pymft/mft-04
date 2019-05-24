# `import` 

```python
>>> import math
>>> print(math)
... <module 'math' (built-in)>
>>> print(type(math))
... <class 'module'>
```

### import full module

```python
import math

res = math.sin(0.5 * math.pi)
print(res)
```

### import full module and alias the name of module
```python
import math as m

res = m.sin(0.5 * m.pi)
print(res)
```

### import specific object from standard library 
```python
from math import sin, pi

res = sin(0.5*pi)
print(res)
```


### import specific object from standard library and alias the name 
 
```python
from random import randint as rnd

rnd(1, 200)
```