# app.py
import streamlit as st
import pandas as pd
from cybersecurity_workflow import CybersecurityWorkflow
from scope import ScopeValidator

def main():
    st.title("Cybersecurity Workflow Visualizer")

    # Sidebar for scope configuration
    st.sidebar.header("Scope Configuration")
    domains = st.sidebar.text_input("Allowed Domains (comma-separated)", "google.com")
    ip_ranges = st.sidebar.text_input("Allowed IP Ranges (comma-separated)", "192.168.1.0/24")

    # Initialize scope validator
    scope_validator = ScopeValidator(
        domains=[domain.strip() for domain in domains.split(",")],
        ip_ranges=[ip_range.strip() for ip_range in ip_ranges.split(",")]
    )

    # Target input
    target = st.text_input("Enter Target (Domain or IP):", "google.com")

    # Run workflow
    if st.button("Run Scan"):
        workflow = CybersecurityWorkflow(scope_validator)
        result = workflow.run(target)

        # Display task list
        st.subheader("Task List")
        for task in workflow.tasks:
            status_emoji = "✅" if task["status"] == "completed" else "❌" if task["status"] == "failed" else "🔄"
            st.write(f"{status_emoji} {task['task']} ({task.get('target', '')})")

        # Display logs
        st.subheader("Execution Logs")
        st.text(workflow.task_executor.log_stream.getvalue())

        # Display results
        st.subheader("Scan Results")
        if result["status"] == "success":
            st.success("Scan completed successfully!")
            st.json(result)

            # Visualize open ports
            st.subheader("Open Ports Visualization")
            open_ports = result.get("open_ports", [])
            if open_ports:
                # Create a DataFrame for visualization
                df = pd.DataFrame(open_ports)
                st.bar_chart(df.set_index("port")["service"].value_counts())

                # Display the table of open ports
                st.write("Open Ports Table:")
                st.dataframe(df)
            else:
                st.warning("No open ports found.")

            # Display HTML report
            st.subheader("HTML Report")
            with open("scan_report.html", "r") as file:
                html_content = file.read()
            st.components.v1.html(html_content, height=500, scrolling=True)

            # Add a download button for the HTML report
            st.download_button(
                label="Download HTML Report",
                data=html_content,
                file_name="scan_report.html",
                mime="text/html"
            )
        else:
            st.error(f"Scan failed: {result['message']}")

if __name__ == "__main__":
    main()