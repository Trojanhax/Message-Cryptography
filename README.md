


# Message Cryptography 

## Purpose

This Python project demonstrates basic cryptography concepts using the `cryptography` library. It includes functions for generating encryption keys, encrypting messages, and decrypting messages using the Fernet symmetric encryption scheme. The project is a useful starting point for learning about cryptography and securing sensitive data.

## Features

- Generate random encryption keys.
- Encrypt plaintext messages.
- Decrypt encrypted messages.
- Test the encryption and decryption functions.

## Project Structure

The project has the following structure:

```bash
project_directory/
├── 03.py (main script)
├── main.py (cryptography functions)
├── test_encrypt_decrypt.py (test script)
├── README.md
├── venv/ (Python virtual environment, optional)
```

## Setup

To set up this project on your local machine, follow these steps:

1. Clone the project repository from GitHub:

```bash
   git clone https://github.com/Trojanhax/Message-Cryptography.git
```

2. Navigate to the project directory:

```bash
   cd cryptography-project
```

3. Create a virtual environment (optional but recommended):

```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

4. Install the required packages:

```bash
   pip install cryptography pytest  # Install necessary packages
```

5. Run the tests to verify that everything is set up correctly:

```bash
pytest test_encrypt_decrypt.py
```

## Usage

To use the project, you can integrate the `main.py` module into your own Python applications, or use it as a reference for your cryptography-related tasks. You can create, encrypt, and decrypt messages as follows:

```python
from main import generate_key, encrypt_message, decrypt_message

# Generate a key
key = generate_key()

# Encrypt a message
message = "Hello, World!"
encrypted_message = encrypt_message(key, message)

# Decrypt the message
decrypted_message = decrypt_message(key, encrypted_message)
```

## Contributing

Contributions to this project are welcome! You can contribute by opening issues, suggesting improvements, or making pull requests. Please follow the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- Trojan hax
- GitHub: [https://github.com/Trojanhax](https://github.com/Trojanhax)


