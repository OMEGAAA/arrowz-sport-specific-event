"""Web用に写真を最適化するスクリプト。

- 入力: レポート用写真-原本/ (オリジナル, 高解像度)
- 出力: レポート用写真/ (Web用, リサイズ+圧縮)
- 仕様: 横最大1920px / JPEG quality 82 / プログレッシブ / EXIF除去
"""
import os
import sys
from PIL import Image, ImageOps

SRC = "レポート用写真-原本"
DST = "レポート用写真"
MAX_WIDTH = 1920
QUALITY = 82


def main():
    os.makedirs(DST, exist_ok=True)
    files = sorted(f for f in os.listdir(SRC)
                   if f.lower().endswith((".jpg", ".jpeg", ".png")))
    total = len(files)
    total_orig = 0
    total_new = 0

    for i, fname in enumerate(files, 1):
        src_path = os.path.join(SRC, fname)
        # Always save as .jpeg (preserving original extension form)
        dst_path = os.path.join(DST, fname)

        orig_size = os.path.getsize(src_path)
        total_orig += orig_size

        with Image.open(src_path) as img:
            # Honor EXIF orientation, then drop EXIF
            img = ImageOps.exif_transpose(img)
            if img.width > MAX_WIDTH:
                ratio = MAX_WIDTH / img.width
                new_h = int(round(img.height * ratio))
                img = img.resize((MAX_WIDTH, new_h), Image.LANCZOS)
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(dst_path, "JPEG",
                     quality=QUALITY, optimize=True, progressive=True)

        new_size = os.path.getsize(dst_path)
        total_new += new_size

        if i % 10 == 0 or i == total:
            pct = 100 * new_size / orig_size if orig_size else 0
            print(f"[{i:3d}/{total}] {fname}: "
                  f"{orig_size//1024:>6d}KB -> {new_size//1024:>5d}KB ({pct:.0f}%)")

    mb_orig = total_orig / (1024 * 1024)
    mb_new = total_new / (1024 * 1024)
    saved = 100 * (1 - total_new / total_orig) if total_orig else 0
    print(f"\nTotal: {mb_orig:.1f}MB -> {mb_new:.1f}MB ({saved:.1f}% smaller)")


if __name__ == "__main__":
    main()
