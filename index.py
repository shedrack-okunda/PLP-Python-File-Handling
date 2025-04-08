def read_file(filename):
    """Read the content of the file."""
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    """Write the content to a new file."""
    with open(filename, 'w') as file:
        file.write(content)

def modify_content(content):
    """Modify the content (example: convert to uppercase)."""
    return content.upper()

def main():
    input_filename = input("Please enter the filename to read: ")
    output_filename = "modified_" + input_filename  # New filename for modified content

    try:
        # Attempt to read the file
        content = read_file(input_filename)
        print(f"Successfully read from {input_filename}.")
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Write the modified content to a new file
        write_file(output_filename, modified_content)
        print(f"Modified content written to {output_filename}.")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()