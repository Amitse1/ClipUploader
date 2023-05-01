import os
import re
import subprocess


def create_virtual_disk(size, path):
    try:
        subprocess.run(["hdiutil", "create", "-size", f"{size}m", "-fs", "HFS+", "-volname", "Clipboard", path],
                       check=True)
        print(f"Virtual disk created at {path}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual disk: {e}")


def mount_virtual_disk(path):
    try:
        result = subprocess.run(["hdiutil", "attach", path], check=True, capture_output=True, text=True)
        mount_path = extract_mount_path(result.stdout)
        print(f"Virtual disk mounted at {mount_path}")
        return mount_path
    except subprocess.CalledProcessError as e:
        print(f"Error mounting virtual disk: {e}")


def extract_mount_path(output):
    pattern = r'/Volumes/[\w\s-]+'
    match = re.search(pattern, output)
    if match:
        return match.group(0).rstrip()
    else:
        raise ValueError("Failed to find the mount path in the output")


def create_and_mount_virtual_disk():
    size = 10  # Size of the virtual disk in megabytes
    output_path = os.path.expanduser("~/Desktop/clipboard.dmg")

    create_virtual_disk(size, output_path)
    return mount_virtual_disk(output_path)


if __name__ == "__main__":
    create_and_mount_virtual_disk()
