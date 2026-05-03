# US-2: User Login

## User Story
As a registered user  
So that I can access my account  
I want to log in using my credentials  

---

## Acceptance Criteria

### Scenario 1: Successful Login
Given the user is registered  
When the user enters valid credentials  
Then the system should authenticate the user  
And grant access  

---

### Scenario 2: Invalid Credentials
Given the user enters incorrect email or password  
When the user submits login  
Then the system should show an error  

---

## Functional Requirements
- System should authenticate users using email and password  
- System should allow access only after successful login  

---

## Non-Functional Requirements
- Authentication should be secure  
- Response time should be fast  

---

## Positive Scenarios
- Valid login → access granted  

---

## Negative Scenarios
- Invalid credentials → access denied  