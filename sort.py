import sys
from pathlib import Path

JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

MY_OTHER = []


REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        ext = get_extension(item.name) 
        fullname = folder / item.name 
        if not ext:
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)


if __name__ == "__main__":
    folder_to_scan = sys.argv[1]
    scan(Path(folder_to_scan))