# Pointer and references (1)

### Possible topics

- Basic pointer and references with variables
- Using references in functions
- How to create a pointer to a new variable
- Why do I want to use references

### Introduction
One of the most confusing things about starting with C++ are pointers and references. In this blog post I will give a deep dive into it and try to explain the topic with alots of examples. Even this post is for the beginner, you can learn a lot from it. To get started we need to think about how variables are stored in memory and how we can access them. Lets say we want to create an integer with the value 5. To be able to easily access this integer we assign a variable with the name <strong>a</strong> to it.

```cpp
int a = 5;
```
Now we can simply use this variable by its name, but how does our program know, where the value of <strong>a</strong> is? Lets go a little bit deeper in the codeline above and see what happens under the hood. We wanted to create an integer with the value of 5. Therefore the computer needs to create this integer and store it somewhere. For the sake of simplicity we call this playe <strong>ma_0</strong> for "memory adress 0". In a real world scenario the adress would be a bunch of hexadecimal numbers. So far so good, but now we want to assign the value to our variable <strong>a</strong>. Instead of simply assigning the value to the variable, the computer will assign the memory adress <strong>ma_0</strong> to <strong>a</strong>. So everytime we call the variable <strong>a</strong> the program will look up the memory adress of <strong>a</strong> and retrieve the value from there. If now we want to know the memory adress of a, we can use the & operator in C++. The following line is simply printing the memory adress of our variable <strong>a</strong> (as I mentioned this will only be a bunch of hexnumber and may differ from time to times). 
  
 ```cpp
 std::cout << "memory adress: " << &a << endl;
 ```
 
### References
So now we can acess the memory adress, but what can we do with it? A first intuition would be to use this memory adress to assign another variable, lets call it <strong>b</strong>, to it. We call a variable which is constructed from a memory adress a reference. The syntax for this type is a trailing <strong>&</strong>. But what are the differences to assigning another variable <strong>c</strong> to the variable <strong>a</strong>?
 
 ```cpp
 int a = 5;
 int& b = a;
 int c = a;
 ```
If we print the values, we will see no differences:

```cpp
std::cout << "value of a: " << a << std::endl;
std::cout << "value of b: " << b << std::endl;
std::cout << "value of c: " << c << std::endl;
```

But if we print out the memory adress, we see what we expect:

```cpp
std::cout << "memory adress of a: " << &a << std::endl;
std::cout << "memory adress of b: " << &b << std::endl;
std::cout << "memory adress of c: " << &c << std::endl;
```

The adresses of <strong>a</strong> and <strong>b</strong> are the same but <strong>c</strong> is different. So what does this really mean? The variable <strong>b</strong> is referencing to the variable <strong>a</strong>. Therefore no new integer has to be created, since <strong>b</strong> is only refering to the integer at <strong>ma_0</strong>. But for variable <strong>c</strong> a integer has to be created (copied) based on the value of <strong>a</strong> at another memory adress <strong>ma_1</strong>. If we are now going to change the value of <strong>a</strong>, we are actually changing the value at <strong>ma_0</strong> and therefore the value of <strong>b</strong> is also changed. For the variable <strong>c</strong> nothing changes since the value of it is at <strong>ma_1</strong>:

```cpp
a = 10;
std::cout << "value of a: " << a << std::endl;
std::cout << "value of b: " << b << std::endl;
std::cout << "value of c: " << c << std::endl;
```

A full link to the code can be found [here](https://wandbox.org/permlink/Thxpj2WwNnE53rst) feel free to experiment with it. Also make sure that once a reference is assigned it cannot be changed to another memory adress.

### References as function arguments
Until now we may have understood how a reference works but we don't have any benefits of it. For a beginner you will come to a point where you want to write a function who can change the value of a passed variable. Lets say we want to write an increment_by_ten function, which simply increases the passed variable by ten. Before we start with the actual implementation we should think about why the following function does not what we want:

```cpp
void increment_by_ten_value(int var)
{
  a += 10;
  return;
}

int main()
{
  a = 10;
  increment_by_ten_value(a);
  std::cout << "value of a: " << std::endl;
  return 0;
}
```

As the name of the function gives you a hint, the argument is passed by value. This means we will only pass in the value of our variable (10 in this case). So inside the function a new integer is created and assigned to a new variable <strong>var</strong> inside the function scope. Even the value of this new integer <strong>var</strong> is 10, the memory location is another. Therefore increasing the value by ten will only increase the value at the memory adress of <strong>var</strong> but not on the memory adress of <strong>a</strong>. To show this behaviour a bit better I will add some cout messages [in the code](https://wandbox.org/permlink/ILXaM1XW2mDf0qyg).

So how can we use the same memory adress inside and outside of the function? We need to pass the variable by reference. A possible implementation is the following:

```cpp
void increment_by_ten_reference(int& var)
{
  var += 10;
  return
}

int main()
{
  a = 10;
  increment_by_ten_reference(a);
  cout << "value of a: " << a << endl;
  return 0;
}
```

Again I added [some code](https://wandbox.org/permlink/2H2zNkvjqC50MRAK) with some debug informations. This time the function has a reference to the variable <strong>a</strong> from the main scope, so the increment takes place directly at the memory adress of <strong>a</strong>. Consequently the value from <strong>a</strong> changed as expected.
Another huge benefit of passing an argument by reference is a faster runtime of your program. To understand why we need to remember what happens when we pass a variable by value. Since the function only knows the value of the variable, it needs to save the value somewhere and creates a new object with the passed value. So we have to pay the price of the initialization. If we consider an object which is very expensive to create (for simplicity we say it takes 10 seconds on every computer) and we want to use this object inside a function, we don't want to copy the same object every time. If we pass the object by reference, we only tell the compiler at which memory adress our object lives. This is the same cost for every object wheter it has a big or small initialization time. I provided a little example [here](https://wandbox.org/permlink/Kes4YvFOr6YYv2ti). Don't worry to much about the BigObject object. It is simple dummy object, which does nothing than waiting for 10 seconds whenever it gets initialized or copied. Also make sure to re-run the code to observe the differences.

### Conclusions
In this post I gave a brief introduction on how to create a reference, change the value of a refered variable and use references in functions. To make sure you learned something I provided three small playgrounds, where you can check your understanding of references:
- [reference train](https://wandbox.org/permlink/2LQD473YlZ9wOZV6)
- [swap function](https://wandbox.org/permlink/LXUFfBcvXyj06DNW)

In a [next post](pointer_references_2.md) we will take a closer look at pointers.
