# list_fonts.py
from __future__ import annotations

import argparse
from collections import defaultdict

def main() -> None:
    ap = argparse.ArgumentParser(description="List installed font family names")
    ap.add_argument("--show-path", action="store_true", help="also show font file paths")
    ap.add_argument("--contains", default="", help="filter: substring (case-insensitive)")
    args = ap.parse_args()

    try:
        from matplotlib import font_manager
    except Exception as e:
        raise SystemExit(
            "matplotlib が必要です。未導入なら: pip install matplotlib\n"
            f"Import error: {e}"
        )

    # ttf/otf を中心に拾う（必要なら afm なども追加可）
    font_files = set(font_manager.findSystemFonts(fontext="ttf") +
                     font_manager.findSystemFonts(fontext="otf"))

    fam_to_paths: dict[str, set[str]] = defaultdict(set)

    for path in sorted(font_files):
        try:
            # font file -> FontProperties -> family name
            prop = font_manager.FontProperties(fname=path)
            fam = prop.get_name()  # 例: "Yu Gothic", "Meiryo", ...
            if fam:
                fam_to_paths[fam].add(path)
        except Exception:
            # 壊れたフォント等はスキップ
            continue

    # フィルタ
    needle = args.contains.lower().strip()
    families = sorted(fam_to_paths.keys(), key=lambda s: s.lower())
    if needle:
        families = [f for f in families if needle in f.lower()]

    # 出力
    for fam in families:
        if not args.show_path:
            print(fam)
        else:
            print(fam)
            for p in sorted(fam_to_paths[fam]):
                print(f"  {p}")

if __name__ == "__main__":
    main()
