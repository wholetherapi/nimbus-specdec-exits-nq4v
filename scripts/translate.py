"""Run the early-exit ensemble on a WMT test split."""
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", default="wmt22")
    args = parser.parse_args()
    print(f"translating split {args.split}")


if __name__ == "__main__":
    main()
