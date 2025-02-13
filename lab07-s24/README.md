# Overview - Lab 07 Spring 2024

This lab focuses on file IO and working with text manipulation.

It specifies requirements, but not a specific implementation.
This will require some design on your part; I've given some starting questions
to consider below; you will implement code in `src/server_log.py` script.

We also continue to reinforce our workflow using Git, so be sure to make regular
commits and pushes.  Start by writing out your design in comments, and
committing that, then update as you go.

In this lab you may either:
 * Work independently
 * With a "brain storm buddy" in the initial design
 * Using "Pair programming" with a partner where you take turns "driving"
   * See [Pair Programming](docs/pair_programming.md) for more information.
   * If you cannot complete everything before the end of lab, it is YOUR responsibility
     to meet with your partner outside of class and finish the Lab before the start of the next lab.
   * Pair programming requirements remain in force for work completed outside of class.
   * You are *NOT* allowed to work independently if using pair programming model.

All labs are due at the start of the next lab.

# Grading Rubric for week 7
Each week of lab will be based out of 100 possible points.

The points will be distributed according to the following critera:

- 10 Points - Complete correct functionality to answer questions below
- 20 Points - Correctness and appropriateness of final code as graded by lab instructor
- 20 Points - Style points as assigned by PyLint and grader script
  * To receive these points, you must
    * have a reasonable attempt at solving the problem
    * your code should also run without errors
- 15 Points - Initial design effort during first lab period
  * Included in this is the expectation that you do some design in comments *BEFORE* starting to code
    * You are allowed to modify and let your design evolve, but you must show some effort at thinking through the problem
    before starting to code.
- 15 Points - Design of `Domain` class finished before the end of class
- 20 Points - Significant progress toward completing project during lab

Verify your grade with instructor before leaving early.


### Server Logs

This project is inspired by problems encountered by Information Science students.

Given a simplified server log, we need to process the log file and present certain data.

Example data :
<pre>
12/6/20 0:48,137.155.4.99,https://example.net/,2726
9/5/20 4:26,137.155.0.225,http://www.example.com/,2762
1/29/20 22:40,137.155.7.198,https://www.example.com/bit/back.html,2329
6/15/20 14:08,137.155.3.9,http://www.example.com/#breath,2109
5/5/20 12:18,137.155.4.127,https://www.example.com/,2679
11/29/20 5:05,137.155.3.61,https://airplane.example.com/addition.html?brick=afternoon,2277
</pre>

The data is comma separated, with the first item being a date and time (e.g. `9/5/20 4:26`), the
second item is an Internet IP address (e.g. `137.155.0.225`) of client, and third item
web page accessed (e.g. `https://example.net/`), and fourth item the number of bytes accessed.

The IP address is represented by four integers separated by dots.  The first three numbers
represent the subnet, while the last identifies an individual interface within that subnet.
For example, any `134.155.4.x` is a Christopher Newport IP address.

For this lab, we will keep it simple and only be concerned with the domain name.
The `.net`, `.com` part is the *top level domain* and directly to the left of that is the
main domain name; further left represents the subdomain (e.g. `airplane` in last line of example).

So, `www.example.com/bit/back.html`, `http://www.example.com/#breath`, and `https://airplane.example.com` will all
map to `example.com`, while   `example.net` and `example.com` are considered as different domain addresses.
To be clear, `www.example.com` and `example.com` are the same domain address.

After the top level designators (e.g.  `.com` or `.net` ) there is a slash. Anything following
the slash represents either a directory or page.  So that `/balance/bag.php` and `/bag.php` would be
different files in different directories.  The *query strings* appearing after the `?` come to the right after the page location (e.g. `?brick=afternoon`)
This is how variables are passed into a web language, and are not used from a networking perspective.

For this lab, we will ignore the page locations and query strings, and are only concerned with the domain address (e.g. `example.com` or `example.net`).

Write a class called `Domain` in the `domain.py` script to hold the relevant information.
As you read the file and encounter a new domain (e.g. `example.com` or `example.net`), create a new instance of your class.
If the instance already exists, then use it and just add new information as needed from additional

If you create a string from this instance, (e.g. to `print`), show the top-level domain name, and total bytes requested.

Define a `dump` method, that prints the string format described above, and then below indented, print each
unique address that accessed the domain, then slightly indented from that, print
the unique access date, page accessed (if known) and bytes accessed.

>NOTE:  The `Domain` class is required for full credit.  You *ARE* free to add additional classes if you
> feel they are warranted.


Write Python code in `server_log.py` to organize the data to answer the following questions.
1. Print all unique domains and total bytes requested for each sorted by top-level domain name

  As a partial solution, I got
    <pre>
    Total bytes by Domain Name
    example.com          (   3741780)
    example.edu          (    234017)
    </pre>

2. Print the `dump` of all data retrieved from the file

    As a partial solution, I printed this:
    <pre>
    example.com          (   3741780)
        137.155.0.0:
              Date/Time       Bytes    Subdomain  Page
            --------------------------------------------------
            7/25/21 5:54          2146            advertisement/bear  
        137.155.0.103:
              Date/Time       Bytes    Subdomain  Page
            --------------------------------------------------
            4/14/20 22:12         2680 baseball   #blow               
            3/8/20 9:24           2169 breath                         
    </pre>

    This specific formatting is not required, but it should be nice and neat.

3. How many unique IP addresses (clients) are there in data file?
4. How many unique subnets (first 3 numbers only in client IP address) are there in data file?
5. How many unique web domain targets are there (at the `example.net` and `example.com` level)?

# Start by doing some design
  * Add comments to `server_log.py` breaking the down the approach and sub-tasks you need to solve
  * Add comments to `domain.py` identifying likely attributes and methods that you might need in `Domain` class
  * Identify opportunities for defining functions to break up the problem and simplify organization
  * Commit this design *BEFORE* you start coding
    * You may define function *stubs* with `def` statement and `pass` as part of this design
    * You *ARE* allowed to modify your design as you go, but you must make a good faith effort at design before starting to code for full credit
# Notes and Suggestions
  * We have not provided any unit tests; this is your opportunity for an open ended design to solve the problem
  * Likewise, we have not specified any particular output format; you design
    * The answers to the above 5 questions should be clear and well organized when you run your code
  * You might find that Python dictionaries (`dict`)  are useful to organize your data.
  * For some questions, a Python `set` might be useful.
  * You do *NOT* necessarily need all of the information in the file.
  * Debugging with the big file is going to be difficult; I suggest you create a shorter data file for initial testing
    *  In `bash` (including `gitbash`), you can use the `tail -n 5 <file_name>` to show the last 5 lines of a file
    *  Using `> output.txt` will *re-direct* console output to the file `output.txt`
    *  So from the `data/` folder in `gitbash` terminal, the command
       `tail -n 5 csdata_base_V1_08312021_0736am.csv > shorter.csv` would create a test file using the last 5 lines of the data file
  * The main file has a header; I used the following code to check for header:
<pre>
              if csv_data[0][0] == '\ufeff':
                # Checks for magic character
                print(f"|{ csv_data }|")
                continue # Skip header
</pre>
  * There is NO WebCAT submission this week; just push your code to GitLab


Good luck and have fun!

######

Copyright 2024 Christopher Newport University

Only for posting on student-gitlab.pcs.cnu.edu
