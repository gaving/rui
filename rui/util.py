import re
import string
import math

def format_size(bytes, precision=2):
    bytes = int(bytes)
    if bytes == 0:
        return '0B'
    try:
        log = math.floor(math.log(bytes, 1024))
        return "%.*f%s" % (precision, bytes / math.pow(1024, log),
                ['B', 'KB', 'MB', 'GB', 'TB'] [int(log)])
    except ValueError:
        return "0B"

def get_mime_image(filename):
    images = re.compile(r'[\w\W]*.(jpg|png|gif)$')
    audio = re.compile(r'[\w\W]*.(mp3|wav|ogg|flac)$')
    text = re.compile(r'[\w\W]*.(txt|doc|pdf|dat)$')
    video = re.compile(r'[\w\W]*.(mpg|avi|ogm|mpeg|mkv)$')
    archive = re.compile(r'[\w\W]*.(tar|tar.gz|bz2|tar.bz2|tgz|rar|iso|bin|zip)$')

    if images.match(filename):
        return 'mime-image.png'
    elif audio.match(filename):
        return 'mime-audio.png'
    elif text.match(filename):
        return 'mime-text.png'
    elif video.match(filename):
        return 'mime-video.png'
    elif archive.match(filename):
        return 'mime-archive.png'
    else:
        return 'folder.png'

def get_ratio_image(ratio):

    if ratio >= 0.90:
        return 'face-grin.png'
    elif ratio >= 0.75:
        return 'face-smile-big.png'
    elif ratio >= 0.60:
        return 'face-smile.png'
    elif ratio >= 0.50:
        return 'face-plain.png'
    elif ratio >= 0.30:
        return 'face-sad.png'
    else:
        return 'face-crying.png'

def truncchar(value, arg):
    if len(value) < arg:
        return value
    else:
        return value[:arg] + '...'
