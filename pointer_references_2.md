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

As you can see we declare a pointer with a trailing \*. Also on the right hand side we find the memory adress of <strong>a</strong>
and not the variable a by itself. This makes sense since we want to store the memory adress and not the value of <strong>a</strong>.
We can see that the variable <strong>b</strong> holds the memory adress of <strong>a</strong>. So in this case <strong>b</strong> is a
variable with a memory location as value. That's why <strong>b</strong> has a own memory adress. If you know want to get the value of
of the memory adress <strong>b</strong> is pointing to, you need to dereferente the pointer with the \* operator:

```cpp
std::cout << "value of a: " << a << std::endl;
std::cout << "memory adress of a: " << &a << std::endl;
std::cout << "value of b: " << b << std::endl;
std::cout << "memory adress of b: " << &b << std::endl;
std::cout << "value at the memory adress b is pointing to: " << *b << std::endl;
```
You can also change the value of the dereferenced pointer while only having access to the pointer:

```cpp
*b = 5;
std::cout << "value of a: " << a << std::endl;
std::cout << "value of dereferenced ptr: " << *b << std::endl;
```
A full version of this code snippet can be found [here](https://wandbox.org/permlink/q0datDWfKjbqgRp5). Since the pointer points to the memory adress of <strong>a</strong> we also changed the value of <strong>a</strong>.

### Size of a ptr
Pointers store a memory adress as their value. Since the most data types need more space than a single memory line, a pointer only points to the beginning of an object. Thereby every pointer has the same size independent to which object the pointer is pointing to. But how does the program know the full value of our object? We are telling through the type identifier to what an object our pointer is pointing to and the program will interpret this adress as the object. This carries some risk, because we could be lying and tell the program the wrong data type. 

```cpp
int a = 5;
float* b = &a;
```

Thankfully the compiler will catch this and give us a hint not to do [this](https://wandbox.org/permlink/ChyC4Dyi6TFPj4yJ). 

### Changing the pointer
Since pointer store a memory adress as their value we can simply change the location a pointer is pointing to. For example we have a pointer first pointing to the adress of a variable <strong>a</strong> and than want to point to variable <strong>b</strong>, we only need to set the new memory adress as the value:

```cpp
int a = 1;
int b = 2;
int* ptr = &a;
std::cout << "value of dereferenced ptr before swap: " << *ptr << std::endl;
ptr = &b;
std::cout << "value of dereferenced ptr after swap: " << *ptr << std::endl;
```

This allows us to easily swap variables without the need of copying the data to another memory adress. Let's try to reimplement the swap function with pointers instead of references.

```cpp
void swap(int* a, int* b)
{
  int* tmp = a;
  a = b;
  b = tmp;
  return;
}

int a = 5;
int b = 10;
swap(&a, &b);
```
Notice that it looks like we are copying the data, but really we are only copying the memory adresses. You can find a comparison between this and the old version [here](https://wandbox.org/permlink/V23q9FD7eFSace3L). I used the BigObject from last time to show the benefits. Again you need to re-run the code. Also you may have noticed that we pass in the memory adress of our variables instead the variables themself. Since the function expects two pointers and pointers are constructed based on a memory adress we need to use the & operator.

### From pointers to arrays
Pointers can also be used to construct an array of an object. An array is a data structure consisting of a collection of objects. Every element is accessible by an index. For example we want an integer array with the values 10, 20, 30. The idea is now to construct this three integers and allign them next to eachoter in the memory. Than we can use a pointer to point to the first element. If we now want to access the second element we can simply jump to next integer adress by adding the size of an integer (mostly 4 bytes) to our adress. And if we want to access the third element we add two times the size of an int to our starting adress. With this technique we can access every element in an array.

```cpp
int arr[] = {10, 20, 30};
std::cout << "array at index 1 with the [] operator: " << arr[1] << std::endl;
std::cout << "array at index 1 with the * operator: " << *(arr + 1) << std::endl;
```
As you can see [here](https://wandbox.org/permlink/5bYBo4sB01sBVWDi) both methods will print out the same. The reason for this is that <strong>arr</strong> is implicitly converted to a pointer. Also the <strong>+ operator</strong> for pointers are overloaded, so we can jump to the next adress by simpy adding 1 to the pointer and the programm will intern lookup the size of the stored objects and add it to the memory adress. For simplicity instead of writing <strong>\*(arr + 1)</strong> you can use the <strong>[]</strong> operator.

Also if you want to use your arrays in a function you will pass them as a pointer. For example we want a function to print the second element, we could do this like:
```cpp
void print_second_element(int* arr)
{
  std::cout << arr[1] << std::endl;
}
```
Note that we can still use the <strong>[]</strong> operator. Since inside the function the programm does not know the size of function, it cannot warn us about an index [out of the range of that array](https://wandbox.org/permlink/xTgb41UCBMml2IfQ).
 
```cpp
int arr = {10, 20, 30};
std::cout << arr[100] << std::endl;
```
Most of the time the value is simply 0 but we have no real knowledge about it.
  
### Conclusion
In this part I introduec the basic idea of pointers and how you can use them. As a next step check out the post about dynamic allocation and how you use pointer for that. Again I provided some small playgrounds for you.

- [Pointer train](https://wandbox.org/permlink/3eGnQ3tWnfGSnNsG)
- [Array to pointer](https://wandbox.org/permlink/4tVSDd1J6DUY7kHl)
- [Reverese an array](https://wandbox.org/permlink/YwScLLZ34K6mldbW)
