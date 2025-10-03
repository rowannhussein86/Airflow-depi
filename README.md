# Airflow_Depi DAG Task

This project demonstrates a simple Apache Airflow DAG with 3 tasks.

---

## 🛠 DAG Overview
- **DAG Name:** `Airflow_Depi`
- **Tasks:**
  1. **Print current date** – using `BashOperator`
  2. **Print welcome message** – using `PythonOperator`
  3. **Generate a random number and save it** – using `PythonOperator`, saves to `/tmp/random.txt`

- **Task Order:**  
```
Task 1 → Task 2 → Task 3
```


---

## 🚀 How to Run
1. Start Airflow environment (Docker or local setup)
2. Load DAG in Airflow UI (`http://localhost:8080`)
3. Trigger the DAG manually or schedule as needed
4. Ensure all tasks succeed (check logs in Airflow UI)

---
## 📸 Screenshots
- DAG Graph View  
  ![DAG Graph View](/images/screenshot1.png)
- Task Logs  
  ![Task Logs](/images/screenshot2.png)

## 📝 Notes
- Task 1: Prints the current system date in Bash  
- Task 2: Prints a welcome message, e.g., `"Welcome! My name is Rowan Hussein"`  
- Task 3: Generates a random number and writes it to `/tmp/random.txt`  
- Logs are stored in `logs/` (ignored in Git with `.gitignore`)
