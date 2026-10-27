---
name: verify-utc-seconds
description: Verify the UTC seconds command line behavior and strict input rejection.
---

## Launch

Use Python 3.9 or later from the repository root. No install or server is needed.

## Doctor

Run `python3 -B utc_delta.py --help` and confirm start and end arguments are listed.

## Drive

Run `python3 -B utc_delta.py 2026-10-27T00:00:00Z 2026-10-27T00:01:05Z`.
Require exit 0 and stdout exactly `65` plus a newline.
Run `python3 -B -m unittest discover -s tests -v` to cover the feature map.

## Evidence

Retain command output and exit codes outside the checkout. The tests invoke the
public entrypoint in subprocesses and check exact outputs and rejection behavior.

## Cleanup

No process or runtime file persists. Confirm `git status --porcelain` is empty.
Keep captured evidence outside the checkout.

## Helpers

The Windows helper is `.fleet/verify.ps1`. Run it with PowerShell from the root.
