# C string
In C++ the are two different types of strings. The old <strong>c string</strong> and the <strong>std::string</strong>. In this
post I will talk about the c string and in the upcomming post I will continue with std::string. 

### Introduction
A <strong>c string</strong> is nothing more than an array of chars. But to be a valid <strong>c string</strong> a terminating <strong>null character</strong> is
needed. This null character is the ASCII character with a value of 0. [ASCII](https://en.wikipedia.org/wiki/ASCII) is a character encoding standard where each character is assigned a value between 0 and 255. The benefit of this terminating character is that you don't need to hold the size of the array because the programm can look for a terminating character. For example this would be a valid string:
```cpp
char str[] = {'H','e','l','l','o','\0'};
std::cout << str << std::endl;
```
As you [can see](https://wandbox.org/permlink/7N6jQmMtvSZBvGus) this will print out the string <italic>hello</hello>. However if we add another terminating character in the middle of the string
```cpp
char str[] = {'H','e','l','\0','l','o','\0'};
std::cout << str << std::endl;
```
the program thinks that the string ends after three characters and thereofore will [only print](https://wandbox.org/permlink/EkZ6lBpWNLWp6SPP) the first three characters.

Since <strong> c strings</strong> are simply arrays of chars we can also access a single character of the string with the <strong>[] operator</strong>:
```cpp
char str[] = {'H','e','l','l','o','\0'};
std::cout << str[1] << std::endl;
```
[In this example](https://wandbox.org/permlink/UWZvGWQtmNTifM4z) the program prints out the second character 'e'.

### String literals
A "string literal" is a sequence of characters enclosed in double quotation marks (" "). String literals are used to represent a sequence of characters which, taken together, form a null-terminated string. In this case the compiler will add the terminating character at the end of the string. In this way we can write
```cpp
char str[] = "Hello";
std::cout << str << std::endl;
```
[to create] a <strong>C string</strong>. But keep in mind that the size of the array ist still 6 because at the end there is still the terminating character.

### Using strings in functions
Because a <strong>C string</strong> is only an array of characters and an array is implicitly converted to a pointer, we can pass a <string>C string</strong> as a pointer to char. For example we can use a string as an argument for a print function [like this](https://wandbox.org/permlink/CI6uBdmRz4jbS2Tx)
```cpp
void print(char* str)
{
  std::cout << str << std::endl;
}
```
We don't need to pass in any size of the string because the program can determine the length by looking for the terminating character. 

### C string library
Since there are many ways you want to manipluate <strong>C strings</strong> there ist the [c string library](http://www.cplusplus.com/reference/cstring/). Here you can find many functions that may help you. For example if you want to compare two strings you cannot simply use the <strong>== operator</strong> as you can see in this example:
```cpp
char str[] = "Salt";
char str2[] = "Salt";
if (str == str2)
{
  std::cout << "Equal" << std::endl;
}
else
{
  std::cout << "Not equal" << std::endl;
}
```
If you [run the code](https://wandbox.org/permlink/qHdzev5NSpzGUWyF) you can see that the result of the comparison is false even the strings should be the same. The reason for this is the implicitly conversion of an array to a pointer. The truth is in this case that you compare the value of two pointers. And as you can remember the value of a pointer is a memory adress and since you created two strings the memory adresses will always be different and the comparsion will always result in false. Thereby you should use the function [strcmp](http://www.cplusplus.com/reference/cstring/strcmp/) to compare two <strong>C strings</strong>. Since this function does not only compare the strings on equality but also if one string is [lexiographic greater](https://en.wikipedia.org/wiki/Lexicographical_order) the function returns an integer. Is the return value 0 than are the strings equal.
```cpp
char str[] = "Salt";
char str2[] = "Salt";
if (strcmp(str, str2) == 0)
{
  std::cout << "Equal" << std::endl;
}
else
{
  std::cout << "Not equal" << std::endl;
}
```
You can find this code [here](https://wandbox.org/permlink/touY93Z6vfo983Ik). Some other usefull functions are [strlen](http://www.cplusplus.com/reference/cstring/strlen/) which returns the length of a string or [strcat](http://www.cplusplus.com/reference/cstring/strcat/) which concatenates two strings.

### Conclusion
In this post you learned something about the representation of strings in C. Since C++ is based on C the strings still resists. In the next post we will take a look at the C++ string class. Even if you don't be using <strong>C strings</strong> you should know how to handle them since many frameworks are still using them. To train your skills on that topic I provided two playgrounds for you:
- [strlen](https://wandbox.org/permlink/YVjsjtjCuu9KxaBF)
- [reverse string](https://wandbox.org/permlink/MbRVSdcHWoLPDVLz)
