from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def Odd_Even():
    return("Welcome here to find your number is Armstrong or Not\n Its a simple demo project just give idea to"
           "\nHow Its work")
@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while (n > 0):
        digit = n % 10
        sum += digit ** order
        n = n // 10
    if (sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Server IP": "122.135.222.4"
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": False,
            "Server IP": "122.135.222.4"
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
