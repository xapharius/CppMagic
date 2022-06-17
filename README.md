CppMagic
=======
Ipython cell magic for jupyter notebooks to run and time C++ code.

<br><br>

Usage
--------
Load extension using %load_ext cppmagic.    
Use %%cpp at the beginning of the cell and write your C++ code. Execute to get results or compilation errors.   
Use %%cpp -t to get a timeit result.

<br><br>

Installation
--------
pip install git+git://github.com/xapharius/cppmagic.git

<br><br>

Examples
------------
**example.ipynb**
```
%load_ext cppmagic
```

<br>

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
%%cpp -t

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
- add timeit params


