# PASSWORD AUTHENTICATION

## Overview

This Python script is designed to help users evaluate the strength of their passwords. It utilizes functions from two separate modules: `password_entry` and `figlet_one`. The primary features include retrieving a password, providing feedback on its strength, and simulating hashcat functionality for password cracking.

## Prerequisites

1. **Python 3**: Ensure you have Python 3 installed on your system. This script has been tested with Python 3.x versions.

2. **rockyou.txt**: The script requires the `rockyou.txt` file for password simulation. This file is commonly found in the `/usr/share/wordlists/` directory for Kali Linux users. Ensure this file is accessible in the specified directory.

3. **Modules**: This script depends on two external modules:
   - `password_entry`: Contains functions for password retrieval, feedback, and strength checking.
   - `figlet_one`: Provides functionality for displaying text in a stylized format.

## How to Use

1. **Place the Modules**: Ensure that the `password_entry` and `figlet_one` modules are located in the same directory as this script, or adjust the import statements accordingly if they are in different locations.

2. **Execute the Script**: Run the script using Python 3. You can do this from the command line with:

   ```bash
   python3 <script_name>.py
   ```

   Replace `<script_name>` with the name of your script file.

3. **Interaction**: When executed, the script will:
   - Display a title "Password Auth" styled by the `print_title` function from `figlet_one`.
   - Prompt the user to enter a password using the `get_password` function.
   - Provide feedback on the password using `password_feedback`.
   - Check the password's strength with `check_password_strength`.
   - Simulate hashcat functionality for the given password with `simulate_hashcat`.

## Error Handling

- **General Exceptions**: If an error occurs, a message will be printed, and the script will suggest trying again.
- **Keyboard Interruptions**: If interrupted by the user, the script will gracefully handle the interruption and provide a friendly message.

## Additional Notes

- Ensure that the `rockyou.txt` file is located in the `/usr/share/wordlists/` directory or update the script or module configurations if it is located elsewhere.
- Modify or extend the `password_entry` and `figlet_one` modules as needed for your specific use case.

For any further assistance or questions, please refer to the documentation or reach out to me by [Mail](shina.salau19@kwasu.edu.ng).

Happy password testing!
