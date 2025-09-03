# ZASADA: natychmiast kończy proces z kodem wyjścia; NIE wywołuje atexit, nie flushuje buforów.
# Użycie awaryjne, np. w potomstwie po fork.
import os, sys
import tempfile

# print("Przed _exit")
# os._exit(0)  # ⚠️ ODKOMENTUJ, aby zobaczyć, że linia poniżej się nie wykona.
# print("Po _exit (zobaczysz tylko gdy wywołanie jest zakomentowane)")


# ZASADA: natychmiastowy abort procesu (zwykle core dump na POSIX). Na Windows zakończy proces z błędem.
# import os
# os.abort()  # ⚠️ ODKOMENTUJ tylko świadomie
# print("abort nie został wywołany")

p = tempfile.NamedTemporaryFile()
print("istnieje?", os.access(p.name, os.F_OK))
