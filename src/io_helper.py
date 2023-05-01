import os

import pyperclip
from PIL import ImageGrab

from virtual_disk import create_and_mount_virtual_disk


def is_text(content):
    return isinstance(content, str)


def save_text(content, filename):
    with open(filename, 'w') as f:
        f.write(content)


def save_image(content, filename):
    content.save(filename)


def save_clipboard_content(content, mount_path=None):
    if mount_path is None:
        mount_path = create_and_mount_virtual_disk()
    output_path = os.path.expanduser(f"{mount_path}/clipboard_content")

    if is_text(content):
        save_text(content, f"{output_path}.txt")
    else:
        try:
            save_image(content, f"{output_path}.png")
        except Exception as e:
            print(f"Error saving image: {e}")


def get_clipboard():
    content = ImageGrab.grabclipboard()
    if content is None:
        content = pyperclip.paste()
    return content
