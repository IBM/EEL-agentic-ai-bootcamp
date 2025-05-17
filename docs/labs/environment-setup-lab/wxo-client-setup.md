# Lab 0 - Environment setup: running wxo-client adk locally

!!! note
    Follow these instructions for running wxo-client ADK locally in order to successfully complete the Agentic AI pro-code bootcamp labs.

## Installing the ADK

Install the IBM watsonx Orchestrate ADK on your computer.
​
## Installation prerequisites

- Install the required software to enable the ADK installation:
    - Python: The programming language that the ADK is written in. The ADK requires at least Python 3.11, and the latest compatible version is Python 3.13. For more information, see Python.
    - Pip: Pip is Python’s package manager. In some operating systems, it’s included with Python’s installation. For more information, see Pip.

- Optional: Create a virtual environment with venv to install the ADK. For more information, see venv --- Creation of virtual environments.


## Installing the ADK

- Install the ADK with pip.

```
pip install ibm-watsonx-orchestrate

```

- Test the installation:

```
orchestrate --help

```

!!! Note: Use the --help argument to get information about each command and its arguments in the ADK CLI.

## Enabling the Bootcamp Environment

```
orchestrate env add --name bootcamp --url <REPLACE_WITH_WXO_INSTANCE_URL> -t ibm_iam
orchestrate env activate bootcamp

```