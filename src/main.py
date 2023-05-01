import time

from io_helper import get_clipboard, save_clipboard_content
from virtual_disk import create_and_mount_virtual_disk


def main():
    mount_path = create_and_mount_virtual_disk()
    previous_clipboard_content = get_clipboard()

    while True:
        current_clipboard_content = get_clipboard()

        if (
                (type(current_clipboard_content) != type(previous_clipboard_content))
                or
                (current_clipboard_content != previous_clipboard_content)
        ):
            save_clipboard_content(current_clipboard_content,
                                   mount_path=mount_path)
            previous_clipboard_content = current_clipboard_content

        time.sleep(1)


if __name__ == "__main__":
    main()
