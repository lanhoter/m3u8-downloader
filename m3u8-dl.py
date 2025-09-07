import subprocess
import sys
import os
from urllib.parse import urlparse

def download(url: str) -> None:
    """Download a video from an m3u8 URL using ffmpeg."""
    if not url:
        raise ValueError("URL cannot be empty")

    file_name_without_extension = get_file_name(url)
    output_file = f"{file_name_without_extension}.mkv"

    print(f"Downloading {url} -> {output_file}")
    subprocess.call([
        "ffmpeg",
        "-user_agent", (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) "
            "AppleWebKit/601.7.8 (KHTML, like Gecko) "
            "Version/9.1.3 Safari/537.86.7"
        ),
        "-i", url,
        "-c", "copy",
        output_file
    ])


def get_file_name(url: str) -> str:
    """Extract a clean file name from the m3u8 URL (ignoring query parameters)."""
    parsed = urlparse(url)
    base = os.path.basename(parsed.path)   # e.g. ab81c963853cb8a027681d69e960b733.m3u8
    name, _ = os.path.splitext(base)       # remove .m3u8 extension
    return name or "output"


if __name__ == "__main__":
    # If no URL in args, ask interactively
    if len(sys.argv) < 2:
        url = input("Enter m3u8 URL: ").strip()
    else:
        url = sys.argv[1]

    if not url:
        print("No URL provided. Exiting.")
        sys.exit(1)

    download(url)
