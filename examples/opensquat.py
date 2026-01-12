#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: Using openSquat as a library.

This example demonstrates how to use openSquat programmatically
instead of using the CLI.
"""
from opensquat.app import Domain
from opensquat.phishing import Phishing
from opensquat.vt import VirusTotal
from opensquat.port_check import PortCheck
from opensquat.output import SaveFile


def example_domain_detection():
    """Example: Detect domain squatting."""
    print("Example 1: Domain Detection")
    print("-" * 40)
    
    # Initialize the Domain class
    domain_checker = Domain()
    
    # Check for squatting domains
    # Parameters: keywords_file, confidence_level, domains_file, method, dns, doppelganger_only
    # Note: keywords_file and domains_file should be file paths
    # For this example, we'll use the example files if they exist
    import os
    keywords_file = "examples/keywords.txt" if os.path.exists("examples/keywords.txt") else "keywords.txt"
    confidence_level = 1  # 0-4: 0=very high, 1=high, 2=medium, 3=low, 4=very low
    domains_file = ""  # Empty string uses default domain list from opensquat feeds
    method = "Levenshtein"  # Options: "Levenshtein" or "JaroWinkler"
    dns = False  # Check if domain is flagged by Quad9 DNS
    doppelganger_only = False  # Only check for doppelganger domains
    
    try:
        results = domain_checker.main(
            keywords_file,
            confidence_level,
            domains_file,
            method,
            dns,
            doppelganger_only
        )
        
        print(f"Found {len(results)} potential squatting domains")
        for domain in results[:5]:  # Show first 5
            print(f"  - {domain}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Note: Make sure keywords.txt file exists or provide a valid path")
    print()


def example_phishing_detection():
    """Example: Detect phishing sites."""
    print("Example 2: Phishing Detection")
    print("-" * 40)
    
    phishing_checker = Phishing()
    keywords = "paypal"
    
    phishing_results = phishing_checker.main(keywords)
    
    print(f"Found {len(phishing_results)} active phishing sites")
    for site in phishing_results[:5]:  # Show first 5
        print(f"  - {site}")
    print()


def example_virustotal_check():
    """Example: Check domains with VirusTotal."""
    print("Example 3: VirusTotal Check")
    print("-" * 40)
    
    vt_checker = VirusTotal()
    domain = "example-suspicious.com"
    
    # Check if domain is flagged as malicious
    votes = vt_checker.main(domain)
    malicious = votes[1]  # Only use malicious votes
    
    if malicious > 0:
        print(f"⚠️  {domain} flagged as malicious ({malicious} votes)")
    else:
        print(f"✓ {domain} appears safe")
    print()


def example_port_check():
    """Example: Check if domain has open webserver ports."""
    print("Example 4: Port Check")
    print("-" * 40)
    
    port_checker = PortCheck()
    domain = "example.com"
    
    open_ports = port_checker.main(domain)
    
    if open_ports:
        print(f"✓ {domain} has open ports: {open_ports}")
    else:
        print(f"✗ {domain} has no open webserver ports")
    print()


def example_save_results():
    """Example: Save results to file."""
    print("Example 5: Save Results")
    print("-" * 40)
    
    saver = SaveFile()
    results = ["example1.com", "example2.com", "example3.com"]
    filename = "results.json"
    file_type = "json"
    
    saver.main(filename, file_type, results)
    print(f"✓ Results saved to {filename}")
    print()


if __name__ == "__main__":
    print("=" * 50)
    print("openSquat Library Usage Examples")
    print("=" * 50)
    print()
    
    # Run examples
    try:
        example_domain_detection()
        example_phishing_detection()
        example_virustotal_check()
        example_port_check()
        example_save_results()
    except Exception as e:
        print(f"Error running examples: {e}")
        print("Note: Some examples may require API keys or network access")
    
    print("=" * 50)
    print("For CLI usage, run: opensquat -h")
    print("=" * 50)
