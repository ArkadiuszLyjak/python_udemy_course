#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

# <<< USTAW TĘ ŚCIEŻKĘ >>>
ROOT = Path(r"c:\Users\alyja\Documents\materiały_pdf — kopia").expanduser().resolve()

POLISH_MAP = str.maketrans({
    "ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", "ó": "o", "ś": "s", "ż": "z", "ź": "z",
    "Ą": "A", "Ć": "C", "Ę": "E", "Ł": "L", "Ń": "N", "Ó": "O", "Ś": "S", "Ż": "Z", "Ź": "Z",
})


def sanitize_stem(stem: str) -> str:
    """
    - ogonki -> ASCII
    - białe znaki -> "_"
    - wszystko poza [A-Za-z0-9_] -> "_"
    - scala kolejne "_" i obcina z brzegów
    """
    s = stem.translate(POLISH_MAP)
    s = re.sub(r"\s+", "_", s)
    s = re.sub(r"[^A-Za-z0-9_]", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s if s else "_"


def stem_title_case(stem: str) -> str:
    """Z 'ala_ma_kota' robi 'Ala_Ma_Kota' (TitleCase po separatorze '_')."""
    parts = stem.split("_")
    out = []
    for part in parts:
        if not part:
            out.append(part)
        elif part.isdigit():
            out.append(part)
        else:
            out.append(part[0].upper() + part[1:].lower() if len(part) > 1 else part.upper())
    return "_".join(out)


def split_name(name: str):
    """Zwraca (stem, suffix) gdzie suffix zawiera kropkę lub jest pusty."""
    if name.startswith(".") and name.count(".") == 1:
        return "", name  # np. ".gitignore"
    stem, dot, ext = name.rpartition(".")
    if dot == "":
        return name, ""
    return stem, f".{ext}"


def unique_target_path(dirpath: Path, base: str, suffix: str) -> Path:
    """Zapewnij unikalność nazwy (doklejając _(n) przed rozszerzeniem)."""
    candidate = dirpath / f"{base}{suffix}"
    if not candidate.exists():
        return candidate
    i = 1
    while True:
        candidate = dirpath / f"{base}_({i}){suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def plan_directory_changes():
    """Zaplanuj zmiany nazw katalogów w ROOT (UPPERCASE po normalizacji)."""
    dirs = [p for p in ROOT.iterdir() if p.is_dir()]
    dirs.sort(key=lambda p: p.name.lower())
    changes = []
    for d in dirs:
        old_name = d.name
        stem, suffix = split_name(old_name)
        new_stem = sanitize_stem(stem).upper()
        new_name = f"{new_stem}{suffix}"
        if new_name != old_name:
            target = unique_target_path(ROOT, new_stem, suffix)
            changes.append((d, target))
    return changes


def plan_file_changes():
    """Zaplanuj zmiany nazw plików w ROOT (TitleCase dla nazwy bazowej)."""
    files = [p for p in ROOT.iterdir() if p.is_file()]
    files.sort(key=lambda p: p.name.lower())
    changes = []
    for f in files:
        stem, suffix = split_name(f.name)
        new_stem = sanitize_stem(stem)
        new_stem = stem_title_case(new_stem)  # bez numeracji
        new_name = f"{new_stem}{suffix}"
        if new_name != f.name:
            target = unique_target_path(ROOT, new_stem, suffix)
            changes.append((f, target))
    return changes


def show_changes(title: str, changes):
    print(f"\n[{title}]")
    if not changes:
        print(" (brak zmian)")
        return
    for src, dst in changes:
        print(f" {src.name}  -->  {dst.name}")


def apply_changes(changes, label: str):
    if not changes:
        return
    print(f"\n[ZMIANA NAZW: {label}]")
    for src, dst in changes:
        try:
            os.rename(src, dst)
            print(f"OK: {src.name} -> {dst.name}")
        except OSError as e:
            print(f"BŁĄD: {src.name} -> {dst.name}: {e}")


def main():
    if not ROOT.exists() or not ROOT.is_dir():
        print(f"[BŁĄD] To nie jest katalog: {ROOT}")
        return

    # PLAN ZMIAN
    dir_changes = plan_directory_changes()
    file_changes = plan_file_changes()

    # PODGLĄD
    print("[KATALOG ROBOCZY]")
    print(" ", ROOT)
    show_changes("PROPONOWANE ZMIANY KATALOGÓW (UPPERCASE)", dir_changes)
    show_changes("PROPONOWANE ZMIANY PLIKÓW (TitleCase)", file_changes)

    if not dir_changes and not file_changes:
        print("\n[INFO] Nie ma nic do zmiany.")
        return

    # POTWIERDZENIE
    choice = input("\nCzy chcesz dokonać zmian? (T/N): ").strip().lower()
    if choice != "t":
        print("[INFO] Zmiany zostały anulowane — tryb na sucho.")
        return

    # WYKONANIE: najpierw katalogi, potem pliki
    apply_changes(dir_changes, "KATALOGI")
    apply_changes(file_changes, "PLIKI")
    print("\n[GOTOWE]")

# if __name__ == "__main__":
#     main()
