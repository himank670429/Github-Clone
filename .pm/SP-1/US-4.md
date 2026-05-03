# US-4: List Repositories

## User Story
As a logged-in user  
So that I can manage my projects  
I want to view a list of my repositories  

---

## Acceptance Criteria

### Scenario 1: View Repository List
Given the user is logged in  
When the user navigates to repositories  
Then the system should show all repositories owned by the user  

---

### Scenario 2: Repository Details
Given repositories are displayed  
Then each repository should show:
- name  
- visibility  
- creation date  

---

### Scenario 3: No Repositories
Given the user has no repositories  
When the user views the list  
Then the system should show an empty state  

---

## Functional Requirements
- System should fetch and display user repositories  
- System should show basic repository details  

---

## Non-Functional Requirements
- List should load quickly  
- UI should be clean and readable  

---

## Positive Scenarios
- User sees all repositories correctly  

---

## Negative Scenarios
- Unauthorized access → blocked  