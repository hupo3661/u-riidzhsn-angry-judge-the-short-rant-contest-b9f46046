# Angry Judge: The Short Rant Contest — Entry

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
