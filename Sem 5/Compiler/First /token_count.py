def count_elements(filename):
    # Define the keywords and operators
    keywords = {
        "auto", "break", "case", "char", "const", "continue", "default", "do",
        "double", "else", "enum", "extern", "float", "for", "goto", "if", "int",
        "long", "register", "return", "short", "signed", "sizeof", "static",
        "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"
    }
    
    operators = {
        "+", "-", "*", "/", "%", "++", "--","="
    }

    # Initialize counts
    keyword_count = 0
    operator_count = 0
    other_count = 0

    with open("sample.c", 'r') as file:
        # Read file content
        content = file.read()
        
        # Split content into words and characters
        words = content.split()
        characters = [char for char in content if char in "+-*/%"]
        
        # Count keywords and other words
        for word in words:
            if word in keywords:
                keyword_count += 1
            elif any(op in word for op in operators):
                operator_count += sum(word.count(op) for op in operators)
            else:
                other_count += 1
        
        # Count operators separately
        operator_count += sum(content.count(op) for op in operators)
    
    # Print results
    print(f"Keyword count: {keyword_count}")
    print(f"Operator count: {operator_count}")
    print(f"Other count: {other_count}")

# Replace 'sample.txt' with the path to your file
count_elements('sample.txt')
