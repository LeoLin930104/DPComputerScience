# DPComputerScience
File from classwork

## First class
> ### Content
>     Setting up Development environment. 
>     Git and Visual Studio Code.
>     This year is all about Python.
> ### File
> + [README.md](README.md)

## 2020/09/11
> ### Content
>     Variable types
>     Operations between different types.
>     Casting types
>     Lists and its operation
>     Simple loops
> ### File
> + [variable.py](variable.py)
> + [operater.py](operater.py)

## 2020/09/18
> ### Content
>     Assigning elements in lists
>     Printing with loops
>     Insert elements
>     Insert elements with different types
>     Length of Lists
>     Repeating elements assign
>     Introducing Statements parcially
>     Find Location by index
>     Insert/Remove elements by Index
>     Pop / Push
>     Count
>     Sort
>     Multiple ways of List from 1 to 10
>     Introduce of Filter
>     Sublist: first Inclusive, end exclusive
>     Swap element
>     Shallow Copy, directing to identical RAM * location
> ### Homework
>     Assigned Homework, list_exercises.py, due 2020/09/25 Friday.
> ### File
> + [lists.py](lists.py)
> + [newton.py](newton.py)
> + [list_exercises.py](list_exercises.py)

## 2020/09/25
> ### Content
> #### Dictionary
>     Dictionary in Python
>     Keys and Values
>     Determine if key exist in Dictionary
>     Null Return in Dictionary
>     Remove Data with Keys and Return
>     Emptying the Entire Dictionary
>     Add a new key
> #### Strings
>     Basic Strings
>     Special Characters (escape characters)
>     Raw Text
>     String Resoruces of System
>     Using unicode to Call for Character
>     Iterating using String
>     Formating 
>     Replacing
>     Spliting 
>     Finding
>     Join Lists into String
> ### File
> + [dicts.py](dicts.py)
> + [strings.py](strings.py)
## 2020/09/26
> ### Content
>     Practices of Strings, Dictionary from last class
> ### File
> + [string_exersices.py](string_exersices.py)
## 2020/10/05
> ### Content
>     Introduction to Function
>     Exercise with Newton's Method
> ### File
> + [function.py](function.py)
## 2020/10/17
> ### Content
>     More exercises with Functions
>     Function only do one thing
>     Function has a input and a output
>     Function has pre-conditions and post-conditions
>     Function can be nested in another function
> ### File
> + [function.py](function.py)
## 2020/10/30
> ### Content
>     Generator Functions
>     Yeild(return) without terminating the function
>     Different Pointer creates separate Increament in Squares()
>     Code of the Range Function
>     Fibonacci Function by Generator
> ### Homework
>     Assigned Homework, function_exercises.py, due 2020/11/2 Monday.
> ### File
> + [function.py](function.py)
> + [function_exercises.py](function_exercises.py)
## 2020/11/06
> ### Content
>     Check on the function homework.
>     Introduce a simple text adventure
>     Introduce a complex text adventure 
>     Introducing curses and downlaod
>     Start writing own text adventure
> ### File
> + [function_exercises.py](function_exercises.py)
> + [context.py](Text_Adventure/context.py)
## 2020/11/13
> ### Content
>     Revise on the function homework.
>     Continue on Text Adventure
>     Wrote Function in Text Adventure that uses Curses
>     Uses functions to make story line
>     Uses Up/Down Key Strokes to make options in Menu
>     Seperates Function of Drawing Menu and Calling consecutive story line
>     Reconnects to the idea that function only to one thing
> ### File
> + [context.py](Text_Adventure/context.py)
> + [story.py](Text_Adventure/story.py)
## 2020/11/20
> ### Content
> #### Text Adventure
>     Recursive Functions used on Text Adventure, causing stack overflowing
>     Return before calling next function solves the stacking problem.
>     Presents Written stories.
> #### Object Orientation
>     Start with introduction to Object Orientation in Python
>     Wrote Example Class Circle
> ### File
> + [context.py](Text_Adventure/context.py)
> + [story.py](Text_Adventure/story.py)
> + [Circle.py](Objects/Circle.py)
## 2020/11/27
> ### Content
>     Writing other class: Rectangle, RegularPolygon
>     Annotation to Property, Setter
>     Modify default functions
> ### File
> + [RegularPolygon.py](Objects/RegularPolygon.py)
> + [Rectangle.py](Objects/Rectangle.py)
> + [Circle.py](Objects/Circle.py)
## 2020/12/04
> ### Content
>     Discussing about what is our big project Going to be,
>     There were options of:
>     A Store System, managaing the Items...
>     A Bug Tracking System, uses network that keeps track of running programs...
>     A Social Media, an application form of Facebook, Instagram, Snapchat, Twitter...
>     An IDOS, this is a System that our School uses, we want to make it better...
>     A ManageBac, another System that out School uses, we want to make it better...
>     
>     As a result, we have chosen to make our own Social Media..............ExchangeGram
> ### File
> + [ExchangeGram](ExchangeGram)
## 2020/12/09
> ### Content
>     To continue to program, there was a brief introduction to extension
>     classes extend super class to be able utilize super class with variation of its own.
>     Short examnple of Pentagon as child class of RegularPolygon.
> ### File
> + [Objects/Pentagon.py](Objects/Pentagon.py)
## 2020/12/11
> ### Content
>     We initialized a configuration file that can help us luanch the correct file, start client, wherever we are in the ExchangeGram folder.
>     We created our application file where are write our constructor and view initializer.
>     The initializer itself calls a sign_in file that construct all the objects need to fill the application window, pack up the windows and items and return it to the application in order to start_client.
> ### File
> + [ExchangeGram/.vscode/launch.json](ExchangeGram/.vscode/launch.json)
> + [ExchangeGram/start_client.py](ExchangeGram/start_client.py)
> + [ExchangeGram/client/app.py](ExchangeGram/client/app.py)
> + [ExchangeGram/client/view/sign_in.py](ExchangeGram/client/view/sign_in.py)
> + [ExchangeGram/client/view/theme.py](ExchangeGram/client/view/theme.py)
## 2020/12/18
> ### Content
>     We have finished the Sign in View Page, it contains: 
>     - A Username Label, A Username Entry,
>     - A Password Label, A Password Entry,
>     - A Sign in Button, A Cancel Button,
>     - A Register Label, A Register Button.
>     
>     We have finished the Register Page, it contains:
>     - A Email Label, A Email Entry, A Email Error Label,
>     - A Username Label, A Username Entry, A Username Error Label,
>     - A Password Label, A Password Entry, 
>     - A Confirm Label, A Confirm Entry, A Password Error Label,
>     - A Register Button, A Cancel Button.
> ### File
> + [ExchangeGram/client/view/sign_in.py](ExchangeGram/client/view/sign_in.py)
> + [ExchangeGram/client/view/register.py](ExchangeGram/client/view/register.py)
## 2020/12/28
> ### Content
>     Introduction to Algorithms.
>     Details to Sorting Algorithms: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort.
>     Practice Writing Sorting Algorithms...
>     Details to Searching Algorithms: Linear Search, Binary Search.
>     Practice Writing Searching Algorithms...
>     Practice Writing miscellaneous algorithms...
> ### File
> + [Algorithms/sort.py](Algorithms/sort.py)
> + [Algorithms/search.py](Algorithms/search.py)
> + [Algorithms/miscellaneous.py](Algorithms/miscellaneous.py)
## 2021/01/04
> ### Content
>     Introduction to Data Structures.
>     Details to FILO(First In Last Out) and FIFO(First In First Out)
>     Practice Writing Data Structures...Stack and Queue
>     Introduction to Doobly Linked List...
>     Challenge us to Write Doobly Linked List...
> ### File
> + [DataStructures/stack.py](DataStructures/stac.py)
> + [DataStructures/queue.py](DataStructures/queue.py)
> + [DataStructures/linkedlist.py](DataStructures/linkedlist.py)
## 2021/01/08
> ### Content
>     Finishing up Register Page
>     Completing Validating Function
> ### File
> + [ExchangeGram/register.py](ExchangeGram/register.py)
## 2021/01/11
> ### Content
>     Finishing up LinkedList
> ### File
> + [DataStructures/linkedlist.py](DataStructures/linkedlist.py)
    