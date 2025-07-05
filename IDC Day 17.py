# Build a context manager for safe file handling

class SafeFileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except Exception as e:
            print(f"Error opening file: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            try:
                self.file.close()
                print(f"File '{self.filename}' closed safely.")
            except Exception as e:
                print(f"Error closing file: {e}")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        # Returning False will re-raise the exception if one occurred
        return False

# Example usage
with SafeFileHandler('example.txt', 'w') as file:
    file.write("Hello, World!")