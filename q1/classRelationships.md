# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: Fantasy Books
Description: This class showcases the different fantasy books that majority of children, teenagers and people of all ages read during their free time, a way for them to clear their mind and more.

## New Related Class
Class: Subgenres
Description: Subgenres are smaller, more specific categories that its inside a larger genre.

## Association
Relationship: Contains
Explanation: The beauty of fantasy books that fans of the genre know is that they typically contain a subgenre/s that create a more interesting and captivating read for each book.

## Multiplicity
Multiplicity: 1:Many
Explanation: Although the book mostly follows a more fantasy genre, it can contain more than 1 subgenres for it to be less simple. An example is Harry Potter, its main genre is fantasy, while its sub-genres are urban fantasy, coming of age, mystery and children's fiction.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
