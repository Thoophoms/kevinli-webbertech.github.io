# Assignment 5 XML Programming

## Submission requirements

* Your word/pdf on top, not in the zip file.
* If you have source code of a project, you can zip and upload it.

## Tasks

1. What is Javascript? And please write a little bit about what versions JS has been gone through and standards, a little history about Javascript.

2. What is unicode?

3. What is Collation in Databases?Links to an external site. And why that matters to database? Please give a good example to explain it.

4. What is the relationship between collation and character sets in database system? Please use solid examples to explain it.

5. Please use python do the following requirements,

Here is movies.xml

```xml
<collection shelf="New Arrivals">

<movie title="Enemy Behind">

<type>War, Thriller</type>

<format>DVD</format>

<year>2003</year>

<rating>PG</rating>

<stars>10</stars>

<description>Talk about a US-Japan war</description>

</movie>

<movie title="Transformers">

<type>Anime, Science Fiction</type>

<format>DVD</format> <year>1989</year>

<rating>R</rating>

<stars>8</stars>

<description>A schientific fiction</description>

</movie>

<movie title="Trigun">

<type>Anime, Action</type>

<format>DVD</format>

<episodes>4</episodes>

<rating>PG</rating>

<stars>10</stars>

<description>Vash the Stampede!</description> </movie>

<movie title="Ishtar">

<type>Comedy</type>

<format>VHS</format>

<rating>PG</rating>

<stars>2</stars>

<description>Viewable boredom</description>

</movie>

</collection>
```

Requirements: I need screenshots if you generate db tables, and sorted_move.xml and step by step screenshots and the final .py code. Java programmers, please try to use python for extra credits if you are short in other scores.

a. read movies.xml from python and print out all the movies, and count how many movies in the list are rated as ‘R’.

b. print out root node ‘s attribute

c. create a Cassandra table using python, and insert everything from xml to the db table called ‘movies’

d. Sort all the rating that is ‘PG’ from Cassandra using python and write to sorted_movie.xml with all the original columns.

6. Once question 5 is done, please write code to read from movies.xml and write to cassandra database, please create keyspace, and table as needed. Prove that it is in the database with python printouts.

> Note: Each tasks or bullet points equally shared the points totally to 100 pts. Your word doc report itself is 10 pts.