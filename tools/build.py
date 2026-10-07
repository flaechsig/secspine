"""secspine für die Auslieferung bauen.

    python3 tools/build.py                 nennt nur die Version
    python3 tools/build.py dist            schreibt den Lieferbaum in den Branch `dist`
    python3 tools/build.py install <pfad>  schreibt den Lieferbaum in ein Projekt
                                           (um einen unveröffentlichten Stand zu erproben)

Der Branch `dist` enthält nur die Dateien, die secspine besitzt, an ihren Zielpfaden in
einem Projekt. Projekte installieren und aktualisieren damit:

    curl -fsSL https://github.com/flaechsig/secspine/archive/refs/heads/dist.tar.gz | tar -xz --strip-components=1
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
BRANCH = "dist"
PAYLOAD = ("STANDARD.md", "finding-template.md", "secspine.py")


def _header_version(path: Path) -> str:
    first = path.read_text(encoding="utf-8").splitlines()[0]
    m = re.match(r"<!--\s*secspine\s+(\S+)", first)
    if not m:
        raise SystemExit(f"{path.relative_to(REPO)} nennt seine Version nicht in der ersten Zeile")
    return m.group(1)


def version() -> str:
    """Die Version dessen, was secspine ausliefert. Quelle: .secspine/STANDARD.md."""
    return _header_version(REPO / ".secspine/STANDARD.md")


def delivery_tree(root: Path) -> None:
    """Die Dateien, die secspine ausliefert, an ihren Zielpfaden in ein Projekt schreiben."""
    sec = root / ".secspine"
    sec.mkdir(parents=True)
    for name in PAYLOAD:
        shutil.copy(REPO / ".secspine" / name, sec / name)
    shutil.copy(REPO / "LICENSE", sec / "LICENSE")
    shutil.copy(REPO / ".secspine/CHANGELOG.md", sec / "CHANGELOG.md")
    skills = root / ".agents/skills"
    skills.mkdir(parents=True)
    for skill in sorted((REPO / ".agents/skills").iterdir()):
        if skill.name.startswith("secspine-") and (skill / "SKILL.md").is_file():
            shutil.copytree(skill, skills / skill.name)
    (root / ".claude").mkdir()
    os.symlink("../.agents/skills", root / ".claude/skills")
    files = sorted(p.relative_to(root).as_posix() for p in root.rglob("*")
                   if p.is_file() or p.is_symlink())
    files.append(".secspine/MANIFEST")
    (sec / "MANIFEST").write_text("\n".join(sorted(files)) + "\n", encoding="utf-8")


def install(project: Path) -> None:
    """Den Lieferbaum in ein Projekt schreiben, wie es die Installationszeile tut."""
    with tempfile.TemporaryDirectory() as tmp:
        tree = Path(tmp) / "tree"
        delivery_tree(tree)
        for src in sorted(tree.rglob("*")):
            dst = project / src.relative_to(tree)
            if src.is_symlink():
                if not dst.is_symlink() and not dst.exists():
                    os.symlink(os.readlink(src), dst)
            elif src.is_dir():
                dst.mkdir(parents=True, exist_ok=True)
            else:
                shutil.copy2(src, dst)


def _git(*args: str, env=None, input=None) -> str:
    return subprocess.run(["git", *args], cwd=REPO, check=True, capture_output=True,
                          text=True, env=env, input=input).stdout.strip()


def commit_dist() -> str:
    """Den Lieferbaum in den Branch `dist` committen, ohne den Arbeitsbaum zu berühren."""
    ver = version()
    with tempfile.TemporaryDirectory() as tmp:
        tree_dir = Path(tmp) / "tree"
        delivery_tree(tree_dir)
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(tmp) / "index"))
        _git("--work-tree", str(tree_dir), "add", "-A", ".", env=env)
        tree = _git("write-tree", env=env)
    parent = subprocess.run(["git", "rev-parse", "--verify", "-q", f"refs/heads/{BRANCH}"],
                            cwd=REPO, capture_output=True, text=True).stdout.strip()
    if parent and _git("rev-parse", f"{parent}^{{tree}}") == tree:
        return parent
    source = _git("rev-parse", "--short", "HEAD")
    args = ["commit-tree", tree] + (["-p", parent] if parent else [])
    commit = _git(*args, input=f"secspine {ver} (from {source})\n")
    _git("update-ref", f"refs/heads/{BRANCH}", commit)
    if subprocess.run(["git", "rev-parse", "--verify", "-q", f"refs/tags/v{ver}"],
                      cwd=REPO, capture_output=True).returncode != 0:
        _git("tag", f"v{ver}", commit)
    return commit


if __name__ == "__main__":
    if sys.argv[1:2] == ["install"] and len(sys.argv) == 3:
        install(Path(sys.argv[2]).resolve())
        print(f"installed secspine {version()} (working copy) into {sys.argv[2]}", file=sys.stderr)
    elif sys.argv[1:] == ["dist"]:
        commit = commit_dist()
        print(f"branch {BRANCH} at {commit[:10]} (secspine {version()})", file=sys.stderr)
    else:
        print(f"secspine {version()}", file=sys.stderr)
