from pathlib import Path


def write_string_to_file(directory_path, string_to_write,
                         prefix="test_", ext=".txt", start=0, zero_pad=2):
    d = Path(directory_path)
    d.mkdir(parents=True, exist_ok=True)

    n = start
    while True:
        name = f"{prefix}{n:0{zero_pad}d}{ext}" if zero_pad else f"{prefix}{n}{ext}"
        p = d / name
        if not p.exists():
            break
        n += 1

    p.write_text(string_to_write, encoding="utf-8")
    return str(p)
