# Password Generator

A secure console-based Password Generator built with Python.

This application allows users to generate one or multiple passwords with customizable settings, evaluate password strength, and optionally save generated passwords to a text file.

## Features

* Generate secure passwords using Python's `secrets` module
* Choose password length (1–100 characters)
* Include or exclude:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Symbols
* Generate multiple passwords at once
* Assign custom names to generated passwords
* Password strength evaluation
* Save generated passwords to a text file
* Input validation and error handling
* User-friendly menu system

## Technologies Used

* Python 3
* Built-in Modules:

  * `string`
  * `secrets`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Donyadev/password-generator
```

2. Navigate to the project folder:

```bash
cd password-generator
```

3. Run the program:

```bash
python password_generator.py
```

## Usage

### Main Menu

```text
===== PASSWORD GENERATOR MENU =====
1. Generate passwords
2. Exit
```

### Password Configuration

The user can:

* Select password length
* Choose which character types to include
* Generate multiple passwords
* Show or hide generated passwords
* Save passwords to a file

### Example Output

```text
===== PASSWORD GENERATOR MENU =====
1. Generate passwords
2. Exit

Choose an option: 1

Enter password length: 12

Include uppercase letters? (y/n) y
Include lowercase letters? (y/n) y
Include numbers? (y/n) y
Include symbols? (y/n) y

Selected:
✓ Uppercase
✓ Lowercase
✓ Numbers
✓ Symbols

How many passwords do you want to generate? 1

Enter a name for password 1: Gmail

✓ Password Generated Successfully

Account: Gmail
Password: @A8m#K2pQ!4x
Strength: strong
```

## Password Strength Rules

The password strength checker evaluates:

* Minimum length of 8 characters
* Presence of uppercase letters
* Presence of lowercase letters
* Presence of numbers
* Presence of symbols

Strength levels:

| Score | Strength  |
| ----- | --------- |
| 0-1   | Very Weak |
| 2-3   | Weak      |
| 4     | Medium    |
| 5     | Strong    |

## File Saving

Generated passwords can be saved into:

```text
passwords.txt
```

Example:

```text
========== GENERATED PASSWORDS ==========

Gmail: @A8m#K2pQ!4x
GitHub: h4J!xP9@Lm2
```

## Project Structure

```text
password-generator/
│
├── password_generator.py
└── README.md
```

## Learning Objectives

This project was created to practice:

* Functions
* Loops
* Conditional Statements
* Dictionaries
* Lists
* Input Validation
* Error Handling (`try/except`)
* File Handling
* Secure Random Generation
* Modular Programming

## Future Improvements

Possible future enhancements:

* Export passwords to JSON
* Custom symbol selection
* Copy password to clipboard
* GUI version using Tkinter

## Author

Created by Donya Hamidi as part of a Python learning journey.
