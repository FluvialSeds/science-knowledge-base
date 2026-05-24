#!/bin/bash
# Install git hooks for the Wiki

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOKS_DIR="$REPO_ROOT/.githooks"

# Create hooks directory if it doesn't exist
mkdir -p "$HOOKS_DIR"

# Configure git to use the hooks directory
git config core.hooksPath .githooks

# Make pre-commit executable
chmod +x "$HOOKS_DIR/pre-commit"

echo "✓ Git hooks installed"
echo "  Hooks directory: $HOOKS_DIR"
echo "  Pre-commit hook: .githooks/pre-commit"
