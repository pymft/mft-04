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

res = math.sin(10)
print(res)
```

### import full module and alias the name of module
```python
import math as m

res = m.sin(10)
print(res)
```

### import specific object from standart library 
```python
from math import sin

res = sin(10)
print(res)
```

