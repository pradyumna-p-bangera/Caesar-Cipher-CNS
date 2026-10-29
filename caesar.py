
from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".")


def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha() and char.isascii():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    message = ""
    shift = 3
    mode = "encrypt"
    error = ""

    if request.method == "POST":
        message = request.form.get("message", "")
        mode = request.form.get("mode", "encrypt")

        try:
            shift = int(request.form.get("shift", 3))

            if not 0 <= shift <= 25:
                error = "Shift value must be between 0 and 25."
            elif mode not in ["encrypt", "decrypt"]:
                error = "Please select a valid operation."
            else:
                result = caesar_cipher(message, shift, mode)

        except ValueError:
            error = "Please enter a valid shift number."

    return render_template(
        "index.html",
        result=result,
        message=message,
        shift=shift,
        mode=mode,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
