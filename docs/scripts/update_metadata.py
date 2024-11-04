import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

if __name__ == "__main__":
    docs_dir = Path("../")
    src_dir = Path("../../src/")

    shutil.copy(
        Path(f"{docs_dir}/docfx.json"),
        Path(f"./backups/{datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")}.json"),
    )

    with open(f"{docs_dir}/docfx.json", "r", encoding="utf-8") as fr:
        original_docfx: Any = json.load(fr)

    new_metadata: list[Any] = []

    for project_file in src_dir.rglob("*.csproj"):
        if project_file.parent.parent.name == "src":
            new_metadata.append(
                {
                    "src": [
                        {
                            "src": str(project_file.parent)[3:].replace("\\", "/"),
                            "files": [
                                project_file.name,
                            ],
                        }
                    ],
                    "output": f"api/Netcord/{project_file.stem}",
                }
            )
        elif project_file.parent.parent.name == "extensions":
            new_metadata.append(
                {
                    "src": [
                        {
                            "src": str(project_file.parent)[3:].replace("\\", "/"),
                            "files": [
                                project_file.name,
                            ],
                        }
                    ],
                    "output": f"api/Extensions/{project_file.stem}",
                }
            )

    original_docfx["metadata"] = new_metadata

    with open(f"{docs_dir}/docfx.json", "w", encoding="utf-8") as fw:
        json.dump(original_docfx, fw, indent=4, sort_keys=True)
