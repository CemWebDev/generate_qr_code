# generate_qr_code

This project is a Python application that generates QR codes, including custom-designed ones. It uses the qrcode' and 'Pillow' libraries to create and manipulate QR codes.

## Features

- Generate QR codes from URLs
- Customize QR code appearance with colors and borders
- Save QR codes as images


## Installation

To get started with this project, you'll need to have Python installed. Follow the steps below to set up the project.

1. Clone the repository:

    ```bash
    git clone https://github.com/SimplyProgYT/qr-code-generator.git
    cd qr-code-generator/generate_qr_code
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To generate a QR code, run the `generate_qr_code.py` script. You can customize the URL and other parameters directly in the script.

```bash
python generate_qr_code.py

