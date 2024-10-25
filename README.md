This project implements a rule engine application with a 3-tier architecture using Flask, SQLAlchemy, and SQLite. The rule engine allows for the creation, combination, evaluation, and modification of rules based on Abstract Syntax Trees (ASTs). A Tkinter-based frontend (UI) is also included.

## Table of Contents
1. [Installation and Setup](#setup)
2. [Project Components](#project-components)
3. [Running the Application](#app-functionalities)
4. [API Endpoints](#api-endpoints)
5. [GUI Test Cases](#gui-test-cases)
---
## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/subhash1208/RuleEngine-with-AST.git
cd <repository_folder>
```

### 2. Install the Required Dependencies
```bash
pip install flask sqlalchemy requests
```

### 3. Run the Flask Application
```bash
python main.py
```
The server should display "Welcome to the Rule Engine API! Use the available endpoints to create, combine, evaluate, and modify rules."
<img src="https://github.com/subhash1208/RuleEngine-with-AST/blob/613df348a6ea1c075ec31e24030b71aeeeb6680e/screenshots/Screenshot%20(158).jpg" width="850">


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
<img src="https://github.com/subhash1208/RuleEngine-with-AST/blob/613df348a6ea1c075ec31e24030b71aeeeb6680e/screenshots/Screenshot%20(145).png" width="850">


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
  <img src="https://github.com/subhash1208/RuleEngine-with-AST/blob/613df348a6ea1c075ec31e24030b71aeeeb6680e/screenshots/Screenshot%20(154).png" width="850">

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
  <img src="https://github.com/subhash1208/RuleEngine-with-AST/blob/613df348a6ea1c075ec31e24030b71aeeeb6680e/screenshots/Screenshot%20(155).png" width="850">

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
  <img src="https://github.com/subhash1208/RuleEngine-with-AST/blob/613df348a6ea1c075ec31e24030b71aeeeb6680e/screenshots/Screenshot%20(156).png" width="850">

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
  <img src="https://github.com/subhash1208/RuleEngine-with-AST/blob/613df348a6ea1c075ec31e24030b71aeeeb6680e/screenshots/Screenshot%20(157).png" width="850">

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
  <img src="https://github.com/subhash1208/RuleEngine-with-AST/blob/613df348a6ea1c075ec31e24030b71aeeeb6680e/screenshots/Screenshot%20(159).png" width="850">
  

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
  <img src="https://github.com/subhash1208/RuleEngine-with-AST/blob/613df348a6ea1c075ec31e24030b71aeeeb6680e/screenshots/Screenshot%20(159).png" width="850">
