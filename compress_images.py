"""
compress_images.py
------------------
Compresses all images in the Files/ folder in-place.
- JPEGs → quality 75 (good visual quality, ~60-80% smaller)
- PNGs  → optimized + converted to web-friendly size
- GIFs  → skipped (lossless; re-encoding can break animation)
- Originals are backed up to Files/_originals/ before overwriting.
"""

import os
import shutil
from pathlib import Path
from PIL import Image

# --- Config ---
FILES_DIR = Path(r"c:\Users\Dell\Documents\AntiG Proj\Portfolio\Files")
BACKUP_DIR = FILES_DIR / "_originals"
JPEG_QUALITY = 75      # 1-95; 75 is a great balance
PNG_MAX_SIZE = (2048, 2048)  # Downscale very large PNGs to fit within this box
JPEG_MAX_SIZE = (2048, 2048)

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}
SKIP_EXTS  = {".gif"}  # Animated GIFs lose frames on re-save — skip them

# --- Helpers ---
def backup(src: Path):
    """Copy original to backup dir, preserving subfolder structure."""
    rel = src.relative_to(FILES_DIR)
    dst = BACKUP_DIR / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not dst.exists():          # Don't overwrite an already-backed-up original
        shutil.copy2(src, dst)

def human(bytes_: int) -> str:
    return f"{bytes_ / 1024:.0f} KB" if bytes_ < 1_048_576 else f"{bytes_ / 1_048_576:.2f} MB"

def compress(path: Path):
    ext = path.suffix.lower()

    if ext in SKIP_EXTS:
        print(f"  SKIP  {str(path.relative_to(FILES_DIR))}  (GIF - skipped to preserve animation)")
        return

    if ext not in IMAGE_EXTS:
        return

    size_before = path.stat().st_size
    backup(path)

    try:
        img = Image.open(path)

        if ext in {".jpg", ".jpeg"}:
            # Convert palette/RGBA → RGB for JPEG
            if img.mode in ("RGBA", "P", "LA"):
                img = img.convert("RGB")
            img.thumbnail(JPEG_MAX_SIZE, Image.LANCZOS)
            img.save(path, "JPEG", quality=JPEG_QUALITY, optimize=True)

        elif ext == ".png":
            if img.mode == "P":
                img = img.convert("RGBA")
            img.thumbnail(PNG_MAX_SIZE, Image.LANCZOS)
            img.save(path, "PNG", optimize=True)

        elif ext == ".webp":
            img.thumbnail(JPEG_MAX_SIZE, Image.LANCZOS)
            img.save(path, "WEBP", quality=JPEG_QUALITY, method=6)

        else:
            # bmp / tiff → convert to JPEG
            if img.mode in ("RGBA", "P", "LA"):
                img = img.convert("RGB")
            new_path = path.with_suffix(".jpg")
            img.thumbnail(JPEG_MAX_SIZE, Image.LANCZOS)
            img.save(new_path, "JPEG", quality=JPEG_QUALITY, optimize=True)
            path.unlink()
            path = new_path

        size_after = path.stat().st_size
        saved = size_before - size_after
        pct = (saved / size_before) * 100 if size_before else 0
        rel = str(path.relative_to(FILES_DIR))
        print(f"  OK    {rel:<55}  {human(size_before):>10} -> {human(size_after):>10}  (saved {pct:.0f}%)")

    except Exception as e:
        print(f"  ERROR {str(path.relative_to(FILES_DIR))}: {e}")

# --- Main ---
def main():
    images = [p for p in FILES_DIR.rglob("*") if p.suffix.lower() in IMAGE_EXTS | SKIP_EXTS
              and "_originals" not in p.parts]

    total_before = sum(p.stat().st_size for p in images)
    print(f"\nFound {len(images)} image files  ({human(total_before)} total)\n")
    print(f"Backing up originals to: {BACKUP_DIR}\n")

    for img in sorted(images):
        compress(img)

    images_after = [p for p in FILES_DIR.rglob("*") if p.suffix.lower() in IMAGE_EXTS | SKIP_EXTS
                    and "_originals" not in p.parts]
    total_after = sum(p.stat().st_size for p in images_after)

    print(f"\n{'='*70}")
    print(f"  Before : {human(total_before)}")
    print(f"  After  : {human(total_after)}")
    print(f"  Saved  : {human(total_before - total_after)}  ({(total_before - total_after)/total_before*100:.1f}%)")
    print(f"{'='*70}\n")
    print("Originals safely stored in Files/_originals/  — delete if no longer needed.")

if __name__ == "__main__":
    main()
