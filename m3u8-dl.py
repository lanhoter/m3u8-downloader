import subprocess
import sys

def download(link):
    file_name_without_extension = get_file_name(link)
    subprocess.call(
        ["ffmpeg",
         "-user_agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
         "-i", link,
         "-c", "copy",
         file_name_without_extension + ".mkv"])


def get_file_name(link):
    Segments = link.rpartition('//m3u8')
    subSegments = Segments[2].rpartition('.m3u8')
    lowSegments = subSegments[0].rpartition('/')
    return lowSegments[2]


if __name__ == '__main__':
    if sys.argv[1] != '' and len(sys.argv) > 1:
        Dlink = sys.argv[1]
        download(Dlink)
