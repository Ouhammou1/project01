import os



import os

base_path = '/Users/bouhammo/goinfre/m/data'  # Change to your main data directory if needed

for entry in os.listdir(base_path):
    full_path = os.path.join(base_path, entry)
    if os.path.isdir(full_path):
        files = [f for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f))]
        if len(files) > 200:
            files.sort()  # Sort to delete consistently (by name)
            to_delete = files[200:]  # Keep first 200, delete rest
            for f in to_delete:
                os.remove(os.path.join(full_path, f))
            print("Deleted {} file(s) from {}".format(len(to_delete), entry))
        else:
            print("Skipped {} ({} files)".format(entry, len(files)))


path = '/Users/bouhammo/goinfre/m/data'

for entry in os.listdir(path):
    full_path = os.path.join(path, entry)
    if os.path.isdir(full_path):
        # Count only files (not subdirectories)
        file_count = sum(
            1 for item in os.listdir(full_path)
            if os.path.isfile(os.path.join(full_path, item))
        )
        print(f"{entry}: {file_count} file(s)")

