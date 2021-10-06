 # Creating & manipulation databases with python

This program creates a database filled with books introduced by the user.

## Objective
The objective of this exercise is to compare the pro's & contras of the used methods to store data.

## Description

- This program actually contains 3 sub programs, all of them used with the intention of creating and using databases.
- The databases are filled with books introduced by the user of the selected program.
- The book structure consists of dictionaries in which you can find the following keys:
  - 'name': where the user enters the name of the book.
  - 'author': where the user enters the name of the author of said book
  - 'status': marks the status if the book, if it is read or not.
  - 'ID': used in the 'project_files' & 'project_json' to identify the books
- Finally, project_lists use lists as meanings of 'storing' data, project_files use the module cvs and cvs files to store the data and project_json creates and use a json as means to store the data.

### Pro's & Con's
- project_lists: as it is a very simple data type is easy to manipulate and makes up for a very simple code if needed. 
The downside is that it does not store the data once the program is finished, so it is not an useful method to store data longtime
Instead of lists we could have also used sets or dictionaries but not tuples, as they are not a mutable type of data.
- project_files: created with the csv library, this program allows us to store data in csv files which can be then used in other programs like Excel.
(Pro) By using csv we could store the data permanently in a document and we could access it whenever we needed. 
(Contra) The downside is that we had to open the document in all the created functions and I think that wastes a high amount of resources and doesn't allow us to simplify the code.
- project_json: JavaScript Object Notation.
(Pro) In my opinion the most useful type of data storage. It is very easy to use them and it allows us  to simplify the code, expend less resources and permanently store the data.
(Contra) With a lot of stored data it could be hard to work with jsons in the IDE console.

### Conclusion
If I had to choose one of the methods tried in this repository, I would choose jsons.
It simplifies the code and allowed me to work with dictionaries and lists, which were very useful in the design of the book structure.

### Executing program
Enter the package you want to try and run the app_name.py file
you can also access the books.csv and book.json in each package if you rather see the stored data.

## Authors
[@rebecalvarezc](https://www.linkedin.com/in/rebeca-alvarez-cepeda/)
