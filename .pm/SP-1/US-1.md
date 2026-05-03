# US-1: User Signup

## User Story
As a new user  
So that I can access the platform  
I want to create an account using my email and password  

---

## Acceptance Criteria

### Scenario 1: Successful Signup
Given the user is on the signup page  
When the user enters a valid email and password  
Then the system should create a new account  
And show a success message  

---

### Scenario 2: Duplicate Email
Given a user tries to sign up with an existing email  
When the user submits the form  
Then the system should show an error  
And prevent account creation  

---

### Scenario 3: Invalid Input
Given the user enters invalid or empty fields  
When the user submits the form  
Then the system should show validation errors  

---

## Functional Requirements
- System should allow users to register using email and password  
- System should ensure email uniqueness  
- System should securely store user credentials  

---

## Non-Functional Requirements
- Passwords must be securely stored (encrypted/hashed)  
- System should respond within acceptable time  

---

## Positive Scenarios
- User signs up with valid details → account created  

---

## Negative Scenarios
- Duplicate email → error shown  
- Invalid input → validation error  