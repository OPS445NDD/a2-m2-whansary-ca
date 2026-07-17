#!/usr/bin/env python3

'''
OPS445 Assignment 2 - Winter 2023
Program: assignment2.py
Author: Walid Hasan Ansary

The Python code in this file is original work written by
Walid Hasan Ansary. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or online resource. I have not shared this Python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description:
This program retrieves Linux system and process memory information.
It creates memory usage bar graphs, retrieves process IDs, and calculates
the resident memory used by individual processes.

Date: July 17, 2026
'''

import argparse
import os
import sys


def parse_command_args() -> object:
    """Set up and return the command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Memory Visualiser -- See Memory Usage Report with bar charts"
        ),
        epilog="Copyright 2023"
    )

    parser.add_argument(
        "-H",
        "--human-readable",
        action="store_true",
        help="Prints sizes in human readable format"
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=20,
        help="Specify the length of the graph. Default is 20."
    )

    parser.add_argument(
        "program",
        type=str,
        nargs="?",
        help=(
            "if a program is specified, show memory use of all "
            "associated processes. Show only total use if not."
        )
    )

    return parser.parse_args()


def percent_to_graph(percent: float, length: int = 20) -> str:
    """Turn a percentage between 0.0 and 1.0 into a bar graph."""
    number_of_hashes = round(percent * length)
    number_of_spaces = length - number_of_hashes

    return "#" * number_of_hashes + " " * number_of_spaces


def get_sys_mem() -> int:
    """Return total system memory in KiB."""
    with open("/proc/meminfo", "r") as meminfo_file:
        for line in meminfo_file:
            if line.startswith("MemTotal:"):
                return int(line.split()[1])

    return 0


def get_avail_mem() -> int:
    """Return currently available system memory in KiB."""
    with open("/proc/meminfo", "r") as meminfo_file:
        for line in meminfo_file:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])

    return 0


def pids_of_prog(app_name: str) -> list:
    """Return a list of process IDs associated with an application."""
    command_output = os.popen(f"pidof {app_name}").read()

    return command_output.split()


def rss_mem_of_pid(proc_id: str) -> int:
    """Return the total resident memory used by a process in KiB."""
    rss_total = 0

    with open(f"/proc/{proc_id}/smaps", "r") as smaps_file:
        for line in smaps_file:
            if line.startswith("Rss:"):
                rss_total += int(line.split()[1])

    return rss_total


def bytes_to_human_r(
        kibibytes: int,
        decimal_places: int = 2
) -> str:
    """Convert a KiB memory value into a human-readable value."""
    suffixes = ["KiB", "MiB", "GiB", "TiB", "PiB"]
    suffix_count = 0
    result = kibibytes

    while result > 1024 and suffix_count < len(suffixes) - 1:
        result /= 1024
        suffix_count += 1

    string_result = f"{result:.{decimal_places}f} "
    string_result += suffixes[suffix_count]

    return string_result


if __name__ == "__main__":
    args = parse_command_args()

    # Output formatting will be completed during the final submission.
    if not args.program:
        pass
    else:
        pass

