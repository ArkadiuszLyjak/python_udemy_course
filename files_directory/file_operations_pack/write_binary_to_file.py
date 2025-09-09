import pickle
from pathlib import Path


def save_tuple_pickle(path: str, data_tuple: tuple) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("wb") as f:
        pickle.dump(data_tuple, f, protocol=pickle.HIGHEST_PROTOCOL)
    return p


def load_tuple_pickle(path: str) -> tuple:
    p = Path(path)

    if not p.exists() or p.stat().st_size == 0:
        raise FileNotFoundError(f"File {path} doesn't exist or is empty.")

    with p.open("rb") as f:
        return pickle.load(f)
