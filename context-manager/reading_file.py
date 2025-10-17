import logging
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class FileReader:
    def __init__(self, filePath, mode="r", chunk_size=None):
        self._filepath = filePath
        self.mode = mode
        self.file = None
        self.chunk_size = chunk_size

    def __enter__(self):
        logging.info(f"Opening file: {self._filepath}")
        self.file = open(self._filepath, self.mode)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            logging.info(f"Closing file: {self._filepath}")
        if exc_type:
            logging.error(f"Error occurred: {exc_val}")
        return False

    def readfile(self):
        self.file.seek(0)
        return self.file.read()
    
    def read_lines(self):
        self.file.seek(0)
        if self.chunk_size is None:
            for line in self.file:
                yield line
        else:
            chunk = []
            for i, line in enumerate(self.file, start=1):
                chunk.append(line)
                if i % self.chunk_size == 0:
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk

# Portable path construction
filePath = os.path.join(os.getcwd(), "context-manager", "large_file.txt")

with FileReader(filePath, chunk_size=1000) as reader:
    for chunk in reader.read_lines():
        logging.info(f"Processing {len(chunk)} lines")
        # for line in chunk: print(line.strip())  # optional for testing small files
