# Documentation for Rule 3 Detector

# We collect all if statement nodes in our program
# For each if statement, there are two conditions
# 1) Condition 1: One line if statement
#   1.1) The number of inner nodes must be two (One inner node is binary operator, another one is if statement node)
#   1.2) The last inner node is an if statement node
# 2) Condition 2: If statement that is surrounded by curly brackets
#   2.1) The number of inner nodes must be two (One inner node is binary operator, another one is if statement node)
#   2.2) The last inner node is a compound statement node and it must contain only one inner node which is an if statement node 



# Load json data
import json

def Rule3Detector(filename, temp_dict, path):
    f = open("temp/"+path+"ifNodes.json")
    jsonData = json.load(f)

    for ele in jsonData:
        # Check the number of inner nodes must be two (One is binary operator)
        if len(ele["inner"]) != 2:
            continue
        # Get the last child of the if statement
        lastChildOfIfStmt = ele["inner"][len(ele["inner"]) - 1]
        if lastChildOfIfStmt.get("inner") == None:
            continue
        # Condition 1: One line if statement
        if lastChildOfIfStmt["kind"] == "IfStmt":
            printer(ele, filename, temp_dict)
        # Condition 2: If statement that is surrounded by curly brackets
        elif lastChildOfIfStmt["kind"] == "CompoundStmt" and len(lastChildOfIfStmt["inner"]) == 1 and lastChildOfIfStmt["inner"][0]["kind"] == "IfStmt":
            printer(ele, filename, temp_dict)


def printer(json, filename, temp_dict):
    temp_dict[3] += 1
    print("{filename}:{row}:{col}: Rule3 Violated: Avoiding deep nested IFs by using and (&&) operator.".format(filename = filename, row = json["range"]["begin"]["line"] - 1, col = json["range"]["begin"]["col"]))