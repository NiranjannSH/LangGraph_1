# LangGraph_1
---

# **Cybersecurity Workflow Automation**

This project is a **LangGraph-based agentic cybersecurity pipeline** that automates security tasks such as port scanning, directory brute-forcing, and vulnerability detection. It integrates tools like `nmap`, `gobuster`, `ffuf`, and `sqlmap` to perform security audits while respecting a user-defined scope.

---

## **Features**

- **Dynamic Task Execution:**
  - Breaks down high-level security tasks into executable steps.
  - Executes tasks sequentially and handles failures automatically.

- **Scope Enforcement:**
  - Restricts scans and analyses to user-defined domains and IP ranges.

- **Real-Time Monitoring:**
  - Logs every action and provides real-time updates on task execution.

- **HTML Report Generation:**
  - Generates a clean and structured HTML report of scan results.

- **Streamlit Dashboard:**
  - Provides a user-friendly interface to define the scope, run scans, and view results.

---

## **How It Works**

1. **Define the Scope:**
   - Specify the allowed domains and IP ranges for scans.

2. **Run Scans:**
   - The workflow executes tasks like port scanning (`nmap`), directory brute-forcing (`gobuster`), web fuzzing (`ffuf`), and SQL injection testing (`sqlmap`).

3. **Analyze Results:**
   - Parses and analyzes scan results to identify vulnerabilities.

4. **Generate Reports:**
   - Creates an HTML report summarizing the findings.

5. **Visualize Results:**
   - View real-time logs, task statuses, and scan results in the Streamlit dashboard.

---

## **Setup Instructions**

### **1. Prerequisites**

- **Python 3.11**: Ensure Python 3.11 is installed on your system.
- **System Tools**: Install the following tools:
  - `nmap`
  - `gobuster`
  - `ffuf`
  - `sqlmap`


### **2. Clone the Repository**

Clone the project repository to your local machine:
```bash
git clone https://github.com/your-username/cybersecurity-workflow.git
cd cybersecurity-workflow
```

### **3. Set Up the Virtual Environment**

Create and activate a virtual environment:
```bash
python -m venv one_venv
source one_venv/bin/activate  # On Linux/macOS
one_venv\Scripts\activate     # On Windows
```

### **4. Install Dependencies**

Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## **Running the Application**

### **1. Define the Scope**

Before running scans, define the scope in the Streamlit app:
- **Allowed Domains**: Comma-separated list of domains (e.g., `google.com`).
- **Allowed IP Ranges**: Comma-separated list of IP ranges (e.g., `192.168.1.0/24`).

### **2. Start the Streamlit App**

Run the Streamlit app to launch the dashboard:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

### **3. Run Scans**

1. **Enter the Target:**
   - Provide the target domain or IP address (e.g., `google.com`).

2. **Click "Run Scan":**
   - The workflow will execute the scans and display real-time logs and results.

3. **View Results:**
   - Check the **Task List** for task statuses (✅ Completed, ❌ Failed, 🔄 Running).
   - View the **Execution Logs** for detailed output from each tool.
   - Explore the **Scan Results** and **HTML Report** for a summary of findings.

---

## **Project Structure**

```
cybersecurity-workflow/
├── app.py                  # Streamlit app for the dashboard
├── cybersecurity_workflow.py # Main workflow logic
├── tasks.py                # Task execution and tool integration
├── scope.py                # Scope validation logic
├── logging_setup.py        # Logging configuration
├── requirements.txt        # List of Python dependencies
├── scanned_reports/        # Directory for generated HTML reports
└── README.md               # Project documentation
```

---

## **Example Workflow**

1. **Define Scope:**
   - Allowed Domains: `google.com`
   - Allowed IP Ranges: `192.168.1.0/24`

2. **Run Scan:**
   - Target: `google.com`
   - The workflow will:
     - Scan open ports using `nmap`.
     - Perform directory brute-forcing using `gobuster`.
     - Fuzz web paths using `ffuf`.
     - Test for SQL injection vulnerabilities using `sqlmap`.

3. **View Results:**
   - Open ports and services are displayed in a table.
   - Vulnerabilities and scan results are summarized in the HTML report.

---

## **Contributing**

If you’d like to contribute to this project, feel free to:
- Open an issue to report bugs or suggest features.
- Submit a pull request with your improvements.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- **LangGraph**: For enabling dynamic workflow creation.
- **Streamlit**: For providing an intuitive dashboard interface.
- **Security Tools**: `nmap`, `gobuster`, `ffuf`, and `sqlmap` for their powerful scanning capabilities.

---

