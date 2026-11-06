# Homework 1

## Submission

* Zip your code in upload. It has to be .zip format, and no windows WinRAR or tar ball are accepted. 
* write a word document with your name, info, and screenshots of your code how it should show to prove you have done it right for each of the questions. The word document can be sitting in parallel with the zip file, no need to put it inside of the zip.
* Fail to fulfill this requirement will get 95/100 max.
* Late sumission is at the discretion of professor, and score is maxed to 90/100.

## Requirements

`Total points: 100`

1/ configure your springboot project to deploy using WAR file. 
Run your project with apache tomcat server in your computer. (25 pts)

2/ Configure your springboot project to connect to mysql database. Create a student table with the following data, (25 pts)

```
{
  {
    "student_id": 1,
    "student_name": "John"
    "age": 21
  },
  {
    "student_id": 2,
    "student_name": "Jack"
    "age": 22
  },
  {
    "student_id": 3,
    "student_name": "Tom"
    "age": 23
  }
}
```

Endpoint: `/students/all`

To test it with http get, try to go to your browser and hit `localhost:8080/students/all`, and it should show the above json in the web page.

3/ Write a Http post method endpoint `/students/add` to add a record to your database(Mysql), and prove the record is added using `http get` endpoint from step 2. To access to your database, you will need to read the Topic 2(Next chapter on my courseware) about the Mysql part. (25 pts)

4/ Write a summary of the following annotations. (25 pts)

- @Autowired
- @SpringBootApplication
- @Component
- @Service
- @Repository
- @Configuration
- @RequestMapping vs @GetMapping
- @Bean
- @Qualifier
- @RequestBody

