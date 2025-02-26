# main.py
from cybersecurity_workflow import CybersecurityWorkflow
from scope import ScopeValidator

def main():
    # Define the scope
    scope_validator = ScopeValidator(domains=["google.com"], ip_ranges=["192.168.1.0/24"])

    # Initialize the workflow
    workflow = CybersecurityWorkflow(scope_validator)

    # Run the workflow
    target = "google.com"
    result = workflow.run(target)
    print(result)

if __name__ == "__main__":
    main()