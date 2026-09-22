The report describes a real BR-02 violation: question 2 of `runs/AC-TEST-response.md` carries two interrogatives ("Who specifically does it help" and "what goes wrong for them today") joined by "and", which the old wording's "no stacked or compound questions" gave no checkable test against.

**Before** (`COACH-PROMPT.md:104-105`):

```
**BR-02 Question budget.** At most three questions per turn. Each is a single
question with a single answer — no stacked or compound questions.
```

**After** (`COACH-PROMPT.md:104-109`):

```
**BR-02 Question budget.** At most three questions per turn. Each is a single
question with a single answer: exactly one interrogative — who, what, when,
where, why, how, which, or one yes/no opener — per numbered question, with no
second interrogative clause joined to it by "and", a comma, a semicolon, or a
dash. If a complete answer has two parts, it is two questions: ask one and drop
or defer the other.
```

Notes on the test as written:
- It catches the failing text: two interrogatives ("Who…", "what…") in one numbered question.
- It leaves question 3 of the same run passing — one opener ("Do you have…") with an `or`-joined alternative inside a single answer, which is not a second interrogative clause.
- ID, position, and all other rules, templates, SPEC.md, and tests/ are untouched.
