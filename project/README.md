# Fast (Similar and Flipped) Images Finder

#### Video Demo:  <[youtube](https://youtu.be/kRrvZk1Ze7s)>
#### Description:
A Python program designed to identify similar images within a specified folder to a reference image. It utilizes the PIL (Python Imaging Library) library for image processing tasks, including opening, hashing, and flipping images. This README file provides an overview of the program's functionality, usage instructions, and key features.

## Key Features

- **Image File Validation:** The program verifies whether a file is an image based on its extension before processing it.
- **Hash-based Comparison:** It computes hash values for images using the average hash algorithm provided by the imagehash library. These hash values are then compared to determine similarity between images.
- **Folder Navigation:** Users can specify a folder containing images to compare against a reference image. The program navigates through the folder and identifies similar images.
- **CSV Output:** The program generates a CSV file containing the filenames of similar images found within the specified folder.
- **User Interaction:** Users interact with the program through the command-line interface, providing input for the reference image file path and the folder path containing images to compare.

## Functions description

1. **is_image_file(filename: str) -> bool**

   **Purpose:** This function determines whether a given file is an image based on its file extension.

   **Components:**
   - **is in:** There's no explicit loop here, but the function utilizes a set of image file extensions to check if the filename ends with any of these extensions.
   - **Variable Types:** The filename parameter is of type str, representing the name of the file. The return type is bool, indicating whether the file is an image or not.
   - **Key Concept:** It leverages the endswith() method to check if the filename ends with any of the predefined image file extensions.
   - **Error Handling:** It handles the case where the filename attribute is not available by catching the AttributeError.

2. **compare_hashes(hash1: str, hash2: str) -> bool**

   **Purpose:** Compares two image hashes to determine if they are identical, indicating similarity between the images.

   **Components:**
   - **Error Handling:** The function handles potential errors arising from comparing the hashes by catching ValueError and TypeError.
   - **Variable Types:** Parameters hash1 and hash2 are of type str, representing the hash values of two images. The return type is bool, indicating whether the hashes are identical.
   - **Key Concept:** It compares the hash values of two images using the equality operator (==).
   - **Error Handling:** It handles errors that may occur during hash comparison, such as invalid hash values or incompatible types.

3. **check_path(path: str, is_folder: bool = False) -> bool**

   **Purpose:** Checks if a given path exists and whether it corresponds to a file or a folder.

   **Components:**
   - **Error Handling:** The function is wrapped in a try-except block to handle potential errors, such as a non-existent path or inaccessible folder.
   - **Conditional Statements:** It uses conditional statements to check if the path exists and whether it is a file or a folder.
   - **Key Concept:** It utilizes the os.path.exists() function to verify the existence of the path and os.path.isfile() and os.path.isdir() functions to determine if it's a file or a folder.
   - **Error Handling:** It returns False in case of any exceptions encountered during path verification.

4. **compute_hash(image_path: str, get_flipped_hash_too: bool = True)**

   **Purpose:** Computes the hash value of an image file, optionally including the hash value of its horizontally flipped version.

   **Components:**
   - **Error Handling:** The function handles potential errors, such as file not found or inability to open the image file, by catching FileNotFoundError and OSError.
   - **Conditional Execution:** It conditionally computes the hash of the flipped image based on the value of the get_flipped_hash_too parameter.
   - **Key Concept:** It utilizes the Image module from the PIL library to open and process the image file, and the imagehash module to compute the hash value.
   - **Error Handling:** It gracefully exits the program with an error message if it encounters any exceptions during image processing.

5. **find_similar_images_in_folder(ref_picture: str, folder_path: str) -> list[str]**

   **Purpose:** Finds similar images to a reference image within a specified folder.

   **Components:**
   - **Loop:** It employs a for loop to iterate over all files in the specified folder.
   - **Error Handling:** The function is wrapped in a try-except block to handle potential errors, such as inability to access the folder or open image files.
   - **Key Concept:** It utilizes previously defined functions (is_image_file() and compute_hash()) to filter image files and compute their hash values, respectively. Additionally, it compares hash values to identify similar images.
   - **Error Handling:** It handles exceptions that may occur during the execution of the function, ensuring graceful error handling and program termination.

6. **get_user_input() -> tuple[str, str]**

   **Purpose:** Prompts the user to input the path to the reference image file and the folder containing images.

   **Components:**
   - **Error Handling:** The function handles various potential errors, such as keyboard interrupts (KeyboardInterrupt), end-of-file signals (EOFError), and general exceptions (Exception).
   - **Key Concept:** It utilizes the input() function to receive user input and the check_path() function to validate the input paths.
   - **Error Handling:** It gracefully exits the program with appropriate error messages in case of errors or interruptions.

7. **write_csv(similar_images: list[str]) -> None**

   **Purpose:** Writes the list of filenames of similar images to a CSV file.

   **Components:**
   - **File Handling:** It uses the csv module to create and write data to a CSV file.
   - **Key Concept:** It opens a CSV file in write mode and uses a csv.writer object to write the filenames of similar images to the file.
   - **Error Handling:** It ensures the proper handling of file operations and exceptions during file writing.

8. **main() -> None**

   **Purpose:** The main function to run the image similarity finder.

   **Components:**
   - **Function Calls:** It calls other functions in a structured manner to perform the image similarity analysis.
   - **Key Concept:** It orchestrates the execution flow of the program, from user input to finding similar images and writing results to a CSV file.
   - **Error Handling:** It ensures proper error handling throughout the execution, handling exceptions and displaying appropriate error messages.



## Python Syntax Features and Advantages explored on this project

## 1. String Slicing:

### Usage:
Python allows slicing of strings using square brackets `[]` with the syntax `[start:stop:step]`, where `start` is the starting index (inclusive), `stop` is the ending index (exclusive), and `step` is the step size.

### Advantages:
- **Concise Code:** String slicing enables concise extraction of substrings or manipulation of string contents.
- **Readability:** It enhances code readability by expressing string operations in a clear and succinct manner.

### Example:
```python
filename.lower().endswith(image_extensions)
```

In this expression, `filename.lower()` converts the filename to lowercase, and `endswith(image_extensions)` checks if it ends with any of the specified image extensions.

## 2. Tuple Unpacking:

### Usage:
Python supports unpacking of tuples, allowing multiple values to be assigned to multiple variables in a single line.

### Advantages:
- **Efficient Assignment:** It enables efficient assignment of values from a tuple to individual variables, reducing code verbosity.
- **Enhanced Readability:** Tuple unpacking enhances code readability by expressing multiple assignments in a single line.

## 3. Error Handling with Try-Except Blocks:

### Usage:
Python's try-except blocks enable graceful handling of exceptions, allowing code to recover from errors and continue execution or provide meaningful error messages.

### Advantages:
- **Robustness:** Error handling ensures the robustness of the code by preventing unexpected crashes and handling exceptional situations gracefully.
- **Debugging:** It facilitates debugging by providing detailed error messages and traceback information.

### Example:
```python
try:
    with Image.open(image_path) as image:
        # Process image
except (FileNotFoundError, OSError):
    sys.exit(f"Error: Unable to open image file '{image_path}'.")
```
## 4. Dynamic Typing and Duck Typing:

### Usage:
Python is dynamically typed, meaning variable types are inferred at runtime. Additionally, it follows the principle of duck typing, where the suitability of an object for a given task is determined by its behavior rather than its type.

### Advantages:
- **Flexibility:** Dynamic typing allows for flexibility in variable assignment and function parameter passing without explicit type declarations.
- **Simplified Syntax:** Duck typing simplifies code syntax by focusing on object behavior rather than type declarations.

### Example:
```python
def is_image_file(filename: str) -> bool:
    # Function definition with type hints

def compare_hashes(hash1: str, hash2: str) -> bool:
    # Function definition with type hints
```

Here, type hints `(str, bool)` provide information about the expected types of function parameters and return values, enhancing code clarity without affecting runtime behavior.

By leveraging these Python-specific syntax features and advantages, the image similarity finder achieves concise, readable, and robust code while benefiting from Python's dynamic nature and expressive syntax.
