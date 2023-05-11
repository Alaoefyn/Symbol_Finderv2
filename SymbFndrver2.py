def get_math_symbol(symbol_name):
    symbols = {
        "integral": "∫",
        "sum": "∑",
        "product": "∏",
        "infinity": "∞",
        "partial": "∂",
        "alpha": "α",
        "beta": "β",
        "gamma": "γ",
        "delta": "δ",
        "epsilon": "ε",
        "theta": "θ",
        "lambda": "λ",
        "mu": "μ",
        "sigma": "σ",
        "omega": "ω",
        "hash": "#",
        "left_bracket": "[",
        "right_bracket": "]",
        "left_brace": "{",
        "right_brace": "}",
        "asterisk": "*",
        "underscore": "_",
        "pipe": "|",
        "less_than": "<",
        "greater_than": ">",
        "apostrophe": "'",
        "caret": "^",
        "plus": "+",
        "minus": "-",
        "slash": "/",
        "left_paren": "(",
        "right_paren": ")",
        "percent": "%",
        "tilde": "\u223C"
    }
    if symbol_name in symbols:
        return symbols[symbol_name]
    else:
        print("Symbol not found in archive")

symbol_name = input("Enter the name of the math symbol you want to find: ")
symbol = get_math_symbol(symbol_name)
if symbol:
    print(symbol)
