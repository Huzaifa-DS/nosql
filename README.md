# NoSQL Project: Movie Recommendation System

This repository demonstrates the integration of three NoSQL database types: **Neo4j**, **Redis**, and **MongoDB**, to build a recommendation system.

---

## **Project Overview**

The system provides personalized movie recommendations for users based on their interests and logs user interactions for analysis. It uses:
- **Neo4j** for relationship-based queries,
- **Redis** for caching recommendations, and
- **MongoDB** for storing user interaction logs.

---

## **Folder Structure**

- **notebooks/**  
  Contains Jupyter notebooks used for development and testing.

- **scripts/**  
  Includes Python scripts for interacting with the databases.

---

## **Database Usage**

### **1. Neo4j (Graph Database)**
- **Purpose:** Handles complex relationship queries to generate movie recommendations.
- **Usage:** Stores the user-movie relationship graph and processes queries to suggest movies.

### **2. Redis (Key-Value Database)**
- **Purpose:** Caches recommendations for fast retrieval.
- **Usage:** Stores movie recommendations for quick access to reduce Neo4j query overhead.

### **3. MongoDB (Document Database)**
- **Purpose:** Logs user activities to track interactions.
- **Usage:** Stores structured logs for auditing and future analysis of user behavior.

---

## **Getting Started**

### Prerequisites
- Install **Python 3.9+** and the required libraries listed in `requirements.txt`.
- Set up **Neo4j**, **Redis**, and **MongoDB** servers.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/nosql-project.git
   cd nosql-project
