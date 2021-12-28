#  EX3 - OOP COURSE
# Directed Weighted Graph in Python
## Introduction
In this assigment, we asked to convert the graph implementation we did in Java to Python. We will also finally be required to compare the performance of the program we wrote in Java with the performance of the program we will write in Python. In this task we implemented interfaces that creates a Directed Weighted Graph build from nodes and edges, later, we implemented algorithms class which run algorithms on the graph and then used matplotlib library to present our code in a graphic way.
 
## A view to our code:
An important detail about this project is the fact that we have already done most of the planning and implementation part in the previous project. you can have a look in the link : https://github.com/ChaimW25/ex2.git

That's why most of our hard work will be converting the old project in Java to Python language. It is important to remember that although the languages are similar, they are different, for example, we changed the uses in hasmap to dictionary. In addition The difference between the languages made us design the project differently and in a different structure, for example, We did not have to create a class of 'Edge'. We used the interfaces 'GraphInterface' and 'GraphAlgoInterface' as skeleton to our project and create their implementations in the classes 'DiGraph' and 'GraphAlgo', the class'Node' help us to implement the other classes. In addition, we created 2 tests classes: 'TestDiGraph', 'TestGraphAlgo'.