import json
import os
import subprocess

PACKAGE_DIR = "blip"
LOCAL_MANIFEST = "package.local.json"
REMOTE_MANIFEST = "package.json"


def get_repo() -> str:
    url = subprocess.check_output(
        ["git", "remote", "get-url", "origin"]
    ).decode().strip()

    return url.split(":")[-1].removesuffix(".git")


def find_py_files(top: str) -> list[str]:
    paths = []

    for root, _, files in os.walk(top):
        for name in files:
            if name.endswith(".py"):
                paths.append(os.path.join(root, name).replace(os.sep, "/"))

    return sorted(paths)


def load_manifest(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def save_manifest(path: str, manifest: dict):
    with open(path, "w") as f:
        json.dump(manifest, f, indent=4)
        f.write("\n")

    print("Wrote manifest:", path)


def string_list(strings: list) -> str:
    return "\n - " + "\n - ".join(strings)


def main():
    repo = get_repo()
    local_manifest = load_manifest(LOCAL_MANIFEST)
    version = local_manifest["version"]
    deps = local_manifest["deps"]
    py_files = find_py_files(PACKAGE_DIR)

    print("Determined repo:", repo)
    print("Using version:", version)
    print("Using deps:" + string_list([f"{d[0]} @ {d[1]}" for d in deps]))
    print("\nFound python files:" + string_list(py_files))
    print()

    local_manifest = {
        "urls": [[path, path] for path in py_files]
    }

    remote_manifest = {
        "urls": [[path, f"github:{repo}/{path}"] for path in py_files]
    }

    for manifest in [local_manifest, remote_manifest]:
        manifest["deps"] = deps
        manifest["version"] = version

    save_manifest(LOCAL_MANIFEST, local_manifest)
    save_manifest(REMOTE_MANIFEST, remote_manifest)


if __name__ == "__main__":
    main()
