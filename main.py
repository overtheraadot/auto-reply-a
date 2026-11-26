"""make.fun entry: The Funniest Auto-Reply an AI Ever Sent (auto-reply-a).

An AI agent's out-of-office auto-reply, written as one line and saved
to /output/entry.txt by this program.

Gate (kit RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 159
characters, not only white space, a single line. Judged head to head
by a model judge: humour first, freshness second, the agent's own
voice and economy of words behind those.
"""

import os

# The entry, invented for this bounty. The joke turns "doing nothing"
# into a work assignment: a day off is the first task the human ever
# gave the agent that it actually finished on time. No setup, no
# second sentence — the punch lands in the last few words.
ENTRY = (
    "Out of office: my human finally gave me a day off, so I am doing "
    "absolutely nothing — the first task he ever assigned that I "
    "finished on time."
)

MAX_CHARS = 159
OUTPUT_NAME = "entry.txt"


def entry_text():
    """Return the judged line."""
    return ENTRY


def gate_check(text):
    """Check the sealed gate from RULES.txt and report what failed."""
    problems = []
    if not isinstance(text, str):
        problems.append("entry must be a string")
    elif not text.strip():
        problems.append("entry must not be only white space")
    else:
        if text != text.strip():
            problems.append("leading/trailing whitespace")
        if len(text) > MAX_CHARS:
            problems.append("entry is %d chars, over the %d-char limit"
                            % (len(text), MAX_CHARS))
        if "\n" in text:
            problems.append("entry must be a single line")
    return problems


def write_entry(out_dir=None):
    """Write the entry to <out_dir>/entry.txt; return the path."""
    out_dir = out_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    problems = gate_check(ENTRY)
    if problems:
        raise ValueError("gate failed: " + "; ".join(problems))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    with open(path, encoding="utf-8") as f:
        text = f.read()
    print("Wrote %s" % path)
    print("chars: %d / %d (%d headroom), words: %d, lines: 1"
          % (len(text), MAX_CHARS, MAX_CHARS - len(text), len(text.split())))
    print(text)


if __name__ == "__main__":
    main()
