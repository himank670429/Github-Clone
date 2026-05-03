# 📘 Project Context - GitHub Clone

## 📌 Overview

This project is a simplified clone of a platform like GitHub, built to understand how a Git-based repository hosting system works internally.

The goal is not to copy every feature, but to build a working system that supports the core developer workflow:
- storing code
- tracking changes
- viewing history
- basic collaboration

---

## 🎯 Purpose

The purpose of this project is to:

- Understand how Git repositories are stored and served from a backend
- Learn how to integrate Git with a web application
- Practice real-world system design
- Build a strong foundation for advanced features like pull requests and CI/CD

---

## 🧱 Core Concept

The system is based on two main responsibilities:

### 1. Git handles code
- All repositories are stored as Git repositories
- Git manages:
  - commits
  - branches
  - history
- Code is NOT stored in the database

---

### 2. Backend handles logic
- Authentication
- Repository metadata
- Access control (later)
- API layer for frontend

---

## ⚙️ System Architecture

### Backend (FastAPI)
- Handles APIs and business logic
- Executes Git commands internally
- Manages authentication and repositories

---

### Database (PostgreSQL)
Stores only metadata:

- Users
- Repositories
- (Future: permissions, pull requests, issues)

⚠️ Important: Code is NOT stored in database

---

### Git Storage
- Repositories are stored as **bare Git repositories**
- Example structure:
    
    ```
    /repos/
    └── {user}/
    └── {repo}.git
    ```

---

### Frontend (React + Tailwind)
- Handles user interface
- Features:
  - Signup/Login
  - Repo listing
  - File explorer
  - File viewer
  - Commit history

---

## 🔑 Core Features (Sprint 1)

### Authentication
- User signup (email + password)
- User login

---

### Repository Management
- Create repository
- Public / Private visibility
- List user repositories

---

### Git Operations
- Push code using Git CLI
- Clone repository
- Proper Git repo initialization

---

### Repository Viewer (UI)
- Browse files and folders
- View file content (latest version)
- View commit history:
  - message
  - author
  - timestamp

---

## 🧠 Key Design Decisions

- Use Git for all code storage and versioning
- Use database only for metadata
- Keep architecture simple in early stages
- Avoid premature optimization

---

## 🚫 Out of Scope (Initial Version)

- Pull Requests
- Issues
- Notifications
- CI/CD (Actions)
- Advanced RBAC

---

## ✅ Definition of Success (Sprint 1)

A user should be able to:

1. Sign up and log in  
2. Create a repository  
3. Push code using Git  
4. Clone the repository  
5. View files in UI  
6. View commit history  

---

## 🚀 Future Scope

- Pull Requests (code review system)
- Role-based access control (owner, contributor, read-only)
- Issues tracking system
- Activity feed
- CI/CD pipelines (Actions)
- Insights and analytics

---

## 📌 Notes

- Do not store code in database
- Always rely on Git for repository operations
- Focus on building a working system first
- Add complexity only when required