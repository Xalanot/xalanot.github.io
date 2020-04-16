# Dynamic Allocation

### Introduction
You will come to some point where you want to create an object during the runtime of a programm. Or you simply want to create an
object inside a function and want to use it outside of the scope. Than you will need to dynamically allocate memory. But before we start on how to do it lets rewind the concepts of the stack and the heap. On the stack the allocation happens on contiguous blocks of memory. The size of memory to be allocated must be known to the compiler. But on the heap the memory is allocated during execution of instructions written by programmers. This is what we call dynamic allocation.

### New operator
Lets consider we want a function that can create an object for us. We also dont want to return the object by value since the copy of
the object will take some time. Thereby we want to create the object inside the function and than use the same memory adress outside
of the function. So first we will need the memory adress outside of the function. For this we can use a [pointer](references_pointer_2.md]
to store the memory adress. As a dummy object I will use again the <strong>VerboseObject</strong> so we can follow up what is going under
the hood. Maybe you would start with a function like this:
```cpp
VerboseObject* createVerboseObject()
{
  VerboseObject obj;
  VerboseObject* ptr = &obj;
  return ptr;
}
```
As you can see we use a pointer to an <strong>VerboseObject</strong> as return type. However if we want to access the object out of the
function we undefined behaviour. The <strong>VerboseObject</strong> from the <strong>obj variable</strong> is deconstructed when the
create function ends. But the pointer is still pointing to the memory adress where the <strong>VerboseObject</strong> lived. So if we are
goint the dereference the pointer we try to read invalid memory. Thereby anything could stand at this memory adress. Maybe you will still
find the old <strong>VerboseObject</strong> but you could also find and integer or an string. But your programm might still think that
there is a <strong>VerboseObject</strong>. So we should ask how can we create an object inside a function that will live after the function has returned? You need to use the <strong>new</strong> operator. For example we can create our object on a free memory adress like this:
```cpp
new VerboseObject;
```
But how can we access our object now? We have neither a variable assigned to it nor the memory adress. Therefore the <strong>new operator</strong> returns the memory adress and we can store it in a pointer.
```cpp
VerboseObject* ptr = new VerboseObject;
```
Now we can rewrite our function.
```cpp
VerboseObject* createVerboseObject()
{
  VerboseObject* ptr = new VerboseObject;
  return ptr;
}
```

### Delete operator
Since we wanted an operator where we can create an object that lives outside of our scope, we need to tell the programm when we want to deconstruct it. But we can only access our object via the assigned pointer. With the <strong>delete operator</strong> we can deconstruct an object at a given memory adress. To tell the memory adress we can simply use our pointer.
```cpp
VerboseObject* ptr = new VerboseObject;
delete ptr;
```
If you re-run [this code](https://wandbox.org/permlink/O7lTMgndlJ8Yy9RA) you can see that the deconstructor of <strong>VerboseObject</strong> is called.

### Dynamic arrays
With the new operator it is also possible to construct an array of objects. In this example we will dynamically construct an array of 3 integer values. Assign values to it and afterwards delete the array.
```cpp
int* arr = new int[3];
arr[0] = 0;
arr[1] = 1;
arr[2] = 2;
delete[] arr;
```
In [the last post](references_pointer_2.md) we have seen how we can store and access an array with a pointer. The only difference between a normal object and an array of objects is that you need to use the <strong>[]</strong> with the new and delete operator. If you would only call the normal <strong>delete operator</strong> you would only deconstruct the first element of the array. The good news here is that your allocator keeps track of the size of the array and therefore you don't need to specify the size while deleting the array.

### Some common pitfalls
What will happen if we reassign our pointer to another object? Consider we created an <strong>VerboseObject</strong> with the <strong>new</strong> operator and assign our pointer to it. Afterwards we create another <strong>VerboseObject</strong> and reassign our pointer to it.
```cpp
VerboseObject* ptr = new VerboseObject;
ptr = new VerboseObject;
```
We created two objects but have only one pointer to store a memory adress. Thereby the first memory adress is lost and we cannot access our object anymore. But even worse the object will now live "foreever" since we cannot deconstruct it. One possible solution would be to delete the first object first and than create another object and reassign it.
```cpp
VerboseObject* ptr = new VerboseObject;
delete ptr;
ptr = new Verbosebject;
```
You may wonder how can I still use my pointer after the deletion. You need to remember that a pointer only stores a memory adress and with the <strong>delete operator</strong> we are telling our programm only to deconstruct the object at the memory adress of our pointer but not our pointer itself.

Another problem that can arise is that you delete an object another pointer is still pointing to. Lets take a look at this code snippet.
```cpp
VerboseObject* ptr = new VerboseObject;
VerboseObject* ptr2 = ptr;
delete ptr;
```
After this the <strong>VerboseObject</strong> has been deconstructed. However <strong>ptr2</strong> is still pointing to the memory adress where the object was stored. If we would dereference <strong>ptr2</strong> we would have undefined behaviour since the object has alreday been deconstructed.
  
As you can see you have to be really carefully with the dynamic allocation. So use it as little as possible and if you have to you should take a look at smart pointers and how they can solve your problem.

### Conclusion
In this post I gave you some use cases why you need to allocate memory on the heap and how you can do it. We learned two new operators new and delete. Also I pointed out some dangerous pitfalls when using dynamic allocation. As always you will find some playgrounds to test your knowledge.
