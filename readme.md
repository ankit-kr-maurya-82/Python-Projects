
# Python Projects

A collection of small Python scripts and example projects. This repository contains lightweight examples intended for learning and quick experimentation.

**Project Structure**
- **`foodMenu.py`**: Simple script demonstrating a food menu example and basic I/O.
- **`trainTicket/`**: Package with train ticket booking examples and utilities. Notable files:
	- `trainTicket.py` - main script for ticket operations
	- `trainBooking.py` - booking-related helper functions
	- `shortlist.py` - shortlist utilities
	- `data.json`, `train.json`, `trainTicket.json` - sample data files

**Requirements**
- **Python**: 3.8 or newer.
- **Dependencies**: none required for the included scripts. See `requirements.txt` for details.

**Quick Start**

- Run the food menu example from the workspace root:

```
python foodMenu.py
```

- Run the `trainTicket` module (from the workspace root):

```
python -m trainTicket.trainTicket
```

If a script expects input files, make sure you run it from the workspace root so relative paths (for example the `trainTicket` data files) resolve correctly.

**Usage Examples**
- Inspect `trainTicket/trainTicket.py` to see available command-line options or example function calls.
- To experiment interactively, open a Python REPL or use an editor and import the module, for example:

```
python
>>> from trainTicket import trainTicket
>>> help(trainTicket)
```

**Development & Notes**
- These are small educational scripts — feel free to refactor or extract functionality into testable modules.
- If you want, I can add unit tests, example runs, or a small CLI wrapper around the `trainTicket` package.

**Contributing**
- Open a pull request or create an issue describing the change you want to make. Small, focused commits are easier to review.

**License**
- No license file is included. Add a `LICENSE` file if you want to apply an open-source license to this repository.


🔐 Random Password Generator (Python)

A simple Python program that generates a strong random password using letters, digits, and special characters.
The user can enter a custom password length, and the program handles invalid input gracefully.

📌 Features

Generates a random password using:

Uppercase letters

Lowercase letters

Numbers

Special characters

Accepts custom password length

Uses a default length if invalid input is provided

Easy to modify and extend

🚀 How to Run

1. Install Python (if not already installed).

2. Save the script as password_generator.py.

3. Run the script: