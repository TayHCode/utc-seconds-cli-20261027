# UTC seconds CLI

A tiny Python standard-library CLI for signed whole seconds between two strict UTC timestamps.
Requires Python 3.9 or later. No installation or paid service is needed.
On Windows, use `python` instead of `python3` if that is your interpreter command.

## Quickstart

```sh
python3 -B utc_delta.py 2026-10-27T00:00:00Z 2026-10-27T00:01:05Z
```

Output is `65` followed by a newline. The result is end minus start.
Reversing the arguments prints `-65`; equal timestamps print `0`.
Only exact ASCII `YYYY-MM-DDTHH:MM:SSZ` values are accepted, with years 0001 through 9999.
Invalid format or calendar values exit with code 2 and print an error to stderr.

## Verify

```sh
python3 -B -m unittest discover -s tests -v
```

The tests invoke the real CLI and assert positive, negative, zero, leap-day,
full date-range, missing-argument and malformed-input behavior.
The Windows workflow runs the same tests using `.fleet/verify.ps1`.

## Limitations

Whole-second UTC calendar arithmetic only. No fractional seconds, offsets,
local time, leap seconds, batch files, network access or clock synchronization.
This is a small synthetic arithmetic fixture, not an elapsed-time clock.

## Existing tools

Python's [datetime library](https://docs.python.org/3/library/datetime.html)
provides parsing and date arithmetic. This CLI adds exact input validation and output.
GNU [date](https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html)
also parses timestamps, but is not required here.
