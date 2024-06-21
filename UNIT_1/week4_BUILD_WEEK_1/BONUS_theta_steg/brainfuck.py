def brainfuck_to_text(code):
    """
    This function decodes Brainfuck code into text.
    
    :param code: A string containing Brainfuck code
    :return: The decoded message as a string
    """
    memory = [0] * 30000  # Initialize memory tape with 30,000 cells
    pointer = 0  # Memory pointer
    code_pointer = 0  # Code pointer
    output = []  # Output list to store the decoded characters
    loop_stack = []  # Stack to handle loops

    while code_pointer < len(code):
        command = code[code_pointer]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '.':
            output.append(chr(memory[pointer]))
        elif command == ',':
            memory[pointer] = ord(input()[0])  # Read a single character
        elif command == '[':
            if memory[pointer] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    code_pointer += 1
                    if code[code_pointer] == '[':
                        open_brackets += 1
                    elif code[code_pointer] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(code_pointer)
        elif command == ']':
            if memory[pointer] != 0:
                code_pointer = loop_stack[-1]
            else:
                loop_stack.pop()

        code_pointer += 1

    return ''.join(output)

def read_brainfuck_from_file(file_path):
    """
    Reads the Brainfuck code from a specified file.
    
    :param file_path: Path to the file containing Brainfuck code
    :return: The Brainfuck code as a string
    """
    with open(file_path, 'r') as file:
        return file.read()

def append_message_to_file(file_path, message):
    """
    Appends the decoded message to the same file as a new line.
    
    :param file_path: Path to the file
    :param message: The decoded message to append
    """
    with open(file_path, 'a') as file:
        file.write('\n' + message)

# Example usage
file_path = '01.jpg.out'  # Change this to your file path
brainfuck_code = read_brainfuck_from_file(file_path)
decoded_message = brainfuck_to_text(brainfuck_code)
append_message_to_file(file_path, decoded_message)
