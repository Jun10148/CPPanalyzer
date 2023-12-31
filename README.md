# CPPAnalyzer
Automatic detection of code refactoring patterns in C++ files.

## Supervisor
* Dr Cruz Izu
  * Lecturer
  * School of Computer and Mathematical Sciences, Faculty of Sciences, Engineering and Technology
  * Research Interests: Computer System Architecture, Higher Education, Networking and Communications, Teacher Education and Professional Development of Educators

## Student Researchers
* Jose De Los Santos
* Seojun Lee
* Faisal Umar

## Context
This project extends and completes a previous incomplete version of the 'CPPAnalyzer' tool supervised by Dr Cruz Izu and students Jiajun Yu and Jian Zhe Chan.

## Summary
CPPAnalyzer is a python-based code quality checking tool for the C++ language that aims to detect novice level refactoring patterns which are missed by current existing tools. It is developed with the intention of being integrated in a student submission system as students typically focus on program correctness instead of code quality. However, the tool can be run standalone.

## Detected Patterns
The implemented patterns are currently:
* Pattern 1: Simplify Boolean Expression
* Pattern 2: Simplify Boolean Return
* Pattern 3: Collapsible Nested IF Statement
* Pattern 4: Consolidate Conditional Expressions
* Pattern 5: Redundant Conditional Check
* Pattern 6: No Use of ELSE
* Pattern 7: Duplicate IF-ELSE Body
* Pattern 8: Empty IF Statement
* Pattern 9: Dead Code

## Running CPPAnalyzer
To run CPPAnalyzer, call ASTProcessor.py followed by the path to the target file to analyse.

For example:

> python ASTProcessor.py test.cpp

or

> python3 ASTProcessor.py test.cpp

## CPPAnalyzer Workflow
CPPAnalyzer uses the Abstract Syntax Tree generated by the Clang compiler to analyse the structure of a single C++ file. First, target nodes are collected. These are nodes that follow a specific structure relevant to the individual patterns listed above (e.g., being an IF statement). Afterwards, separate detectors for the patterns analyse the respective target node and determine whether the node violates the pattern. If so, a statement is printed giving a warning to the corresponding line and column within the C++ file. 

<img src="CPPAnalyzer Structure.png" width=1000px>

## Building on CPPAnalyzer
Future work includes:
* Adding more patterns
* Creating a user-friendly CLI/GUI
* Allowing input for multi-file projects

<br>
<br>

*README by Jose De Los Santos*