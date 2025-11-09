# main.py
import os
import argparse
import subprocess
import sys

def install_dependencies():
    """Installs necessary project dependencies."""
    try:
        print("Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def run_react_native(platform: str):
    """Runs the React Native application for the specified platform."""
    try:
        if platform == "ios":
            print("Starting iOS build...")
            subprocess.check_call(["npx", "react-native", "run-ios"])
        elif platform == "android":
            print("Starting Android build...")
            subprocess.check_call(["npx", "react-native", "run-android"])
        else:
            print("Invalid platform. Choose 'ios' or 'android'.")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running React Native: {e}")
        sys.exit(1)

def lint_code():
    """Lints the codebase using ESLint."""
    try:
        print("Linting code...")
        subprocess.check_call(["npx", "eslint", "."])
        print("Linting complete.")
    except subprocess.CalledProcessError as e:
        print(f"Linting failed: {e}")
        sys.exit(1)

def format_code():
    """Formats the codebase using Prettier."""
    try:
        print("Formatting code...")
        subprocess.check_call(["npx", "prettier", "--write", "."])
        print("Formatting complete.")
    except subprocess.CalledProcessError as e:
        print(f"Formatting failed: {e}")
        sys.exit(1)

def main():
    """Main entry point of the script."""
    parser = argparse.ArgumentParser(description="Mobile App React Native Utility Script")
    parser.add_argument("action", choices=["run", "lint", "format", "install"], help="Action to perform: run, lint, format, install")
    parser.add_argument("--platform", choices=["ios", "android"], help="Platform to run on (required for 'run' action)")

    args = parser.parse_args()

    if args.action == "install":
        install_dependencies()
    elif args.action == "run":
        if not args.platform:
            print("Platform is required for 'run' action. Use --platform ios or --platform android.")
            sys.exit(1)
        run_react_native(args.platform)
    elif args.action == "lint":
        lint_code()
    elif args.action == "format":
        format_code()
    else:
        print("Invalid action. Choose 'run', 'lint', 'format', or 'install'.")
        sys.exit(1)

if __name__ == "__main__":
    main()