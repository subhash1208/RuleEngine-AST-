import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_create_rule(rule_string):
    print("\nTesting create_rule...")
    url = f"{BASE_URL}/create_rule"
    data = {"rule_string": rule_string}
    response = requests.post(url, json=data)
    print(f"Response: {response.json()}")
    return response.json().get('id', None)

def test_combine_rules(rule_ids):
    print("\nTesting combine_rules...")
    url = f"{BASE_URL}/combine_rules"
    data = {"rule_ids": rule_ids}
    response = requests.post(url, json=data)
    print(f"Response: {response.json()}")
    return response.json().get('id', None)

def test_evaluate_rule(rule_id, data):
    print("\nTesting evaluate_rule...")
    url = f"{BASE_URL}/evaluate_rule"
    data = {"rule_id": rule_id, "data": data}
    response = requests.post(url, json=data)
    print(f"Response: {response.json()}")

def test_modify_rule(rule_id, new_rule_string):
    print("\nTesting modify_rule...")
    url = f"{BASE_URL}/modify_rule"
    data = {"rule_id": rule_id, "new_rule_string": new_rule_string}
    response = requests.post(url, json=data)
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    # Edge Case 1: Invalid Rule String
    print("Edge Case: Invalid Rule String")
    test_create_rule("(age > 30 AND department 'Sales')")  # Missing operator after department

    # Edge Case 2: Empty Rule String
    print("Edge Case: Empty Rule String")
    test_create_rule("")  # Should handle or reject empty rule

    # Edge Case 3: Missing Data Fields in Evaluation
    print("Edge Case: Missing Data Fields in Evaluation")
    rule_id = test_create_rule("(age > 25 AND salary > 30000)")
    test_evaluate_rule(rule_id, {"age": 28})  # Missing 'salary'

    # Edge Case 4: Nonexistent Rule IDs in Combine
    print("Edge Case: Nonexistent Rule IDs in Combine")
    test_combine_rules([999, 1000])  # Rule IDs that do not exist

    # Edge Case 5: Conflicting Data Types
    print("Edge Case: Conflicting Data Types in Evaluation")
    rule_id = test_create_rule("(age > 25 AND salary > 30000)")
    test_evaluate_rule(rule_id, {"age": "thirty", "salary": 30000})  # Age should be an integer

    # Edge Case 6: Empty Rule List for Combining
    print("Edge Case: Empty Rule List for Combining")
    test_combine_rules([])  # Should handle empty list gracefully

    # Edge Case 7: Duplicate Rule IDs for Combining
    print("Edge Case: Duplicate Rule IDs for Combining")
    rule_id1 = test_create_rule("(age > 20)")
    rule_id2 = test_create_rule("(salary > 30000)")
    test_combine_rules([rule_id1, rule_id1, rule_id2])  # Duplicate rule ID

    # Edge Case 8: Nonexistent Rule ID in Modify
    print("Edge Case: Nonexistent Rule ID in Modify")
    test_modify_rule(9999, "age > 40")  # Modify rule with a nonexistent ID

    # Edge Case 9: Empty Modify Rule String
    print("Edge Case: Empty Modify Rule String")
    test_modify_rule(rule_id1, "")  # Empty new rule string

    print("Edge Case Testing Completed.")
