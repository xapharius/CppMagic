CppMagic
=======
Ipython cell magic to run and time C++ code.

<br><br>

Usage
--------
Use %%cpp at the beginning of the cell and write your C++ code.   
Use %%cpp -t to get a timeit result.

<br><br>

Install
--------
git clone then in folder run python setup.py install

<br><br>

Example
------------
**example.ipynb**

- Example 1: Get stdout

```
%%cpp

#include <stdio.h>

int main(void) {
   printf("Hello World");
   return 0;
}
```

```
'Hello World'
```

<br>

- Example 2: Time execution (compilation time is excluded)

```
%%cpp

#include <stdio.h>

int main(void) {
   printf("Hello World");
   return 0;
}
```
```
<TimeitResult : 3.45 ms ± 354 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)>
```

<br>

- Example 3: Get compilation errors


```
%%cpp

#include <stdio.h>

int main(void) {
   printf("Hello World")
   return 0;
}

```
```
/tmp/tmpcqw333xf/d72d557b-9e3f-486d-9a72-acf0fbbe9ec6.cpp: In function ‘int main()’:
/tmp/tmpcqw333xf/d72d557b-9e3f-486d-9a72-acf0fbbe9ec6.cpp:6:4: error: expected ‘;’ before ‘return’
    return 0;
    ^
```

<br><br>

TODO:
--------
- test on windows
- test on python 2
- add compiler flags
- add timeit params


