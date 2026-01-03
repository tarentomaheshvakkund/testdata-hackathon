"""Shell utility with command injection vulnerability."""
import os
import subprocess

def ping_host(hostname):
    """Ping host - VULNERABLE to command injection."""
    os.system(f"ping -c 4 {hostname}")

def run_command(cmd):
    """Run command - CRITICAL VULNERABILITY."""
    return os.popen(cmd).read()
