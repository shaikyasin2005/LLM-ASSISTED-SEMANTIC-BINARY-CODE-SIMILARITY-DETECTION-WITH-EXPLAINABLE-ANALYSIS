import subprocess
import os

# Path to RetDec executable
RETDEC_PATH = r"D:\retdec\bin\retdec-decompiler.exe"


def disassemble_file(input_path):

    # Output C file
    output_path = input_path + ".c"

    try:

        command = [
            RETDEC_PATH,
            input_path,
            "-o",
            output_path
        ]

        subprocess.run(command, check=True)

        if os.path.exists(output_path):
            with open(output_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()

        return ""

    except Exception as e:
        print("RetDec Error:", e)
        return ""
