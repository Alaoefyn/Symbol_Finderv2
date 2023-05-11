def get_math_symbol(symbol_name):
    math_symbols = {
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
        "tilde": "∼",
    }
    
    pysic_symbols = {
        "h_bar": "ℏ",
        "angstrom": "Å",
        "mu_0": "μ₀",
        "epsilon_0": "ε₀",
        "sigma": "σ",
        "rho": "ρ",
        "phi": "φ",
        "degree": "°",
        "ohm": "Ω",
        "delta": "Δ",
        "lambda": "λ",
        "nu": "ν",
        "pi": "π",
        "tau": "τ",
        "omega": "ω",
        "alpha": "α",
        "beta": "β",
        "gamma": "γ",
        "delta": "δ",
        "epsilon": "ε",
        "kappa": "κ",
        "chi": "χ",
        "zeta": "ζ",
        "eta": "η",
        "mu": "μ",
        "nu": "ν",
        "sigma": "σ",
        "theta": "θ",
        "xi": "ξ",
        "psi": "ψ",
        "rho": "ρ"
    }
    
    
    
    if symbol_name in math_symbols:
        return math_symbols[symbol_name]
    elif symbol_name in pysic_symbols:
        return pysic_symbols[symbol_name]
    else:
        return None

while True:
    library = input("Please choose desired section: M for Math Symbols, P for Physics Symbols: ")

    if library == "M":
        symbol_name = input("Enter the name of the math symbol you want to find: ")
        symbol = get_math_symbol(symbol_name)
        if symbol:
            print(symbol)
        else:
            print("Symbol not found in archive. Please check your input and try again.")
    elif library == "P":
        symbol_name = input("Enter the name of the physics symbol you want to find: ")
        symbol = get_math_symbol(symbol_name)
        if symbol:
            print(symbol)
        else:
            print("Symbol not found in archive.Please check your input and try again.")
    else:
        print("Invalid input. Please choose M or P and try again.")
        continue

    response = input("Do you wish to continue? Yes or No? (y/n): ")
    if response.lower() != "y":
        break
