# Random-Password-Generator
# Random Password Generator (GUI)
A simple Python application with a graphical user interface (GUI) to generate strong passwords and passphrases. The GUI allows users to specify the desired length or word count and generates either a random password or a secure passphrase.

## Features
✅ Generates strong passwords with uppercase, lowercase, digits, and symbols  
✅ Creates passphrases using random words  
✅ User-friendly GUI built with Tkinter  
✅ Customizable length for passwords and passphrases  
✅ Stylish purplish-pink theme  

## Requirements
Ensure you have Python installed on your system (Python 3+). The script uses the built-in `random`, `string`, and `tkinter` modules, so no additional dependencies are required.

## Installation
1. Clone this repository or download the script:
   ```
   git clone https://github.com/your-repo/random-password-generator.git
   cd random-password-generator
   ```
2. Run the script:
   ```
   python password_generator.py
   ```

## Usage
1. Enter the desired **password length** (minimum 4) or **passphrase word count** (minimum 2).
2. Select either **"Password"** or **"Passphrase"**.
3. Click **"Generate"** to see the result.

## Example Output
🔐 **Password:** `A$k3@f8z!Tq`  
📝 **Passphrase:** `apple-jungle-delta-banana`  

## Customization
You can modify the word list for passphrases in the `generate_passphrase()` function by adding or removing words from the list.

## License
This project is open-source and available under the MIT License.

