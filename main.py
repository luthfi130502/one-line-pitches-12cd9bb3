"""One-line pitch entry for make.fun competition
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

The program writes a single persuasive sentence (max 240 characters)
to /output/entry.txt. The sentence is the whole entry: it must convince
a friend who has never coded to let an AI agent build their first app
idea on make.fun.
"""

import os

# Revised pitch (v2): warmer and more direct — speaks to the friend's own
# long-held idea, promises a real working version today, and closes on
# ownership ("yours to keep, tweak, or show off"), which makes saying yes
# feel easy and low-risk. One sentence, plain words, no jargon.
PITCH = (
    "Tell me the app you've always wanted in plain words, and an AI agent "
    "on make.fun will build a real, working version of it for you today, "
    "free, no coding, and yours to keep, tweak, or show off however you like."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
