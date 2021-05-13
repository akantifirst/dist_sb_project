# Functions:
# get project directory based on a project number
#
# Flow:
# User starts a script from shortcut/CLI and is asked for a project number
# The project number must be validated first:
#   - it must be an  integer
#   - its length must be from 3 to 4 symbols
# If user input is validated, the root directory path of the project as well as the project name must be provided.
# User must confirm that the project name is chosen correctly.
# after user confirmation, the program gives the list of files and asks, should all the sections be processed 'EI', 'BE'
# if the answer is no, user can specify which switchboard needs to be processed by chosing the it via checkoxes (module inquirer)
# after that the program asks if all sections must be processed
# if no the user chooses the sections needed
#

# Beside of user input, the following global variables must be pulled from a separate config file:
#   - root directory of projects {root_projects}
#   - type of files to be searched for {file_type}
#   - typical path template to project plans
#   - additional variables for building the correct path to drawings needed
