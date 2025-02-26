# cybersecurity_workflow.py
import os
from langgraph.graph import Graph
from tasks import TaskExecutor
from scope import ScopeValidator


class CybersecurityWorkflow:
    def __init__(self, scope_validator):
        """
        Initializes the cybersecurity workflow.

        Args:
            scope_validator (ScopeValidator): Validator to enforce scope constraints.
        """
        self.task_executor = TaskExecutor(scope_validator)
        self.graph = Graph()
        self.tasks = []  # Track tasks and their statuses

    def build_workflow(self):
        """
        Builds the LangGraph-based workflow by defining nodes and edges.
        """
        # Define nodes
        self.graph.add_node("scan_ports", self.scan_ports)
        self.graph.add_node("gobuster_scan", self.gobuster_scan)
        self.graph.add_node("ffuf_scan", self.ffuf_scan)
        self.graph.add_node("sqlmap_scan", self.sqlmap_scan)
        self.graph.add_node("analyze_results", self.analyze_results)

        # Define edges
        self.graph.add_edge("scan_ports", "gobuster_scan")
        self.graph.add_edge("gobuster_scan", "ffuf_scan")
        self.graph.add_edge("ffuf_scan", "sqlmap_scan")
        self.graph.add_edge("sqlmap_scan", "analyze_results")

        # Set the entry point for the workflow
        self.graph.set_entry_point("scan_ports")

        # Set the end point for the workflow
        self.graph.set_finish_point("analyze_results")

        # Compile the graph into an executable workflow
        self.executable_workflow = self.graph.compile()

    def scan_ports(self, input_dict):
        """
        Executes an nmap scan on the target.

        Args:
            input_dict (dict): Input dictionary containing the target.

        Returns:
            dict: Scan results or error message, including the target.
        """
        # Extract the target from the input dictionary
        target = input_dict["target"]
        print(f"Scanning target: {target}")  # Debug print

        # Log the task
        self.tasks.append(
            {"task": "scan_ports", "status": "running", "target": target})

        # Execute the nmap scan
        result = self.task_executor.execute_nmap_scan(target)
        print(f"Scan result: {result}")  # Debug print

        # Update task status
        if result["status"] == "success":
            self.tasks[-1]["status"] = "completed"
        else:
            self.tasks[-1]["status"] = "failed"

        # Return the result with the target included
        return {"target": target, **result}

    def gobuster_scan(self, input_dict):
        """
        Executes a gobuster scan on the target.

        Args:
            input_dict (dict): Input dictionary containing the target.

        Returns:
            dict: Scan results or error message, including the target.
        """
        # Extract the target from the input dictionary
        target = input_dict["target"]
        print(f"Running gobuster on target: {target}")  # Debug print

        # Log the task
        self.tasks.append(
            {"task": "gobuster_scan", "status": "running", "target": target})

        # Execute the gobuster scan
        result = self.task_executor.execute_gobuster_scan(target)
        print(f"Gobuster result: {result}")  # Debug print

        # Update task status
        if result["status"] == "success":
            self.tasks[-1]["status"] = "completed"
        else:
            self.tasks[-1]["status"] = "failed"

        # Return the result with the target included
        return {"target": target, **result}

    def ffuf_scan(self, input_dict):
        """
        Executes an ffuf scan on the target.

        Args:
            input_dict (dict): Input dictionary containing the target.

        Returns:
            dict: Scan results or error message, including the target.
        """
        # Extract the target from the input dictionary
        target = input_dict["target"]
        print(f"Running ffuf on target: {target}")  # Debug print

        # Log the task
        self.tasks.append(
            {"task": "ffuf_scan", "status": "running", "target": target})

        # Execute the ffuf scan
        result = self.task_executor.execute_ffuf_scan(target)
        print(f"Ffuf result: {result}")  # Debug print

        # Update task status
        if result["status"] == "success":
            self.tasks[-1]["status"] = "completed"
        else:
            self.tasks[-1]["status"] = "failed"

        # Return the result with the target included
        return {"target": target, **result}

    def sqlmap_scan(self, input_dict):
        """
        Executes a sqlmap scan on the target.

        Args:
            input_dict (dict): Input dictionary containing the target.

        Returns:
            dict: Scan results or error message, including the target.
        """
        # Extract the target from the input dictionary
        target = input_dict["target"]
        print(f"Running sqlmap on target: {target}")  # Debug print

        # Log the task
        self.tasks.append(
            {"task": "sqlmap_scan", "status": "running", "target": target})

        # Execute the sqlmap scan
        result = self.task_executor.execute_sqlmap_scan(target)
        print(f"Sqlmap result: {result}")  # Debug print

        # Update task status
        if result["status"] == "success":
            self.tasks[-1]["status"] = "completed"
        else:
            self.tasks[-1]["status"] = "failed"

        # Return the result with the target included
        return {"target": target, **result}

    def analyze_results(self, input_dict):
        """
        Analyzes the results of the scans and returns a simplified summary.

        Args:
            input_dict (dict): Input dictionary containing the scan results and target.

        Returns:
            dict: Simplified analysis results or error message.
        """
        # Extract the target and scan result from the input dictionary
        target = input_dict["target"]
        scan_result = input_dict

        print(f"Analyzing scan result: {scan_result}")  # Debug print

        # Log the task
        self.tasks.append({"task": "analyze_results", "status": "running"})

        # Analyze the scan results
        if scan_result["status"] == "success":
            self.tasks[-1]["status"] = "completed"

            # Extract relevant information from the scan result
            scan_data = scan_result.get("result", {})
            open_ports = []

            # Extract open ports and their details
            if "scan" in scan_data:
                target_ip = list(scan_data["scan"].keys())[0]
                for port, details in scan_data["scan"][target_ip]["tcp"].items():
                    if details["state"] == "open":
                        open_ports.append({
                            "port": port,
                            "service": details["name"],
                            "state": details["state"]
                        })

            # Generate HTML report
            self.generate_html_report(target, open_ports)

            # Return a simplified summary
            return {
                "status": "success",
                "message": "Analysis complete",
                "target": target,
                "open_ports": open_ports
            }
        else:
            self.tasks[-1]["status"] = "failed"
            return {"status": "error", "message": scan_result.get("message", "Analysis failed")}

    def generate_html_report(self, target, open_ports):
        """
        Generates an HTML report for the scan results and saves it in the 'scanned_reports' directory.

        Args:
            target (str): The target domain or IP address.
            open_ports (list): List of open ports and their details.
        """
        # Create the 'scanned_reports' directory if it doesn't exist
        os.makedirs("scanned_reports", exist_ok=True)

        # HTML template
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Scan Report</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                h1 {{
                    color: #333;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                th, td {{
                    padding: 10px;
                    border: 1px solid #ddd;
                    text-align: left;
                }}
                th {{
                    background-color: #f4f4f4;
                }}
            </style>
        </head>
        <body>
            <h1>Scan Report for {target}</h1>
            <table>
                <thead>
                    <tr>
                        <th>Port</th>
                        <th>Service</th>
                        <th>State</th>
                    </tr>
                </thead>
                <tbody>
        """

        # Add rows for open ports
        for port in open_ports:
            html_content += f"""
                    <tr>
                        <td>{port['port']}</td>
                        <td>{port['service']}</td>
                        <td>{port['state']}</td>
                    </tr>
            """

        # Close HTML tags
        html_content += """
                </tbody>
            </table>
        </body>
        </html>
        """

        # Save the HTML file in the 'scanned_reports' directory
        report_filename = f"scanned_reports/scan_report_{target.replace('.', '_')}.html"
        with open(report_filename, "w") as file:
            file.write(html_content)

        print(f"HTML report generated: {report_filename}")

    def run(self, target):
        """
        Runs the cybersecurity workflow for the given target.

        Args:
            target (str): The target domain or IP address.

        Returns:
            dict: Final results of the workflow.
        """
        # Build the workflow
        self.build_workflow()

        # Execute the workflow with the target as input
        result = self.executable_workflow.invoke({"target": target})

        # Return the final result
        return result
