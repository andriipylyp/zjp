"""
Skript na spúšťanie testov pre vybraný týždeň.
Použitie: python scripts/run_tests.py --week 01
"""
import argparse
import os
import sys
import unittest


def normalize_week(value):
    text = value.strip().lower()
    if text.startswith("week"):
        text = text[4:]
    if not text.isdigit():
        raise ValueError("Neplatný formát týždňa.")
    num = int(text)
    if num < 1 or num > 10:
        raise ValueError("Týždeň musí byť v rozsahu 01-10.")
    return f"week{num:02d}"


def main():
    parser = argparse.ArgumentParser(description="Spustenie testov pre vybraný týždeň.")
    parser.add_argument("--week", required=True, help="Číslo týždňa, napr. 01")
    args = parser.parse_args()

    try:
        week = normalize_week(args.week)
    except ValueError as exc:
        print(f"Chyba: {exc}")
        return 2

    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if root not in sys.path:
        sys.path.insert(0, root)

    tests_dir = os.path.join(root, "tests", week)
    if not os.path.isdir(tests_dir):
        print(f"Chyba: Neexistuje adresár testov pre {week}.")
        return 2

    suite = unittest.defaultTestLoader.discover(start_dir=tests_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    failed = len(result.failures) + len(result.errors)
    passed = result.testsRun - failed - len(result.skipped)
    print(f"Zhrnutie: úspešné {passed}, neúspešné {failed}, spolu {result.testsRun}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
