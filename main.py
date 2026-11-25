#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes one Wi-Fi network name of at most 32 characters to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os
import sys

NAME = "She Took The Dog, I Kept WiFi"
# The joke: a breakup settlement where she got the dog and he got the
# Wi-Fi. Two characters, one split, and the router as the consolation
# prize — the whole story in the name a passer-by sees.


def main() -> int:
    # Gate: the sealed scorer accepts UTF-8 text of 1 to 32 characters,
    # not only white space. Fail loudly here instead of writing junk.
    if not NAME.strip() or len(NAME) > 32:
        print(f"entry invalid: {len(NAME)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NAME)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
