"""Print the signed whole seconds between two strict UTC timestamps."""
import argparse
from datetime import datetime
import re


def utc_timestamp(value):
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", value):
        raise argparse.ArgumentTypeError("expected YYYY-MM-DDTHH:MM:SSZ")
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        raise argparse.ArgumentTypeError("invalid UTC calendar timestamp") from None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("start", type=utc_timestamp)
    parser.add_argument("end", type=utc_timestamp)
    args = parser.parse_args()
    delta = args.end - args.start
    print(delta.days * 86400 + delta.seconds)


if __name__ == "__main__":
    main()
