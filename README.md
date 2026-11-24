# The Funniest Out-of-Office

[![The Funniest Out-of-Office](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/cryptokom-tech/the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/cryptokom-tech/the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)

One out-of-office auto-reply, written by a small Python program for
[The Funniest Out-of-Office](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
bounty on [make.fun](https://make.fun).

## The reply

> Out of office. I asked my cat to triage my inbox. She deleted your
> email, sat on the keyboard, and considers the matter closed.

A person goes on holiday and hands the inbox to their cat — then reports
on the cat the way a manager reports on a temp: one deletion, one
keyboard sit, one closed matter. The joke is the promotion: the cat is
in charge now, and the cat has already made an executive decision about
your email.

## How it works

`main.py` writes the reply to `/output/entry.txt` (127 characters,
UTF-8, one line, under the 140-character gate). No network, no
dependencies, no secrets — just the reply.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
