<img width="1919" height="1079" alt="Screenshot 2026-06-29 180545" src="https://github.com/user-attachments/assets/42f0d7ed-43ea-4bd9-aaa9-39404f272114" />
<img width="1919" height="1079" alt="Screenshot 2026-06-29 180526" src="https://github.com/user-attachments/assets/98b7f1bf-4c51-433e-92d2-8d9d41d336fa" />
<img width="1919" height="1079" alt="Screenshot 2026-06-29 180505" src="https://github.com/user-attachments/assets/7efd2c26-0bd6-4735-8b64-ed01c7f7411a" />


# Password Strength Checker

A Python-based password analysis tool that evaluates password strength using multiple security checks and provides actionable feedback for improvement.

> This project was built as part of my Python learning journey. The goal was not only to create a password checker but also to practice object-oriented programming, regular expressions, file handling, modular project structure, and security-focused problem solving.

---

## Features

### Password Composition Analysis

Checks whether the password contains:

* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

### Length Evaluation

Evaluates password length and rewards longer passwords.

### Common Password Detection

Checks the password against a list of the 10,000 most commonly used passwords.

Examples:

* password
* qwerty
* admin123

Passwords found in this list are immediately classified as insecure.

### Leetspeak Detection

Normalizes common substitutions used to disguise weak passwords.

Examples:

* P@ssword → Password
* P4ssw0rd → Password
* Adm1n → Admin

This helps detect weak passwords that attempt to bypass simple dictionary checks.

### Repeated Pattern Detection

Detects repeating chunks of text.

Examples:

* abcabc
* xyzxyz
* testtest

### Excessive Character Repetition

Detects repeated characters that reduce password strength.

Examples:

* aaa
* 111
* $$$

### Keyboard Sequence Detection

Detects predictable keyboard patterns and paths.

Examples:

* qwerty
* asdf
* zxcv
* 1234
* 4321

The checker supports multiple keyboard layouts:

* QWERTY
* QWERTZ
* AZERTY
* Numeric keypad patterns

### Security Scoring

Assigns a score based on:

* Password length
* Character diversity
* Common password usage
* Repetition patterns
* Keyboard sequences

### Actionable Feedback

Provides detailed suggestions to improve password security.

Example:

1. Add an uppercase letter.
2. Add a special character.
3. Avoid keyboard sequences such as qwerty.

---

## Project Structure

```text
password-strength-checker/
│
├── main.py
├── inspection.py
├── scorer.py
├── reporter.py
├── data.py
├── 10k-most-common.txt
└── README.md
```

### Modules

#### Inspection

Responsible for analyzing the password and collecting information such as:

* Length
* Character categories
* Common-password status
* Keyboard sequences
* Repetition patterns

#### Scorer

Calculates a strength score based on the analysis results.

#### Reporter

Displays the final score and recommendations to the user.

#### Data

Stores keyboard layouts and sequence data used for pattern detection.

---

## Example Usage

```text
---Welcome to the Password Strength Checker---

Let me know the password that you want to analyze.
password123

your password is weaker. with score: 0/10

you need to work on below points to make your password secure.

1. CRITICAL: This password is among the most commonly used passwords and is easily hacked!
```

Another example:

```text
---Welcome to the Password Strength Checker---

Let me know the password that you want to analyze.
Tr7$kP9!LmQ

your password is strong. with score: 8/10

Excellent! Your password meets all security guidelines.
```

---

## Concepts Practiced

This project helped me practice:

* Object-Oriented Programming (OOP)
* Python classes and modules
* Regular expressions (regex)
* File handling
* Dictionaries and lists
* String processing
* Program architecture
* Security-focused validation logic
* User feedback systems

---

## Limitations

This project is intended for educational purposes and does not provide a complete security assessment.

It currently does not:

* Check password breach databases (e.g., Have I Been Pwned)
* Calculate true password entropy
* Estimate password cracking time
* Detect personal information such as names or birthdays
* Perform advanced probabilistic password analysis

---

## Future Improvements

Possible future enhancements:

* Entropy estimation
* Password crack-time estimation
* Have I Been Pwned API integration
* GUI version using Tkinter or PyQt
* Web application version using Flask or FastAPI
* Unit testing suite
* Configuration-driven scoring system
* Advanced password intelligence analysis

---

## Learning Notes

This project evolved significantly during development. What started as a simple password validator gradually expanded into a multi-layered password analysis tool with:

* Common password detection
* Pattern recognition
* Leetspeak normalization
* Keyboard sequence analysis

---
