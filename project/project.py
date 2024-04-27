from PIL import Image
import imagehash
import os
import sys
import csv


def is_image_file(filename: str) -> bool:
    """
    Check if a file is an image based on its extension.

    Args:
    - filename (str): Name of the file.

    Returns:
    - is_image (bool): True if the file is an image, False otherwise.
    """
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", "webp")
    try:
        return filename.lower().endswith(image_extensions)
    except AttributeError:
        return False


def compare_hashes(hash1: str, hash2: str) -> bool:
    """
    Compare two image hashes and determine if they are similar.

    Args:
    - hash1 (str): Hash value of the first image.
    - hash2 (str): Hash value of the second image.

    Returns:
    - is_similar (bool): True if the images are similar, False otherwise.
    """
    try:
        return hash1 == hash2
    except (ValueError, TypeError):
        return False


def check_path(path: str, is_folder: bool = False) -> bool:
    """
    Check if the given path exists and if it is a folder or a file.

    Args:
    - path (str): The path to be checked.
    - is_folder (bool): If True, check if the path is a folder. If False, check if the path is a file.

    Returns:
    - is_valid (bool): True if the path exists and is of the specified type (file or folder), False otherwise.
    """
    try:
        if os.path.exists(path):
            if not is_folder and os.path.isfile(path):
                return True
            elif is_folder and os.path.isdir(path):
                return True
        return False
    except Exception as e:
        return False


def compute_hash(image_path: str, get_flipped_hash_too: bool = True):
    """
    Compute the hash value of an image.

    Args:
    - image_path (str): Path to the image file.
    - get_flipped_hash_too (bool): Whether to compute the hash of the flipped image as well.

    Returns:
    - hash_value (str) or tuple of hash_values: Hash value of the image (and flipped image).
    """
    try:
        with Image.open(image_path) as image:
            hash = str(imagehash.average_hash(image))
            if get_flipped_hash_too:
                image_flipped = image.transpose(Image.FLIP_LEFT_RIGHT)
                flipped_hash = str(imagehash.average_hash(image_flipped))

        if get_flipped_hash_too:
            return hash, flipped_hash
        return hash
    except (FileNotFoundError, OSError):
        sys.exit(f"Error: Unable to open image file '{image_path}'.")


def show_percentage_done(iterations_left: int, iterations_total: int):
    """
    Calculate and display the percentage completion of an iterative process.

    Args:
    - iterations_left (int): The number of iterations remaining in the process.
    - iterations_total (int): The total number of iterations in the process.
    """
    percent = ((iterations_total - iterations_left + 1) / iterations_total) * 100
    print(f"Percentage done: {percent:.2f}%", end="\r")


def find_similar_images_in_folder(ref_picture: str, folder_path: str) -> list[str]:
    """
    Find similar images to a reference image within a folder.

    Args:
    - ref_picture (str): Path to the reference image file.
    - folder_path (str): Path to the folder containing images.

    Returns:
    - similar_images (list): List of filenames of similar images.
    """
    similar_images = []
    try:
        ref_hash, ref_flipped_hash = compute_hash(ref_picture)
        list_files = os.listdir(folder_path)
        num_files = i = len(list_files)
        for filename in list_files:
            show_percentage_done(i, num_files)
            i -= 1
            if is_image_file(filename):
                image_path = os.path.join(folder_path, filename)
                try:
                    image_hash = compute_hash(image_path, False)

                    if compare_hashes(ref_hash, image_hash) or compare_hashes(
                        ref_flipped_hash, image_hash
                    ):
                        similar_images.append(filename)

                except (FileNotFoundError, OSError):
                    print(
                        f"Warning: Unable to open image file '{image_path}'. Skipping."
                    )
    except (FileNotFoundError, OSError):
        sys.exit(f"Error: Unable to access folder '{folder_path}'.")
    return similar_images


def get_user_input() -> tuple[str, str]:
    """
    Get user input for reference picture and folder path.

    Returns:
    - ref_picture (str): Path to the reference image file.
    - folder_path (str): Path to the folder containing images.
    """
    try:
        ref_picture = input("Enter the path to the reference image file: ")
        if not check_path(ref_picture, is_folder=False):
            sys.exit(f"Error: File '{ref_picture}' not found or is not a valid image.")

        folder_path = input("Enter the path to the folder containing images: ")
        if folder_path.endswith("/"):
            folder_path = folder_path[:-1]
        if not check_path(folder_path, is_folder=True):
            sys.exit(f"Error: Folder '{folder_path}' not found.")

        return ref_picture, folder_path

    except KeyboardInterrupt:
        sys.exit("\nUser interrupted the program.")
    except EOFError:
        sys.exit("\nCtrl + D detected. Exiting.")
    except Exception as e:
        sys.exit(f"An error occurred: {str(e)}")


def write_csv(similar_images: list[str]) -> None:
    """
    Write the list of similar images to a CSV file.

    Args:
    - similar_images (list): List of filenames of similar images.
    """
    with open("similar_images.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Filename"])
        for filename in similar_images:
            writer.writerow([filename])


def main() -> None:
    """
    Main function to run the image similarity finder.
    """
    ref_picture, folder_path = get_user_input()
    similar_images = find_similar_images_in_folder(ref_picture, folder_path)

    if not similar_images:
        print("No similar images found")
        exit()

    write_csv(similar_images)

    print("Similar images CSV file has been created.")


if __name__ == "__main__":
    main()
