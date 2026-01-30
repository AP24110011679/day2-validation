# day2-validation
This repository contains my day-2 challenge python program for input validation
Student Registration Validation Program
📌 Overview
This Python program validates user input for Student ID, Email, Password, and Referral Code based on predefined rules.
If all inputs meet the required format, the program prints Approved; otherwise, it prints Rejected.
🧠 Features
The program checks:
Student ID format
Email format
Password strength
Referral code format
📥 Input Requirements
1️⃣ Student ID
Must follow this format:
Length = 7 characters
Starts with CSE-
Last 3 characters must be digits
✅ Example: CSE-123
2️⃣ Email
Must meet these conditions:
Contains @ and .
Must not start or end with @
Must end with .edu
✅ Example: student@college.edu
3️⃣ Password
Must:
Be at least 8 characters
Start with an uppercase letter
Contain letters + numbers or symbols
❌ Only alphabets are not allowed
✅ Example: Password1
4️⃣ Referral Code
Must follow this format:
Length = 6 characters
Starts with REF
Next 2 characters must be digits
Last character must be @
✅ Example: REF12@
▶️ How to Run
Install Python
Copy the program into a file named validation.py
Run the program using:
Copy code

python validation.py
📤 Output
If all inputs are valid:
Copy code

Approved
If any input is invalid:
Copy code

Rejected
💻 Sample Run
Copy code

Enter student id: CSE-101
Enter email: nani@college.edu
Enter password: StrongPass1
Enter referral: REF45@
Approved
