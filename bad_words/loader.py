import os
import shutil

class Load:
    def __init__(self) -> None:
        # Get the path to the directory of the current script
        self.script_dir = os.path.dirname(os.path.realpath(__file__)
        
        # Define directories for bad words and good words resources
        self.resource_dir_bad_words = os.path.join(self.script_dir, 'resource/bad_words')
        self.resource_dir_good_words = os.path.join(self.script_dir, 'resource/good_words')

    def update_file(self, source_file: str, target_dir: str) -> None:
        # Check if the source file exists and is a file
        if os.path.exists(source_file) and os.path.isfile(source_file):
            # Generate the target file path by joining the target directory and the source file's base name
            target_file = os.path.join(target_dir, os.path.basename(source_file))
            
            # If the target file already exists, remove it
            if os.path.exists(target_file):
                os.remove(target_file)
            
            # Copy the source file to the target directory
            shutil.copy(source_file, target_file)
        else:
            raise FileNotFoundError(f"File not found at {source_file}")

    def load_bad_file(self, file_path: str) -> None:
        # Load the specified file into the bad words resource directory
        self.update_file(file_path, self.resource_dir_bad_words)

    def load_good_file(self, file_path: str) -> None:
        # Load the specified file into the good words resource directory
        self.update_file(file_path, self.resource_dir_good_words)

class Unload:
    def __init__(self) -> None:
        # Get the path to the directory of the current script
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        
        # Define directories for bad words and good words resources
        self.resource_dir_bad_words = os.path.join(self.script_dir, 'resource/bad_words')
        self.resource_dir_good_words = os.path.join(self.script_dir, 'resource/good_words')

    def unload_file(self, source_file: str, target_dir: str) -> None:
        # Check if the source file exists and is a file
        if os.path.exists(source_file) and os.path.isfile(source_file):
            # Generate the target file path by joining the target directory and the source file's base name
            target_file = os.path.join(target_dir, os.path.basename(source_file))
            
            # If the target file already exists, remove it
            if os.path.exists(target_file):
                os.remove(target_file)
            
            # Copy the source file to the target directory
            shutil.copy(source_file, target_file)
        else:
            raise FileNotFoundError(f"File not found at {source_file}")

    def unload_bad_file(self, file_path: str) -> None:
        # Unload the specified file from the bad words resource directory
        self.unload_file(file_path, self.resource_dir_bad_words)

    def unload_good_file(self, file_path: str) -> None:
        # Unload the specified file from the good words resource directory
        self.unload_file(file_path, self.resource_dir_good_words)
