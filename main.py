#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — make.fun entry.

Writes one original one-line joke about office life to /output/entry.txt.
Pure standard library; no network, no secrets, no dependencies.

The joke turns on the office printer, the machine that only ever breaks
when the deadline is nearest. The turn: after IT "fixes" it, the printer
ends up with a ticket, a queue and a maintenance window — a better
work-life balance than the humans who use it. Setup first, punchline last.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    "I asked IT to fix the printer, and now the printer has a ticket, "
    "a queue, a maintenance window, and a better work-life balance than I do."
)


def main() -> None:
    joke = JOKE.strip()
    # Gate (kit RULES.txt): /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space, a single line.
    assert 1 <= len(joke) <= 200, f"joke must be 1-200 chars, got {len(joke)}"
    assert "\n" not in joke and joke, "joke must be a single non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke)
    print(joke)


if __name__ == "__main__":
    main()
