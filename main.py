from pathlib import Path

DOWNLOADS_PATH = Path(r"C:\Users\..\Downloads")

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".csv", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".srt"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".bat", ".sh"]
}

def create_folders():
    for folder in FILE_CATEGORIES.keys():
        folder_path = DOWNLOADS_PATH / folder
        if not folder_path.exists():
            folder_path.mkdir()

def organize_files():
    for file in DOWNLOADS_PATH.iterdir():
        if file.is_file():  # Ignore directories
            for category, extensions in FILE_CATEGORIES.items():
                if file.suffix.lower() in extensions:
                    destination = DOWNLOADS_PATH / category
                    file.rename(destination / file.name)
                    break  # Stop checking once a match is found

if __name__ == "__main__":
    create_folders()
    organize_files()
    print("Downloads folder organized successfully!")