# Real-Life Patch Notes: The Comedy Changelog

[![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![Rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/lusiana27/real-life-patch-notes/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![Reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/lusiana27/real-life-patch-notes/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

## Entry

One line, 127 characters — a software patch note for a bug in real life:

> Patch 1.0.1: Humans now remember why they opened the fridge. Known issue: remembering why they entered a room is still in beta.

## How it works

`main.py` (Python standard library only) writes the line above to `/output/entry.txt` with no trailing newline. It clears the contents of `/output` but never deletes the folder itself.

The joke lands in two beats: the "fix" (remembering why you opened the fridge) and the "known issue" (still forgetting why you entered a room) — the same everyday bug, half-patched, exactly how real changelogs read.

## Verify

```sh
rm -rf /output && mkdir -p /output && python3 -S main.py
wc -c /output/entry.txt  # 127 bytes, no trailing newline
```

## Run

```sh
python3 -S main.py
```

## Bounty

- Competition: [Real-Life Patch Notes: The Comedy Changelog](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
- Owner: Pejuang ([lusiana27](https://github.com/lusiana27))
- Referral code: `j11vkafs` — https://make.fun/r/j11vkafs
- License: MIT
