# Assignment 1 - Python Behave BDD

## Objective

Set up and execute a Python BDD framework using Behave for an end-to-end embedded-platform simulation workflow.

## Tools

- Python
- Behave
- PyCharm
- QEMU
- GDB
- Eclipse

## Project Structure

Assignment_1/
    features/
        login.feature
        environment.py
        steps/
            login_steps.py
    src/
        application.py
    README.md

## Installation

Open the PyCharm terminal and run:

python -m pip install behave

## Run the BDD Tests

From the Assignment_1 directory run:

python -m behave

## Expected Result

Both scenarios should pass.

## QEMU and GDB

The provided Python application represents the simulated application logic used by the Behave scenarios. QEMU must be configured separately for the specific embedded platform supplied by the training assignment because the target architecture, firmware image, kernel image, machine type, memory configuration, and GDB port are platform-specific.

A typical QEMU debugging workflow is:

1. Start the target in QEMU with GDB waiting enabled.
2. Start Eclipse.
3. Configure the GDB debugger with the target architecture and executable.
4. Connect GDB to the QEMU GDB server.
5. Set breakpoints.
6. Start or continue execution.
7. Execute the Behave scenarios against the simulated application.

The exact QEMU command must be replaced with the command provided for the assigned embedded platform.

## PyCharm

Open Assignment_1 as a project in PyCharm and set the Python interpreter.

Open the terminal in PyCharm and run:

python -m behave

## Day 1

Install and verify QEMU, GDB, Eclipse, Python and Behave. Configure the embedded target in QEMU and connect GDB through Eclipse.

## Day 2-4

Implement the remaining scenarios supplied with the original assignment and execute them against the simulated environment.
