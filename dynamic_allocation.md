# Dynamic Allocation

### Introduction
You will come to some point where you want to create an object during the runtime of a programm. Or you simply want to create an
object inside a function and want to use it outside of the scope. Than you will need to dynamically allocate memory. 

### New and delete
Lets consider we want a function that can create an object for us. We also dont want to return the object by value since the copy of
the object will take some time. Thereby we want to create the object inside the function and than use the same memory adress outside
of the function. So first we will need the memory adress outside of the function. For this we can use a [pointer](references_pointer_2.md]
to store the memory adress. As a dummy object I will use again the <strong>BigObject</strong> so we can follow up what is going under
the hood. Maybe you would start with a function like this:
```cpp
BigObject* createBigObject()
{
  BigObject obj;
  BigObject* ptr = &obj;
  return ptr;
}
```
As you can see we use a pointer to an <strong>BigObject</strong> as return type. However if we want to access the object out of the
function we undefined behaviour. The <strong>BigObject</strong> from the <strong>obj variable</strong> is deconstructed when the
create function ends. But the pointer is still pointing to the memory adress where the <strong>BigObject</strong> lived. So if we are
goint the dereference the pointer we try to read invalid memory. Thereby anything could stand at this memory adress. Maybe you will still
find the old <strong>BigObject</strong> but you could also find and integer or an string. But your programm might still think that
there is a <strong>BigObject</strong>. So we should ask how can we create an object inside a function that will live after the function
has returned?
