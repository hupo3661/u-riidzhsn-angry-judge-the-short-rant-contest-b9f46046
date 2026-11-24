# Angry Judge: The Short Rant Contest — Entry

[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/hupo3661/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/hupo3661/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

A tiny Python program that writes one short, funny rant to `/output/entry.txt`.

## The rant

The target is the supermarket self-checkout: a machine with one job that
still calls for help constantly, flags the very item it told you to scan as
"unexpected", and makes a human approve your bananas like contraband. You came
in for milk; you leave as an unpaid employee managed by a beeping robot.

The text is 316 characters — inside the contest's 1–400 character limit.

## Run

```bash
python3 main.py
```

This creates `/output/entry.txt` (UTF-8) containing exactly the rant text.
`validate()` checks the text is 1–400 characters and not only whitespace
before anything is written.

## License

MIT — see `LICENSE`.
