import glob
import hashlib
import os
import shutil
import time
import uuid
from datetime import datetime


def get_image_hash(path):
    with open(path, 'rb') as file:
        image_hash = hashlib.md5(file.read()).hexdigest()
    return image_hash


def copy_images(src_root, dest_root, verbose=True):
    src_paths = []
    image_hashes = []
    duplicate_count = 0
    dir_count = 0

    # Get image hashes already in dest
    for filename in glob.iglob(dest_root + '/**/*', recursive=True):
        path = os.path.abspath(filename)
        if not os.path.isdir(path):
            image_hash = get_image_hash(path)
            if image_hash not in image_hashes:
                image_hashes.append(image_hash)

    if verbose:
        print(f'LOG: Found {len(image_hashes)} unique images already in dest_root')

    # Get all unique images from src that are not already in dest
    for filename in glob.iglob(src_root + '/**/*', recursive=True):
        path = os.path.abspath(filename)
        if not os.path.isdir(path):
            ext = os.path.splitext(path)[1]
            IMAGE_EXTS = [
                '.jpg', '.avi', '.jpeg', '.mov', '.png',
                '.gif', '.tif', '.tiff', '.heic', '.svg',
                '.webp', '.raw', '.bmp', '.heif'
            ]
            if ext.lower() not in IMAGE_EXTS:
                continue

            image_hash = get_image_hash(path)
            if image_hash not in image_hashes:
                src_paths.append(path)
                image_hashes.append(image_hash)
            else:
                duplicate_count += 1
        else:
            dir_count += 1

    if verbose:
        print(f'LOG: Found {len(src_paths)} unique images in src_root')
        print(f'LOG: Found {duplicate_count} duplicate images in src_root')
        print(f'LOG: Found {dir_count} subdirectories in src_root')

    if not os.path.exists(dest_root):
        os.mkdir(dest_root)

    for src_path in src_paths:
        ext = os.path.splitext(src_path)[1]
        timestamp = int(os.path.getmtime(src_path))
        date = datetime.fromtimestamp(timestamp).strftime('%Y%m%d%H%M%S-')
        dest_path = os.path.join(dest_root, f'{date}' + str(uuid.uuid4()) + ext)
        shutil.copy2(src_path, dest_path)

    if verbose:
        print(f'LOG: Copied {len(src_paths)} images to dest_root')


if __name__ == '__main__':
    start = time.time()
    SRC_ROOT = os.path.join('test')
    DEST_ROOT = os.path.join('dest')
    copy_images(SRC_ROOT, DEST_ROOT)
    end = int(time.time() - start) / 60
    print(f'--- {round(end, 2)}m ---')
