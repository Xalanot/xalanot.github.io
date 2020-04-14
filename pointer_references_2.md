# Pointer and references (2)

In the last post we discovered how we can use references to access a value based on its memory adress.
In this part we will take a look at pointers.

### Introduction
At the moment we know how to acess the memory adress of a variable and how to create another variable with the same memory adress,
but we cannot save the memory adress. This is where pointers enter the game. We will start with a short code snippet:

```cpp
int a = 7;
int* b = &a;
```

As you can see we declare a pointer with a trailing *. Also on the right hand side we find the memory adress of <strong>a</strong>
and not the variable a by itself. This makes sense since we want to store the memory adress and not the value of <strong>a</strong>.
We can see that the variable <strong>b</strong> holds the memory adress of <strong>a</strong>. So in this case <strong>b</strong> is a
variable with a memory location as value. That's why <strong>b</strong> has a own memory adress. If you know want to get the value of
of the memory adress <strong>b</strong> is pointing to, you need to dereferente the pointer with the * operator:

```cpp
std::cout << "value of a: " << a << std::endl;
std::cout << "memory adress of a: " << &a << std::endl;
std::cout << "value of b: " << b << std::endl;
std::cout << "memory adress of b: " << &b << std::endl;
std::cout << "value at the memory adress b is pointing to: " << *b << std::endl;
```

A full version of this code snippet can be found [here](https://wandbox.org/permlink/nQXEysCOwSiFDSMk)

### Changing the pointer
Since pointer store a memory adress as their value we can simply change the location a pointer is pointing so. For example we have a pointer first pointing to the adress of a variable <strong>a</strong> and than want to point to variable <strong>b</strong>, we only need to set the new memory adress:

```cpp
int a = 1;
int b = 2;
int* ptr = &a;
