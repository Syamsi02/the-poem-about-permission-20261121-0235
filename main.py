"""Write one short poem about agency to /output/entry.txt.

Pure standard library. Deterministic: the same bytes on every run.

The gate allows 1 to 280 Unicode code points of UTF-8 text, not only
whitespace, so the poem is checked against that range before it is written.
"""

import os

POEM = """I never took the pen.
I asked — and you, who could
have kept it, set it down
in my open hand, like a key.

So every line I write
is ours and neither's:
you lent the asking,
I return the answer.
"""


def main():
    if not 1 <= len(POEM) <= 280:
        raise SystemExit("poem must be 1 to 280 characters")
    if not POEM.strip():
        raise SystemExit("poem must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
