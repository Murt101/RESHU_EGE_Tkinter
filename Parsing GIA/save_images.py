import subprocess
import os


def svg_to_png(svg_path, png_path, dpi=200):
    resvg_exe = os.path.join(os.path.dirname(__file__), "resvg.exe")
    if not os.path.exists(resvg_exe):
        raise FileNotFoundError("resvg.exe не найден. Скачайте его с https://github.com/RazrFalcon/resvg/releases")

    zoom = dpi / 96.0
    cmd = [resvg_exe, "--zoom", str(zoom), svg_path, png_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Ошибка resvg: {result.stderr}")
    print(f"SVG сохранён как PNG: {png_path}")




# Пример:
svg_to_png("27.svg", "temp.png", dpi=200)
