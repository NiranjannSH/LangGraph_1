# scope.py
import re

class ScopeValidator:
    def __init__(self, domains=None, ip_ranges=None):
        self.domains = domains or []
        self.ip_ranges = ip_ranges or []

    def is_in_scope(self, target):
        print(f"Checking if {target} is in scope")  # Debug print

        # Check if target is a domain
        for domain in self.domains:
            pattern = domain.replace(".", r"\.").replace("*", r".*")
            if re.match(pattern, target):
                print(f"Target {target} matches domain pattern {pattern}")  # Debug print
                return True

        # Check if target is an IP within the specified ranges
        for ip_range in self.ip_ranges:
            if target.startswith(ip_range.split('/')[0]):
                print(f"Target {target} matches IP range {ip_range}")  # Debug print
                return True

        print(f"Target {target} is out of scope")  # Debug print
        return False