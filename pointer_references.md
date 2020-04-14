# Pointer and references

### Possible topics

- Basic pointer and references with variables
- Using references in functions
- How to create a pointer to a new variable

### Introduction
One of the most confusing things about starting with C++ are the concepts of pointers and references. In this blog post I will give a deep dive into it and try to explain the topic with alots of examples. Even this post is for the beginner, you can learn a lot from it. To get startet we need to think about how variables are stored in memory and how we can access them. Lets say we want to create an integer with the value 5. To be able to easily access this integer we assign a variable with the name <strong>a</strong> to it.

```cpp
int a = 5;
```
Now we can simply use this variable by its name, but how does our program know, where the value of <strong>a</strong> is? Lets go a little bit deeper in the codeline above and see what happens under the hood. We wanted to create an integer with the value of 5. Therefore the computer needs to create this integer and store it somewhere. For the sake of simplicity we call this playe <strong>ma_0</strong> for "memory adress 0". In a real world scenario the adress would be a bunch of hexadecimal numbers. So far so good, but now we want to assign the value to our variable <strong>a</strong>. Instead of simply assigning the value to the variable, the computer will assign the memory adress <strong>ma_0</strong> to <strong>a</strong>. So everytime we call the variable <strong>a</strong> the program will look up the memory adress of <strong>a</strong> and retrieve the value from there. If now we want to know the memory adress of a, we can use the & operator in C++. The following line is simply printing the memory adress of our variable <strong>a</strong> (as I mentioned this will only be a bunch of hexnumber and may differ from time to times). 
  
 ```cpp
 std::cout << "memory adress: " << &a << endl;
 ```
 
 ### References
 
