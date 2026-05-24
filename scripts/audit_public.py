#!/usr/bin/env python3
"""
Security audit: check for secrets, local paths, private keys, etc.
"""

import sys
from pathlib import Path
import re


PATTERNS = [
    (r"api[_-]?key\s*[:=]", "API key"),
    (r"secret\s*[:=]", "Secret"),
    (r"password\s*[:=]", "Password"),
    (r"private[_-]?key", "Private key"),
    (r"-----BEGIN RSA PRIVATE KEY-----", "RSA private key"),
    (r"-----BEGIN OPENSSH PRIVATE KEY-----", "SSH private key"),
    (r"token\s*[:=]", "Token"),
    (r"/Users/[^/]+/", "Local user path"),
    (r"aws_access_key_id", "AWS key"),
    (r"aws_secret_access_key", "AWS secret"),
]

EXCLUDE_PATHS = {
    ".git",
    ".obsidian",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    "venv",
    "env",
    "scripts/audit_public.py",  # Exclude the audit script itself
}


def audit() -> int:
    """Check for security issues."""
    errors = []
    vault_root = Path.cwd()

    for file_path in vault_root.rglob("*"):
        # Skip excluded paths
        rel_path = str(file_path.relative_to(vault_root))
        if any(part in EXCLUDE_PATHS for part in file_path.parts) or rel_path in EXCLUDE_PATHS:
            continue

        if file_path.is_dir() or file_path.suffix in {".png", ".jpg", ".pdf", ".mp3", ".mp4"}:
            continue

        try:
            with open(file_path, "r", errors="ignore") as f:
                content = f.read()

            for pattern, name in PATTERNS:
                if re.search(pattern, content, re.IGNORECASE):
                    errors.append(f"{file_path.relative_to(vault_root)}: {name}")
        except:
            pass

    if errors:
        print("✗ Security audit failed:")
        for error in errors:
            print(f"  {error}")
        return 1

    print("✓ Security audit passed")
    return 0


if __name__ == "__main__":
    sys.exit(audit())
