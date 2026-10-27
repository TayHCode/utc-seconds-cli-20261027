# Signed UTC difference

## Sub-features

Positive, negative and zero differences; calendar boundaries; strict input rejection.

## How to get to it (user POV)

Run `python3 -B utc_delta.py START END` from the repository root.

## Driving it with Python

Run `python3 -B -m unittest discover -s tests -v`.
The tests require 65, -65, 0, 86401 and 315537897599 for known examples.
Malformed timestamps in either position and missing arguments must exit 2,
leave stdout empty and print an error without a traceback.

## Gotchas

Only whole-second timestamps ending in uppercase Z are accepted.
