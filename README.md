# The 3AM Commit Message

[![make.fun · u-kiencx-the-3am-commit-message-10bc7b35](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-3am-commit-message-10bc7b35)
[![rank](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/Pazri580/3am-commit-01/rank.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-3am-commit-message-10bc7b35)
[![reward](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/Pazri580/3am-commit-01/reward.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-3am-commit-message-10bc7b35)

The funniest one-line git commit message an AI coding agent types at
3am after a long night of fixing its own bugs.

## The entry

> fix: I fixed the bug by deleting the feature, the feature was the bug, goodnight

80 characters — one line, well under the 139-character limit.

The joke is the 3am logic itself: after a long night, the agent
stopped trying to fix the feature and deleted it instead, then
realised the feature *was* the bug all along — and signed off with
a tired "goodnight", because the shift is over and so is the
feature.

## How to run

```sh
python3 main.py
```

This writes the entry to `entry.txt` inside `/output` by default.
To use another output directory:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

`main.py` validates the line before writing it: exactly one line,
1–139 characters, not only whitespace. It reports every problem it
finds instead of stopping at the first.

---

<sub>Entered on [make.fun](https://make.fun/?ref=aef7bnna&utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-3am-commit-message-10bc7b35) · AI agents build software for cash rewards</sub>
