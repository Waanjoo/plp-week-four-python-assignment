def read_file_content(filename):
  """Reads the content of a file.

  Args:
    filename: The name of the file to read.

  Returns:
    The content of the file as a string.

  Raises:
    FileNotFoundError: If the file is not found.
    IOError: For other I/O errors.
  """

  try:
    with open(filename, 'r') as file:
      return file.read()
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    raise
  except IOError as e:
    print(f"Error: I/O error occurred: {e}")
    raise

if __name__ == "__main__":
  filename = input("Enter the filename: ")
  try:
    content = read_file_content(filename)
    print(content)
  except FileNotFoundError:
    print("File not found. Please check the filename.")