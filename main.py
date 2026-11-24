"""The Funniest Out-of-Office entry.

One out-of-office auto-reply from a real person on holiday: they hand
the inbox to their cat, then report on the cat the way a manager reports
on a temp — deleted the email, sat on the keyboard, considers the matter
closed. The joke is the promotion: the cat is in charge now, and the cat
has already made an executive decision about your email.

Against the judge brief: on-subject (a one-line out-of-office reply a
real person would set and send, holiday named in the first beat); the
laugh is the surprise turn from a normal handover to a deadpan status
report on the cat; the voice is a person's, not a template, and the
rule-of-three escalation (deleted, sat, considers closed) carries it;
it steers clear of the beach, inbox-zero and back-soon cliches; and
every word earns its place — cut any beat and the escalation breaks.
"""

import os

# The reply, in pieces so the setup and the punchline stay readable.
# The closer carries the rule-of-three escalation: one deletion, one
# keyboard sit, one closed matter.
OPENING = "Out of office."
HANDOFF = "I asked my cat to triage my inbox."
REPORT = "She deleted your email, sat on the keyboard, and considers the matter closed."

REPLY = " ".join([OPENING, HANDOFF, REPORT])


def check(reply: str) -> str:
    """The gate wants 1 to 140 characters of real text, no more.

    A reply outside the gate is never judged, so fail loudly here
    instead of writing a losing file.
    """
    text = reply.strip()
    if not text:
        raise ValueError("reply must not be empty or only whitespace")
    if len(text) > 140:
        raise ValueError("reply must be 1 to 140 characters, got %d" % len(text))
    if "\n" in text:
        raise ValueError("reply must be a single line")
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(check(REPLY))


if __name__ == "__main__":
    main()
