#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openSquat CLI.

Command-line interface for openSquat library.

* https://github.com/atenreiro/opensquat

software licensed under GNU version 3
"""
import time
import signal
import functools
import concurrent.futures

from colorama import init, Fore, Style
from opensquat import __VERSION__
from opensquat import arg_parser, output, app, phishing, check_update
from opensquat import port_check, vt


def signal_handler(sig, frame):
    """Function to catch CTR+C and terminate."""
    print("\n[*] openSquat is terminating...\n")
    exit(0)


def print_logo():
    """Print the openSquat logo."""
    logo = (
        Style.BRIGHT + Fore.GREEN +
        """
                                             █████████                                  █████
                                            ███░░░░░███                                ░░███
      ██████  ████████   ██████  ████████  ░███    ░░░   ████████ █████ ████  ██████   ███████
     ███░░███░░███░░███ ███░░███░░███░░███ ░░█████████  ███░░███ ░░███ ░███  ░░░░░███ ░░░███░
    ░███ ░███ ░███ ░███░███████  ░███ ░███  ░░░░░░░░███░███ ░███  ░███ ░███   ███████   ░███
    ░███ ░███ ░███ ░███░███░░░   ░███ ░███  ███    ░███░███ ░███  ░███ ░███  ███░░███   ░███ ███
    ░░██████  ░███████ ░░██████  ████ █████░░█████████ ░░███████  ░░████████░░████████  ░░█████
     ░░░░░░   ░███░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░░   ░░░░░███   ░░░░░░░░  ░░░░░░░░    ░░░░░
              ░███                                          ░███
              █████                                         █████
             ░░░░░                                         ░░░░░
                    (c) Andre Tenreiro - https://github.com/atenreiro/opensquat
    """ + Style.RESET_ALL
    )
    print(logo)
    print("\t\t\tversion " + __VERSION__ + "\n")


def main():
    """Main CLI entry point."""
    signal.signal(signal.SIGINT, signal_handler)

    init()
    print_logo()

    args = arg_parser.get_args()

    start_time_squatting = time.time()

    file_content = app.Domain().main(
        args.keywords,
        args.confidence,
        args.domains,
        args.method,
        args.dns
    )

    if args.subdomains or args.vt or args.phishing \
        or args.portcheck:
        print("\n[*] Total found:", len(file_content))

    # Check for subdomains
    if (args.subdomains):
        list_aux = []
        print("\n+---------- Checking for Subdomains ----------+")
        time.sleep(1)
        for domain in file_content:
            print("[*]", domain)
            subdomains = vt.VirusTotal().main(domain, "subdomains")

            if subdomains:
                for subdomain in subdomains:
                    print(
                        Style.BRIGHT + Fore.YELLOW +
                        " \\_", subdomain +
                        Style.RESET_ALL,
                        )
                    list_aux.append(subdomain)
        file_content = list_aux
        print("[*] Total found:", len(file_content))

    # Check for VirusTotal (if domain is flagged as malicious)
    if (args.vt):
        list_aux = []
        print("\n+---------- VirusTotal ----------+")
        time.sleep(1)
        for domain in file_content:
            total_votes = vt.VirusTotal().main(domain)

            # total votes
            harmless = total_votes[0]
            malicious = total_votes[1]

            if malicious > 0:
                print(
                    Style.BRIGHT + Fore.RED +
                    f"[*] found: {domain} ({malicious})" +
                    Style.RESET_ALL,
                )
                list_aux.append(domain)
            elif malicious < 0:
                print(
                    Style.BRIGHT + Fore.YELLOW +
                    f"[*] VT is throttling the response: {domain}" +
                    Style.RESET_ALL,
                )
                list_aux.append(domain)
        file_content = list_aux
        print("[*] Total found:", len(file_content))

    # Check for phishing
    if (args.phishing != ""):
        file_phishing = phishing.Phishing().main(args.keywords)
        output.SaveFile().main(args.phishing, "txt", file_phishing)

    # Check if domain has webserver port opened
    if (args.portcheck):
        list_aux = []
        print("\n+---------- Domains with open webserver ports ----------+")
        time.sleep(1)
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futs = [
                (domain, executor.submit(functools.partial(port_check.PortCheck().main, domain)))
                for domain in file_content
            ]
        
        for tested_domain, result_domain_port_check in futs:
            ports = result_domain_port_check.result()
            if ports:
                list_aux.append(tested_domain)
                print(
                    Fore.YELLOW +
                    "[*]", tested_domain, ports +
                    Style.RESET_ALL
                    )
        
        file_content = list_aux
        print("[*] Total found:", len(file_content))

    output.SaveFile().main(args.output, args.type, file_content)
    end_time_squatting = round(time.time() - start_time_squatting, 2)

    # Print summary
    print("\n")
    print(
        Style.BRIGHT + Fore.GREEN +
        "+---------- Summary Squatting ----------+" +
        Style.RESET_ALL)

    print("[*] Domains flagged:", len(file_content))
    print("[*] Domains result:", args.output)

    if (args.phishing != ""):
        print("[*] Phishing results:", args.phishing)
        print("[*] Active Phishing sites:", len(file_phishing))

    print("[*] Running time: %s seconds" % end_time_squatting)
    print("")

    check_update.CheckUpdate().main()


if __name__ == "__main__":
    main()
