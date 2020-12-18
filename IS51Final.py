"""
The program is designed to calculate an average of student grades on a final exam based off of a text file.
This average will not only determine the percentage of grades above the average grade, but also will show the user
the total number of grades and the average grade on the exam.

To create the program, a main() function will be used to initialize the application or,
in other words, start up the program.

Next, a calculate_percent_above_average function will also be used to calculate
the percentage of grades that are above the average grade.

In this function, all the grades in the text file will be read using the open() method. It will then immediately close the file
and the grades will be assigned to a list of integers. The program will use this list to execute addition and division operations in order
to determine the average grade on the exam.

After the program runs, the information that will be printed to the user include the number of grades,
the average grade, and the percentage of grades that are above the average grade.
"""