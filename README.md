# **JSCEFR**
## *Studying JavaScript Code Competency in Open-Source Projects*

### What is this project about?

In this project, we intend to study JavaScript code competency in open-source projects by defining and evaluating JavaScript code competency using references from CEFR (Common European Framework of Reference, read more: https://en.wikipedia.org/wiki/Common_European_Framework_of_Reference_for_Languages) to estimate the competency of programmers in the JavaScript programming language. Then, we create a program for analyzing and reporting the detected JavaScript code competency. Lastly, we apply the program to open-source projects to understand the competency of JavaScript code in real-world software projects.

### How does it work?

There are two main directories inside this project; `jscefr_tool` and `experiment`. `jscefr_tool` directory focuses on the competency report generation based on a JavaScript project as the input, but `experiment` focuses on the competency report visualization. Hence, steps 1 to 4 comprehensively show how JSCEFR works in `jscefr_tool`, and steps 5 until the end is related to how to use `experiment`.

1. After cloning the whole repository, enter `jscefr_tool` by the command: `cd jscefr_tool`.
2. Execute the command: `python3 dictionary_converter/dict.py`. This command converts the competency table, `dict.csv`, into the competency matrix, `dict.json`.
   1. If the user wants to modify the competency level assignment into some code construct. The user needs to do it in `dict.csv` before executing the command.
3. Then, execute the command: `python3 jscefr.py directory [the path of the project directory]`. This command calls the main program to parse the input JavaScript project, match the code constructs found to their competency levels as assigned in the competency matrix, and generate the competency reports.
4. The competency reports can be accessed in `report` directory, which are shown in both CSV and JSON formats.
