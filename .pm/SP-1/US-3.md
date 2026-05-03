# US-3: Create Repository

## User Story
As a logged-in user  
So that I can manage my code  
I want to create a repository  

---

## Acceptance Criteria

### Scenario 1: Successful Creation
Given the user is logged in  
When the user provides a valid repository name  
Then the system should create a repository  
And show it in the user’s repository list  

---

### Scenario 2: Duplicate Repository Name
Given the user already has a repository with the same name  
When the user tries to create another  
Then the system should show an error  

---

### Scenario 3: Visibility Selection
Given the user creates a repository  
When the user selects visibility  
Then the system should save it as public or private  

---

## Functional Requirements
- System should allow repository creation  
- System should support public and private visibility  
- System should associate repository with the user  

---

## Non-Functional Requirements
- Repository creation should be fast and reliable  

---

## Positive Scenarios
- User creates repo → visible in list  

---

## Negative Scenarios
- Duplicate name → error  
- Unauthorized access → blocked  