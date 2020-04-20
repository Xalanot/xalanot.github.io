# C++ string
The C++ standard also prvodies a representation of strings. The standard [string class](http://www.cplusplus.com/reference/string/string/)
is an object that represents sequences of character like the c strings. 

### Introduction
A simple skelleton of a string class would look like this
```cpp
class string
{
public:
  string(const char* str_ptr);
private:
  char[] str;
  int size;
}
```
The idea is that you do not need a terminating character anymore since you can store the length of the string as a member variable.
You can also see that you can construct a string from a char pointer. 
```cpp
std::string str("Hello");
std::cout << str << std::endl;
```
Make sure that you include the header <strong><string></strong> to be able to use the string class. You program should now [print
out](https://wandbox.org/permlink/NvcciwP3douh7vRt) the string.
The big difference now between a c string is that the standard string is a own object. Therefore you can also [pass a string as
value to a function](https://wandbox.org/permlink/PlwjgvSRApA0BLH6).
```cpp
void print(std::string str)
{
  std::cout << str << std::endl;
}
```
### Typical string operations
Another benefit of the string class is that there are many member functions to manipulate the string. You can for example get the
size of a string with
```cpp
std::string str("Hello");
std::cout << str.size() << std::endl;
```
This [code snippet](https://wandbox.org/permlink/PlwjgvSRApA0BLH6) will print out the size 5. To access a part of the string you
can use the member function [substr](http://www.cplusplus.com/reference/string/string/substr/).
```cpp
std::string str("Hello");
std::cout << str.substr(0, 3) << std::endl;
```
In [this example](https://wandbox.org/permlink/gEsmuejWgHmBhw65) we get the string "Hel" as the result. Another useful member function
is [find](http://www.cplusplus.com/reference/string/string/find/) which allows to search for a particular substring and to return
the startind index.
```cpp
std::string str("Hello");
std::cout << str.find("ll") << std::endl;
```
[This](https://wandbox.org/permlink/Vb5XtQEkklFan87q) will result in the index 2. Since strings are now handled as objects the
comparison operators have been overwritten. Now we can write more expressive code withoud the need of an extra function.
```cpp
std::string str("Hello");
std::string str2("Hi");
if (str != str2)
{
  std::cout << "Not equal" << std::endl;
}
```
You can find an example [here](https://wandbox.org/permlink/dLma4IhUc3RgsYOn). Sometimes you still need to get a <strong>c string</strong>
out of your <strong>std::string<strong>. You can get a poiner to the null terminated char array with the member function [c_str()](http://www.cplusplus.com/reference/string/string/c_str/).
For example we could use our old print function in this way
```cpp
void print(const char* str)
{
  std::cout << str << std::endl;
}

std::string str("Hello");
print(str.c_str());
```
You can find the code [here](https://wandbox.org/permlink/hTarKIJLFHNMxzCs).

### Memory allocation
When creating a string object you always need to remember the memory allocation of a string bject. Even if the object itself is created
on the stack the inner data (the sequence of characters) is created on the heap. To visualize this behaviour I overloaded the new operator
to see when memeroy is allocated on the heap.
```cpp
static int allocation_count = 0;

void* operator new(size_t)
{
  allocation_count += 1;
  std::cout << "allocation memory on the heap" << std::endl;
  return malloc(size);
}
```
This function simply increment the allocation count variable and than allocates memory like the normal <strong>new operator</strong>.
So lets see what happens if we create a string and pass it to a function.
```cpp
void print(std::string str)
{
    std::cout << str << std::endl;   
}

std::string str("This is a very long string");
print(str);
```
If we now run [this code](https://wandbox.org/permlink/bFRKu7oLK6zYJZZ1) we see that we have two allocations on the heap. Make sure
that your string is long enough otherwise the compiler will optimize the heap allocation for you according to SSO(short string 
optimization). Because we pass the string as value to the function a new string has to be created. For <strong>C strings</strong>
this would never happen since we are always using pointers in those cases. To get rid of that extra allocation we can simply pass
our string as a [reference](reference_pointer_1.md]. 
```cpp
void print(std::string const& str)
{
    std::cout << str << std::endl;   
}
```
[Now](https://wandbox.org/permlink/QsoeGtCYsIs5dPoE) we only have one allocation.

### Conclusion
C++ offers a new way to deal with strings. If you can you should always be using the <strong>std::string</strong>, however there will
come situations where you have to deal with both kinds of strings. Therefore you should be familiar with both. As alway I added some
playgrounds to get familar with the string class:
- [filter](https://wandbox.org/permlink/9czuX3KKVUD0qGrA)
