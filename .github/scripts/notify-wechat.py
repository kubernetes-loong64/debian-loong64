#!/usr/bin/env python3
"""Send a WeChat Work webhook notification for Debian package version updates."""

import argparse
import json
import textwrap
import urllib.request


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Notify WeChat Work webhook about new Debian package versions."
    )
    parser.add_argument("--webhook-url", required=True, help="WeChat Work webhook URL")
    parser.add_argument("--deb-name", required=True, help="Debian package name")
    parser.add_argument("--expected-version", required=True, help="Expected version")
    parser.add_argument("--newer-versions", required=True, help="Newer versions found")
    parser.add_argument("--run-url", required=True, help="GitHub Actions run URL")
    args = parser.parse_args()

    content = textwrap.dedent(f"""\
    ## Debian 包版本更新通知

    > **包名**: <font color="comment">{args.deb_name}</font>
    > **预期版本**: <font color="comment">{args.expected_version}</font>
    > **新版本**: <font color="warning">{args.newer_versions.strip()}</font>

    请及时更新 [GitHub Actions]({args.run_url})""")

    payload = json.dumps({
        "msgtype": "markdown",
        "markdown": {"content": content},
    }).encode()

    req = urllib.request.Request(
        args.webhook_url,
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    urllib.request.urlopen(req)

    print("WeChat Work notification sent.")


if __name__ == "__main__":
    main()
