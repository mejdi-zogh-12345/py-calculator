"""Simple command-line to-do list app.

Usage:
    python todo.py add "Buy milk"
    python todo.py list
    python todo.py done 1
    python todo.py remove 1
"""

import json
import os
import sys

TASKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, text):
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f"Added: {text}")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['text']}")


def complete_task(tasks, index):
    if index < 1 or index > len(tasks):
        print(f"No task numbered {index}.")
        return
    tasks[index - 1]["done"] = True
    save_tasks(tasks)
    print(f"Completed: {tasks[index - 1]['text']}")


def remove_task(tasks, index):
    if index < 1 or index > len(tasks):
        print(f"No task numbered {index}.")
        return
    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"Removed: {removed['text']}")


def print_usage():
    print(__doc__)


def main(argv):
    if len(argv) < 2:
        print_usage()
        return

    command = argv[1]
    tasks = load_tasks()

    if command == "add" and len(argv) >= 3:
        add_task(tasks, " ".join(argv[2:]))
    elif command == "list":
        list_tasks(tasks)
    elif command == "done" and len(argv) == 3:
        complete_task(tasks, int(argv[2]))
    elif command == "remove" and len(argv) == 3:
        remove_task(tasks, int(argv[2]))
    else:
        print_usage()


if __name__ == "__main__":
    main(sys.argv)
