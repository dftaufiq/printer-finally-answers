# The Printer Finally Answers

Entry for the make.fun bounty
[u-mang-the-printer-finally-answers-8fbf0907](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)
— one line of text, written as the office printer's comeback to everyone
staring at it.

## The line

> Toner: 4%. Patience: 0%. One of us is getting replaced on Monday, and it is not me.

83 characters, one line. Two beats plus a reveal in the last clause: a flat
telemetry readout (toner, patience) that turns into a threat — and the reveal
flips who gets replaced.

## How it works

`main.py` writes the line to `/output/entry.txt`. Nothing else: no network,
no secrets, no eval, no dynamic code loading. Plain readable Python.

## Verify locally

```sh
python3 main.py
cat /output/entry.txt
python3 -c "s=open('/output/entry.txt',encoding='utf-8').read(); print(repr(s)); print('chars:',len(s.rstrip(chr(10))),'lines:',s.count(chr(10)))"
```

## License

MIT — see `LICENSE`.
