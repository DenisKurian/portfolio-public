from pdf2image import convert_from_path
from django.core.files.base import ContentFile
from django.conf import settings
from pathlib import Path
from io import BytesIO

def generate_thumbnail(pdf_path):
    try:
        path = Path(pdf_path).resolve()  # ✅ use clean, resolved Path object

        print(f"[DEBUG] Trying to generate thumbnail from: {path}")
        print(f"[DEBUG] Poppler path: {settings.PDF2IMAGE_POPPLER_PATH}")

        images = convert_from_path(
            pdf_path = str(Path(pdf_path).resolve()),
            first_page=1,
            fmt='jpeg',
            size=(600, None),
            poppler_path=settings.PDF2IMAGE_POPPLER_PATH
        )

        if not images:
            print("[Thumbnail Error] No image returned from convert_from_path")
            return None

        thumb_io = BytesIO()
        images[0].save(thumb_io, format='JPEG')
        return ContentFile(thumb_io.getvalue(), name='thumb.jpg')

    except Exception as e:
        print(f"[Thumbnail Error] {e}")
        return None
