# Contributing to Eukalyptus

Français : [CONTRIBUTING.md](CONTRIBUTING.md) · English

Thank you for your interest. Eukalyptus is **free, closed-source software**: this repository does not contain its source code, so there
are no code pull requests. It exists to collect your **feedback** and to publish what can be published: the documentation and the
language files. Here is what you can do, and how.

You can write in English everywhere: issues, discussions and pull requests. French is the default language of this repository.

Before taking part, please read the [code of conduct](CODE_OF_CONDUCT.md).

## Contents

- [Report a bug](#report-a-bug)
- [Suggest an idea](#suggest-an-idea)
- [Ask a question](#ask-a-question)
- [Fix the documentation](#fix-the-documentation)
- [Translate the app](#translate-the-app)
- [Report a security vulnerability](#report-a-security-vulnerability)
- [What is not accepted](#what-is-not-accepted)

## Report a bug

1. **Update the app**: the bug may already be fixed. Versions are listed in the [changelog](CHANGELOG.md) (notes in French).
2. **Search the [issues](https://github.com/ant-rdg/eukalyptus/issues)** (open and closed): if the problem already exists, add a 👍 and,
   if you have an extra detail, a comment.
3. Otherwise, **[open an issue](https://github.com/ant-rdg/eukalyptus/issues/new?template=bug.yml)** with the "Bug" form. Please include:
   - **The Eukalyptus version**: Settings › Credits › About (on Mac, also the Eukalyptus menu › About Eukalyptus).
   - **Your system**: macOS version (Apple menu › About This Mac) or Windows version (Settings › System › About), and the processor type.
   - **The steps to reproduce** the problem, one per line.
   - **What you expected**, and **what happened** (the exact error message, a screenshot if it helps).
   - **The kind of server** involved when relevant (Linux, Windows, NAS, OpenSSH version…).
4. **Hide sensitive information** before posting: passwords, keys, tokens, private IP addresses and server names. An issue is public.

One issue = one problem. If you have several, open several.

## Suggest an idea

Ideas are discussed in **[Discussions, "Idées" category](https://github.com/ant-rdg/eukalyptus/discussions/new?category=idees)**, not in
issues.

- **Search first** for a similar idea: vote with 👍 instead of opening a duplicate. Votes help choose what comes next.
- **Describe the need before the solution**: what you are trying to do, what gets in your way today, with what kind of server or
  workflow. An idea with its context is far more useful than a feature requested alone.
- Check the [roadmap](ROADMAP.md): the idea may already be there.

Suggesting an idea does not oblige the author to build it, and no date is promised.

## Ask a question

A question about usage, setup or compatibility: **[Discussions, "Questions" category](https://github.com/ant-rdg/eukalyptus/discussions/new?category=questions)**.
Have a look at the [guides](README.en.md#guides) first: the answer may be there. For a question about an Eukalyptus+ purchase or your
personal data, write to contact@eukalyptus.app rather than in public.

## Fix the documentation

The guides are in [`docs/en/`](docs/en/) (English) and [`docs/fr/`](docs/fr/) (French). A typo, a wrong command, information that is no
longer true, a confusing explanation: **pull requests are welcome**.

1. Fork the repository and edit the Markdown file directly (GitHub's "Edit" button is enough).
2. Keep the guide's style: direct tone, commands in code blocks, no emoji in headings.
3. Change one topic per pull request.
4. If you fix the French, fix the English too (or say so in the description): both versions must say the same thing.
5. Do not paste any private information (addresses, passwords, machine names).

Open the pull request with the provided template: a short description is enough. The author reviews and merges.

For a mistake you cannot fix yourself, open an issue naming the guide and the passage.

## Translate the app

The app follows the system language. It exists in **French** and **English**, and the language files are published in
[`translations/`](translations/): you can correct the English or propose a **new language**. The full procedure is in
[`translations/README.md`](translations/README.md). In short:

- The files use Apple's **`.strings`** format (`"key" = "value";`). Both apps (macOS and Windows) read the same files.
- **Never change the keys** (the left side of the `=` sign): they are the original French text, and the app finds its strings through
  them. Only the value (the right side) is translated.
- **Keep the placeholders** (`%@`, `%lld`, `\n`…) unchanged, in the same number.
- **No text longer than necessary**: buttons, menus and tabs have a limited width. Pick the shortest term that stays clear.
- Use the polite form of your language (never slang or overly familiar).
- **A translation cannot be tried out without building the app**: you will not see it on screen before it is integrated. The author
  reviews your pull request and includes it in a version; you can then report any cut-off or misplaced text in an issue.

A translation is proposed as a **pull request on `translations/`**. If you are not comfortable with Git, open an issue or a discussion
and attach the file.

## Report a security vulnerability

**Never post a vulnerability in an issue, a discussion or a pull request.** Use GitHub's private reporting ("Report a vulnerability" in
the Security tab) or write to the author. Everything is explained in [SECURITY.md](SECURITY.md).

## What is not accepted

- **Code pull requests**: there is no code here. A pull request that adds or changes code will be closed.
- **Feature requests without context** ("add X"). Explain the need in Discussions, with your use case.
- **Duplicates** of issues or ideas that are already open: vote or comment on the existing one.
- **Support requests by e-mail or on X** that should be public: answers help other users.
- **Off-topic, promotional or disrespectful messages**: see the [code of conduct](CODE_OF_CONDUCT.md).

Thank you for helping Eukalyptus improve.
