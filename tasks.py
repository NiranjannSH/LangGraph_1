# tasks.py
import subprocess
#import python_nmap as nmap  
# Use underscore instead of hyphen
import nmap
from scope import ScopeValidator
from logging_setup import setup_logging

class TaskExecutor:
    def __init__(self, scope_validator):
        """Initialize the TaskExecutor with a scope validator."""
        self.scope_validator = scope_validator
        self.logger, self.log_stream = setup_logging()

    def execute_nmap_scan(self, target):
        """Execute an nmap scan."""
        if not self.scope_validator.is_in_scope(target):
            self.logger.error(f"Target {target} is out of scope")
            return {"status": "error", "message": "Target out of scope"}
        try:
            nm = nmap.PortScanner()
            scan_result = nm.scan(target, arguments="-p 80,443")
            self.logger.info(f"Scan completed for {target}")
            return {"status": "success", "result": scan_result}
        except Exception as e:
            self.logger.error(f"Scan failed: {e}")
            return {"status": "error", "message": str(e)}

    def execute_gobuster_scan(self, target):
        """Execute a gobuster scan."""
        if not self.scope_validator.is_in_scope(target):
            self.logger.error(f"Target {target} is out of scope")
            return {"status": "error", "message": "Target out of scope"}
        try:
            result = subprocess.run(
                ["gobuster", "dir", "-u", f"http://{target}", "-w", "wordlist.txt"],
                capture_output=True, text=True
            )
            self.logger.info(f"Gobuster scan completed for {target}")
            return {"status": "success", "result": result.stdout}
        except Exception as e:
            self.logger.error(f"Gobuster scan failed: {e}")
            return {"status": "error", "message": str(e)}

    def execute_ffuf_scan(self, target):
        """Execute an ffuf scan."""
        if not self.scope_validator.is_in_scope(target):
            self.logger.error(f"Target {target} is out of scope")
            return {"status": "error", "message": "Target out of scope"}
        try:
            result = subprocess.run(
                ["ffuf", "-u", f"http://{target}/FUZZ", "-w", "wordlist.txt"],
                capture_output=True, text=True
            )
            self.logger.info(f"Ffuf scan completed for {target}")
            return {"status": "success", "result": result.stdout}
        except Exception as e:
            self.logger.error(f"Ffuf scan failed: {e}")
            return {"status": "error", "message": str(e)}

    def execute_sqlmap_scan(self, target):
        """Execute a sqlmap scan."""
        if not self.scope_validator.is_in_scope(target):
            self.logger.error(f"Target {target} is out of scope")
            return {"status": "error", "message": "Target out of scope"}
        try:
            result = subprocess.run(
                ["sqlmap", "-u", f"http://{target}", "--batch"],
                capture_output=True, text=True
            )
            self.logger.info(f"Sqlmap scan completed for {target}")
            return {"status": "success", "result": result.stdout}
        except Exception as e:
            self.logger.error(f"Sqlmap scan failed: {e}")
            return {"status": "error", "message": str(e)}