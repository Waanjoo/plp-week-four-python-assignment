def read_and_modify_file(input_file, output_file):
  """Reads a file, modifies its content, and writes it to a new file.

  Args:
    input_file: The name of the input file.
    output_file: The name of the output file.
  """

  try:
    with open(input_file, 'r') as file:
      content = file.read()

    # Modify the content (e.g., reverse the lines)
    modified_content = content.splitlines()[::-1]
    modified_content = '\n'.join(modified_content)

    with open(output_file, 'w') as file:
      file.write(modified_content)

    print(f"File '{output_file}' created successfully.")

  except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
  except IOError as e:
    print(f"Error: I/O error occurred: {e}")

if __name__ == "__main__":
  input_file = input("Enter the input file name: ")
  output_file = input("Enter the output file name: ")
  read_and_modify_file(input_file, output_file)