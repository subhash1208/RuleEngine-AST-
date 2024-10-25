<<<<<<< HEAD


# Rule Engine with AST

This project implements a rule engine application with a 3-tier architecture using Flask, SQLAlchemy, and SQLite. The rule engine allows for the creation, combination, evaluation, and modification of rules based on Abstract Syntax Trees (ASTs). A Tkinter-based frontend (UI) is also included.

## Table of Contents
1. [Installation and Setup](#setup)
2. [Project Components](#project-components)
3. [Running the Application](#app-functionalities)
4. [API Endpoints](#api-endpoints)
5. [Testing Automation](#testing-with-`test.py`)
6. [GUI Test Cases](#gui-test-cases)

---
=======
Here’s the complete README file formatted in Markdown for your rule engine application:

`\`\`markdown
>>>>>>> 4b238ee (Added Edge Case Handling)

# Rule Engine Application

<<<<<<< HEAD
### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Install the Required Dependencies
```bash
pip install flask sqlalchemy requests
```

### 3. Run the Flask Application
```bash
=======
## Overview

This project is a Rule Engine application designed to create, combine, evaluate, and modify rules based on user-defined conditions. It utilizes a Flask API for backend processing and a Tkinter GUI for user interaction. The rules are stored in a SQLite database, and the engine supports logical operations like AND, OR, and various comparison operations.

## Features

\- \*\*Create Rules:\*\* Define new rules using a structured format.

\- \*\*Combine Rules:\*\* Merge existing rules into a new rule.

\- \*\*Evaluate Rules:\*\* Assess if a rule is satisfied based on input data.

\- \*\*Modify Rules:\*\* Update existing rules with new conditions.

\- \*\*GUI Interface:\*\* User-friendly interface for interaction.

\## Project Structure

\`\`\`

rule\_engine/

│

├── main.py # Flask API for rule management

├── rlg.py # Tkinter GUI for user interaction

├── test.py # Test script for rule engine functionalities

├── requirements.txt # List of project dependencies

└── rules.db # SQLite database for storing rules

\`\`\`

\## Installation

\### Prerequisites

\- Python (version 3.6 or higher)

\- SQLite (comes bundled with Python)

\### Steps to Run the Application

1\. \*\*Clone or Download the Repository:\*\*

\`\`\`bash

git clone

cd rule\_engine

\`\`\`

2\. \*\*Create a Virtual Environment (Optional but Recommended):\*\*

\`\`\`bash

python -m venv venv

source venv/bin/activate # On Windows use \`venv\\Scripts\\activate\`

\`\`\`

3\. \*\*Install Requirements:\*\*

\`\`\`bash

pip install -r requirements.txt

\`\`\`

4\. \*\*Run the Flask API:\*\*

\- Open a terminal and navigate to the directory where \`main.py\` is located.

\`\`\`bash

>>>>>>> 4b238ee (Added Edge Case Handling)
python main.py
```
The server should display "Welcome to the Rule Engine API! Use the available endpoints to create, combine, evaluate, and modify rules."
![Evaluate Rule Example - Rule ID 24](https://drive.google.com/file/d/1dJsV7gcQGH3huby8SSJO0IbjKawZ1b2M/view?usp=sharing)

<<<<<<< HEAD
## Project Components

1. **Backend**: `main.py` (Flask and SQLAlchemy)
2. **Frontend**: `rlg.py` (Tkinter-based UI)
3. **Automated Testing Script**: `test.py` (contains edge and standard cases for API testing using `requests`)

## App Functionalities

1. **Create Rule**: Adds a new rule based on the rule string provided (e.g., `"age > 30 AND department = 'Sales'"`).
2. **Combine Rules**: Combines multiple rules into a single "Mega Rule" using comma-separated rule IDs (e.g., `13,15`).
3. **Evaluate Rule**: Evaluates a rule or a combined rule by providing the rule ID and data in JSON format.
4. **Modify Rule**: Updates an existing rule with a new rule string.

## API Endpoints

Refer to the initial documentation for detailed endpoint information on `/create_rule`, `/combine_rules`, `/evaluate_rule`, and `/modify_rule`.

## Testing with `test.py`

The `test.py` script automates testing for the rule engine application, including typical cases and specific edge cases. It tests functionalities for creating, combining, evaluating, and modifying rules. Each function in `test.py` sends requests to the corresponding API endpoints and logs the responses.

### Running the Tests
```bash
python test.py
```

### Edge Cases Included in `test.py`

1. **Invalid Rule String**: Checks for syntax errors in rule strings.
2. **Empty Rule String**: Tests rule creation with an empty string to verify graceful handling.
3. **Missing Data Fields in Evaluation**: Evaluates a rule with missing data fields to test error handling.
4. **Nonexistent Rule IDs**: Attempts to combine or modify rules with IDs that don’t exist.
5. **Conflicting Data Types**: Evaluates rules with incorrect data types (e.g., strings instead of integers).
6. **Empty Rule List for Combining**: Tests combining with an empty list of rule IDs.
7. **Duplicate Rule IDs in Combine**: Tests combining with duplicate rule IDs in the list.
8. **Nonexistent Rule ID in Modify**: Attempts to modify a rule with a nonexistent ID.
9. **Empty Modify Rule String**: Tests modifying a rule with an empty string.
![Evaluate Rule Example - Rule ID 24](https://drive.google.com/file/d/1OCBQKn2D12l1mk9-eulgW8o7T_Xk7Rhx/view?usp=sharing)


## GUI Test Cases 

### 1. Create Rule Functionality
- **Input**: 
  - Rule Definition for ID 21: `(age >= 30 AND income < 50000) OR (experience >= 5)`
- **Expected Output**:
  ```json
  {
    "ast": "{\"type\": \"operator\", \"value\": \"OR\", \"left\": {\"type\": \"operator\", \"value\": \"AND\", \"left\": {\"type\": \"operand\", \"value\": \"age >= 30\", \"left\": null, \"right\": null}, \"right\": {\"type\": \"operand\", \"value\": \"income < 50000\", \"left\": null, \"right\": null}}, \"right\": {\"type\": \"operand\", \"value\": \"experience >= 5\", \"left\": null, \"right\": null}}",
    "id": 21
  }
  ```
- **Screenshot**:
  ![Create Rule Example - Rule ID 21](https://drive.google.com/file/d/1itDLICCYQidY1wirbHh2SKZxKUGpL8nw/view?usp=sharing)

### 2. Create Rule Functionality
- **Input**:
  - Rule Definition for ID 22: `(department IN ('Finance', 'HR') AND salary >= 60000) OR (performance_rating = 5)`
- **Expected Output**:
  ```json
  {
    "ast": "{\"type\": \"operator\", \"value\": \"OR\", \"left\": {\"type\": \"operator\", \"value\": \"AND\", \"left\": {\"type\": \"operand\", \"value\": \"department IN ('Finance', 'HR')\", \"left\": null, \"right\": null}, \"right\": {\"type\": \"operand\", \"value\": \"salary >= 60000\", \"left\": null, \"right\": null}}, \"right\": {\"type\": \"operand\", \"value\": \"performance_rating = 5\", \"left\": null, \"right\": null}}",
    "id": 22
  }
  ```
- **Screenshot**:
  ![Create Rule Example - Rule ID 22](https://drive.google.com/file/d/1_3xjG5P_EYvfXp9wmpJYT9u6vQ3HoXwS/view?usp=sharing)

### 3. Create Rule Functionality
- **Input**:
  - Rule Definition for ID 23: `(location = 'Onsite' AND spend < 2000) OR (location = 'Remote' AND spend > 1000)`
- **Expected Output**:
  ```json
  {
    "ast": "{\"type\": \"operator\", \"value\": \"OR\", \"left\": {\"type\": \"operator\", \"value\": \"AND\", \"left\": {\"type\": \"operand\", \"value\": \"location = 'Onsite'\", \"left\": null, \"right\": null}, \"right\": {\"type\": \"operand\", \"value\": \"spend < 2000\", \"left\": null, \"right\": null}}, \"right\": {\"type\": \"operator\", \"value\": \"AND\", \"left\": {\"type\": \"operand\", \"value\": \"location = 'Remote'\", \"left\": null, \"right\": null}, \"right\": {\"type\": \"operand\", \"value\": \"spend > 1000\", \"left\": null, \"right\": null}}}",
    "id": 23
  }
  ```
- **Screenshot**:
  ![Create Rule Example - Rule ID 23](https://drive.google.com/file/d/1snuq_idTrXRutAJuwGg4AmfUwoIz1jqj/view?usp=sharing)

### 4. Combine Rules Functionality
- **Input**: Combining Rule IDs 21 and 23 into Rule ID 24
- **Expected Output**:
  ```json
  {
    "combined_ast": "{\"type\": \"operator\", \"value\": \"AND\", \"left\": {\"type\": \"operator\", \"value\": \"OR\", \"left\": {\"type\": \"operator\", \"value\": \"AND\", \"left\": {\"type\": \"operand\", \"value\": \"age >= 30\", \"left\": null, \"right\": null}, \"right\": {\"type\": \"operand\", \"value\": \"income < 50000\", \"left\": null, \"right\": null}}, \"right\": {\"type\": \"operand\", \"value\": \"experience >= 5\", \"left\": null, \"right\": null}}, \"right\": {\"type\": \"operator\", \"value\": \"OR\", \"left\": {\"type\": \"operator\", \"value\": \"AND\", \"left\": {\"type\": \"operand\", \"value\": \"location = 'Onsite'\", \"left\": null, \"right\": null}, \"right\": {\"type\": \"operand\", \"value\": \"spend < 2000\", \"left\": null, \"right\": null}}, \"right\": {\"type\": \"operator\", \"value\": \"AND\", \"left\": {\"type\": \"operand\", \"value\": \"location = 'Remote'\", \"left\": null, \"right\": null}, \"right\": {\"type\": \"operand\", \"value\": \"spend > 1000\", \"left\": null, \"right\": null}}}}",
    "id": 24
  }
  ```
- **Screenshot**:
  ![Combine Rule Example - Rule ID 24](https://drive.google.com/file/d/1Woe7DND9GG2Vb8qCMMONDfpIG0TlWRDL/view?usp=sharing)

### 5. Evaluate Rule Functionality
- **Input**:
  - Evaluating Rule ID 24 with the following data:
    ```json
    {
      "age": 35,
      "income": 40000,
      "experience": 5,
      "department": "Finance",
      "salary": 70000,
      "location": "Onsite",
      "spend": 1800,
      "performance_rating": 5
    }
    ```
- **Expected Output**:
  ```json
  { "result": true }
  ```
- **Screenshot**:
  ![Evaluate Rule Example - Rule ID 24](https://drive.google.com/file/d/1dJsV7gcQGH3huby8SSJO0IbjKawZ1b2M/view?usp=sharing)

### 6. Modify Rule Functionality
- **Input**:
  - Modifying Rule ID 22 with new definition:
    ```json
    { "new_string": "department IN ('Finance', 'HR') AND salary > 70000 OR performance_rating = 5" }
    ```
- **Expected Output**:
  ```json
  { "message": "Rule updated successfully" }
  ```
- **Screenshot**:
  ![Modify Rule Example - Rule ID 22](https://drive.google.com/file/d/1dJsV7gcQGH3huby8SSJO0IbjKawZ1b2M/view?usp=sharing)

=======
\`\`\`

\- The server will start on \`http://127.0.0.1:5000\`.

5\. \*\*Run the GUI Application:\*\*

\- In a separate terminal window, run:

\`\`\`bash

python rlg.py

\`\`\`

\- This will launch the Tkinter GUI for the rule engine.

\## API Endpoints

\### 1. Create Rule

\- \*\*Endpoint:\*\* \`/create\_rule\`

\- \*\*Method:\*\* POST

\- \*\*Payload:\*\*

\`\`\`json

{

"rule\_string": "(age > 30 AND department = 'Sales')"

}

\`\`\`

\- \*\*Response:\*\*

\`\`\`json

{

"id": 1,

"ast": "{\\"type\\":\\"operator\\",\\"value\\":\\"AND\\", ...}"

}

\`\`\`

\### 2. Combine Rules

\- \*\*Endpoint:\*\* \`/combine\_rules\`

\- \*\*Method:\*\* POST

\- \*\*Payload:\*\*

\`\`\`json

{

"rule\_ids": \[1, 2\]

}

\`\`\`

\- \*\*Response:\*\*

\`\`\`json

{

"id": 3,

"combined\_ast": "{\\"type\\":\\"operator\\",\\"value\\":\\"AND\\", ...}"

}

\`\`\`

\### 3. Evaluate Rule

\- \*\*Endpoint:\*\* \`/evaluate\_rule\`

\- \*\*Method:\*\* POST

\- \*\*Payload:\*\*

\`\`\`json

{

"rule\_id": 3,

"data": {

"age": 35,

"department": "Sales",

"salary": 60000,

"experience": 6

}

}

\`\`\`

\- \*\*Response:\*\*

\`\`\`json

{

"result": true

}

\`\`\`

\### 4. Modify Rule

\- \*\*Endpoint:\*\* \`/modify\_rule\`

\- \*\*Method:\*\* POST

\- \*\*Payload:\*\*

\`\`\`json

{

"rule\_id": 1,

"new\_rule\_string": "(age > 40 AND department = 'HR')"

}

\`\`\`

\- \*\*Response:\*\*

\`\`\`json

{

"message": "Rule updated successfully"

}

\`\`\`

\## Test Cases

The \`test.py\` file includes various test cases for each of the functionalities in the rule engine, which can be executed to verify the application behavior.

\## Requirements

To run this application, you will need the following Python packages:

\`\`\`

Flask==2.0.1

Flask-SQLAlchemy==2.5.1

requests==2.26.0

tkinter

\`\`\`

\## License

This project is licensed under the MIT License. See the LICENSE file for more information.

\## Acknowledgments

\- Inspired by various rule engine implementations.

\- Thanks to the Flask and Tkinter communities for their excellent resources.

\`\`\`

You can copy this entire text into a file named \`README.md\` in your project directory. Let me know if you need any more modifications!
>>>>>>> 4b238ee (Added Edge Case Handling)
