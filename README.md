# Steganic v1.0 - 2018 version

Steganography program written in Python named Steganic
works with command options parsing
2 modes ByteEdit and ColorEdit
bad project structure, redudant code, not optimized


# Steganic v2.0 Re; version - 2023

- Has similar option managing as Metasploit with commands
- Cleaned up project structure
- Written with OOP in mind, every file has its own class and meaning
- ColorEdit - writes 8 bits in RGB, 3b in R, 2b in G, 3b in B
- ByteEdit  - replaces B in RGB with 1 byte of message
    # Steganic Commands Syntax
        - set input_img|output_img|mode|msg value
        - detect img_path
        - run Read/Write
        - list
        - help
#Requirements for running Steganic:
- colorama 0.4.5 version
- Pillow 9.4.0 version
    # Installing with requirements.txt
        - pip install -r requirements.txt
    # Manually installing
        - pip install colorama==0.4.5
        - pip install Pillow==9.4.0
