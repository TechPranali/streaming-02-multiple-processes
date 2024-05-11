# Project: Concurrent Processing & Resource Sharing

Author: Pranali Baban Dhobale

Repository: [Github Repo](https://github.com/TechPranali/streaming-02-multiple-processes)

## Introduction

This project delves into the dynamics when multiple processes are concurrently accessing a shared resource. The shared resource can be diverse, ranging from a SQLite database, a queue, or even an office printer. Essentially, it simulates scenarios where multiple users, locations, or programs interact with a shared database simultaneously.

## Requirements

Before getting started, ensure the following prerequisites are met:

1. Git
2. Python 3.7+ (preferably 3.11+)
3. VS Code Editor
4. VS Code Extension: Python (by Microsoft)

## Task 1: Fork 

Begin by forking this repository into your GitHub account.

## Task 2: Clone

Next, clone your newly forked GitHub repository to your local machine's Documents folder.


## Task 3. Explore

Explore your new project repo in VS Code on your local machine.

## Task 4. Execute Check Script

Execute 00_check_core.py to generate useful information.

```python
python 00_check_core.py
```

## Task 5. Execute Multiple Processes Project Script

Execute multiple_processes.py.

````python
python multiple_processes.py
````

Read the output. Read the code. 
Try to figure out what's going on. 

1. What libraries did we import? 
datetime
logging
multiprocessing
os
platform
sqlite3
sys
time

1. Where do we set the TASK_DURATION_SECONDS?
```python
TASK_DURATION_SECONDS = 3 # TODO: increase this to 3 and see what happens
```

1. How many functions are defined?
7

1. What are the function names? 
```python
recreate_database
create_table
drop_table
insert_pet
process_one
process_two
process_three
```

1. In general, what does each function do? 
```python
recreate_database():
```
This function is responsible for resetting the database to a clean state. It does this by first dropping the existing table (if it exists) and then creating a new table. It's useful for ensuring that each run of the script starts with a fresh database setup.

```python
create_table():
```
This function establishes a new table within the database. It opens a connection to the SQLite database, creates a cursor to execute SQL commands, defines and executes a SQL statement to create a table, and then commits the changes. It handles exceptions that might occur during these operations and logs appropriate messages.

```python
drop_table():
```
The function removes a table from the database, if it exists. It opens a connection to the database, creates a cursor, executes a SQL command to drop the table, commits the transaction, and closes the connection. It also handles errors, logging them appropriately.

```python
insert_pet(process, name, breed):
```
This function is used to insert records into the database table. It takes parameters specifying the process (for logging purposes), and the name and breed of the pet to be added. The function handles the database connection, executes the SQL insertion command, sleeps for a defined duration to simulate a long-running task (illustrating concurrency issues), commits the changes, and handles any errors that occur.

```python
process_one():
```
A function that defines a specific series of database operations simulating a process. In this case, it inserts two pet records into the database. This function is intended to run in its own process, demonstrating concurrent access to the database.

```python
process_two():
```
Similar to process_one, this function also simulates a distinct process by inserting another set of pet records into the database. It runs in a separate process and contributes to the demonstration of concurrent database access.

```python
process_three():
```
This function, again similar to the previous two process functions, inserts a unique set of pet records, running in a separate process to add to the concurrency demonstration.

1. Where does the execution begin? Hint: generally at the end of the file.
```python
if __name__ == "__main__":
```

1. How many processes do we start? How many records does each process insert?

In this first run, we start 3 processes, 
each inserting 2 records into a shared database 
(for a total of 6 records inserted.)

In each case, the process gets a connection to the database, 
and a cursor to execute SQL statements.
It inserts a record, and exits the database quickly.

In general, we're successful and six new records get inserted. 

### PROJECT TASK 1 NOTES - Concurrent Multiprocessing Example (quick processes)
Output of executing multiple_processes.py with Task Duration set to 0 for P1 insert of pet Ace and P3 insert of pet Emma, both returned error: database is locked. This stems from concurrent write attempts to the SQLite database. SQLite handles concurrency through a locking mechanism that prevents more than one process from writing to the database simultaneously. When multiple processes attempt to write at the same time, some processes may be blocked, leading to these errors. 

## Task 6. Execute Multiple Processes Script with Longer Tasks

For the second run, modify the task duration to make each task take 3 seconds. 
Hint: Look for the TODO.
Run the script again. 
With the longer tasks, we now get into trouble - 
one process will have the database open and be working on it - 
then when another process tries to do the same, it can't and 
we end up with errors. 

### PROJECT TASK 2 NOTES - Concurrent Multiprocessing Example (longer-running processes)
Output of executing multiple_processes.py with Task Duration set to 3 for P1 insert of pet Ace and P2 insert of pet Cooper, both returned error: database is locked. This stems from concurrent write attempts to the SQLite database. SQLite handles concurrency through a locking mechanism that prevents more than one process from writing to the database simultaneously. When multiple processes attempt to write at the same time, some processes may be blocked, leading to these errors.

## Task 7. Document Results After Each Run

To clear the terminal, in the terminal window, type clear and hit enter or return. 

`clear`

To document results, clear the terminal, run the script, and paste all of the terminal contents into the output file.

Use out0.txt to document the first run. 

Use out3.txt to document the second run.

###  PROJECT TASK 3 NOTES - Stream Processing Example
 - copy process_streaming_0.py from the Module 1 repo: [P1: Streaming 01 Getting Started](https://github.com/tfmontague/streaming-01-getting-started) and paste to parent local streaming-02-multiple-processes folder
 - copy April 2024's nutrient.csv from [USDA FoodData Central](https://fdc.nal.usda.gov/download-datasets.html)and paste to parent local streaming-02-multiple-processes folder

###  PROJECT TASK 4 NOTES - Custom Stream from CSV Script
 - change process_streaming_0.py Python script name to process_streaming_tmontague.py
 - confirm nutrient.csv file exists in appropriate location from TASK 3
 - refactor process_streaming_tmontague.py Python script to stream from nutrient.csv into new file named out9.txt
    - change python script INPUT_FILE_NAME line from
    ```python
    INPUT_FILE_NAME = "batchfile_0_farenheit.csv"
    ``` 
    
    to

    ```python
    INPUT_FILE_NAME = "nutrient.csv"
    ```

    - change define(row) to:
    ```python
    id, name, unit_name, nutrient_nbr, rank, time = row
    ```

    - refactor the code create a custom stream from csv script that streams from the nutrient.CSV file into a new file named out9.txt. The script should Generate one record every 1-3 seconds to out9.txt The code should write the output to out9.txt

    - execute the script

    ```python
    python process_streaming_tmontague.py
    ```

    - Run long enough to write ten or more records to out9.txt

    - Stop the script in terminal using: 
    
    ```python
    Ctrl+C
    ``` 
-----

## Helpful Information

To get more help on the early tasks, see [streaming-01-getting-started](https://github.com/denisecase/streaming-01-getting-started).

### Select All, Copy, Paste

On Windows the select all, copy, paste hotkeys are:

- CTRL a 
- CTRL c 
- CTRL v 

On a Mac the select all, copy, paste hotkeys are:

- Command a
- Command c
- Command v

Detailed copy/paste instructions (as needed)

1. To use these keys to transfer your output into a file, 
clear the terminal, run the script, then click in the terminal to make it active.
1. To select all terminal content, hold CTRL and the 'a' key together. 
1. To copy the selected content, hold CTRL and the 'c' key together. 
1. To paste, open the destination file (e.g. out0.py) for editing.
1. Click somewhere in the destination file to make it the active window.
1. Now hit CTRL a (both together) to select all of the destination file.
1. Hit CTRL v (both together) to paste the content from your clipboard.

Do a web search to find helpful videos on anything that seems confusing
and share them in our discussion.

### Reading Error Messages

Python has pretty helpful error messages. 
When you get an error, read them carefully. 

- What error do you get?

