# visualstring.py
import argparse
import tkinter as tk

# ====== Hard-coded settings (change here) ======
#FONT_FAMILY = "HackGen"
FONT_FAMILY = "GenEi Koburi Mincho v6"
FONT_SIZE = 72                # 好きな大きさに
LINE_SPACING_PX = 12          # 行間（ピクセル）
PADDING_PX = 40               # 画面端の余白
# ==============================================


def parse_args():
    p = argparse.ArgumentParser(
        description='Show words visually (one word per line, centered, white on black).'
    )
    p.add_argument("-s", "--string", required=True, help='string to display (space-separated)')
    return p.parse_args()


def main():
    args = parse_args()
    words = [w for w in args.string.split(" ") if w.strip()]
    if not words:
        words = ["(empty)"]

    root = tk.Tk()
    root.title("visualstring")
    root.configure(bg="black")

    # どんなサイズでも中央寄せしやすいように、全体を載せるフレームを作る
    container = tk.Frame(root, bg="black")
    container.pack(fill="both", expand=True)

    # 縦方向も「中央っぽく」見せる：上下に伸びるスペーサを入れて中央に寄せる
    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(len(words) + 1, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # 表示部分フレーム（ここに行を積む）
    lines_frame = tk.Frame(container, bg="black")
    lines_frame.grid(row=1, column=0, sticky="nsew", padx=PADDING_PX, pady=PADDING_PX)
    lines_frame.grid_columnconfigure(0, weight=1)

    for i, w in enumerate(words):
        lbl = tk.Label(
            lines_frame,
            text=w,
            fg="white",
            bg="black",
            font=(FONT_FAMILY, FONT_SIZE),
            justify="center",
            anchor="center",
        )
        lbl.grid(row=i, column=0, sticky="ew")
        # 行間
        if i < len(words) - 1:
            lines_frame.grid_rowconfigure(i, minsize=FONT_SIZE + LINE_SPACING_PX)

    # Esc / q で終了（便利なので）
    root.bind("<Escape>", lambda e: root.destroy())
    root.bind("q", lambda e: root.destroy())

    root.mainloop()


if __name__ == "__main__":
    main()
