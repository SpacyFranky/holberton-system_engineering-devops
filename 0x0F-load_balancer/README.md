# 0x0F. Load balancer
# Background Context
I have been given 2 additional servers:
* gc-[STUDENT_ID]-web-02-XXXXXXXXXX
* gc-[STUDENT_ID]-web-02-XXXXXXXXXX
Lets improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, I will need to write Bash scripts to automate my work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.
# Requirements
* Allowed editors: vi, vim, emacs
* All files were interpreted on Ubuntu 16.04 LTS
* All Bash script files are executable
* Bash script must pass Shellcheck (version 0.3.7) without any error
* The first line of all your Bash scripts is exactly #!/usr/bin/env bash
* The second line of all Bash scripts should be a comment explaining what is the script doing