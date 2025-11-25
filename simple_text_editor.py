#!/usr/bin/env python3
"""
Простой консольный текстовый редактор.
Команды:
  new <filename>    - создать/открыть файл (перезаписать)
  open <filename>   - открыть файл (чтение)
  append <filename> - добавить текст в конец файла
  show <filename>   - показать содержимое
  find <filename> <substr> - найти подстроку (печатает номера строк)
  exit              - выйти
"""
import sys
import os

def cmd_new(fn):
    with open(fn, "w", encoding="utf-8") as f:
        print(f"Файл {fn} создан/очищен.")

def cmd_open(fn):
    if not os.path.exists(fn):
        print("Файл не найден.")
        return
    with open(fn, "r", encoding="utf-8") as f:
        print(f.read())

def cmd_append(fn):
    print("Вводите строки. По отдельной строке с '.' сохраняется и выходит.")
    if not os.path.exists(fn):
        open(fn, "w", encoding="utf-8").close()
    with open(fn, "a", encoding="utf-8") as f:
        while True:
            line = input()
            if line == ".":
                break
            f.write(line + "\n")
    print("Сохранено.")

def cmd_show(fn):
    cmd_open(fn)

def cmd_find(fn, substr):
    if not os.path.exists(fn):
        print("Файл не найден.")
        return
    with open(fn, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if substr in line:
                print(f"{i}: {line.rstrip()}")

def repl():
    print("Простой текстовый редактор. help для списка команд.")
    while True:
        try:
            s = input(">> ").strip()
        except EOFError:
            break
        if not s:
            continue
        parts = s.split(maxsplit=2)
        cmd = parts[0].lower()
        if cmd == "exit":
            break
        if cmd == "help":
            print(__doc__)
            continue
        if cmd == "new" and len(parts) >= 2:
            cmd_new(parts[1])
        elif cmd == "open" and len(parts) >= 2:
            cmd_open(parts[1])
        elif cmd == "append" and len(parts) >= 2:
            cmd_append(parts[1])
        elif cmd == "show" and len(parts) >= 2:
            cmd_show(parts[1])
        elif cmd == "find" and len(parts) >= 3:
            cmd_find(parts[1], parts[2])
        else:
            print("Неизвестная команда. help для списка.")

if __name__ == "__main__":
    repl()
