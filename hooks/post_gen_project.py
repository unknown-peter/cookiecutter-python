import os
import shutil
from pathlib import Path


def remove_files(*files: str):
	for f in files:
		path = Path(f)
		if not path.is_file():
			raise ValueError(f"未找到文件 {path}")
		
		path.unlink()


def setup_license(license: str):
	if license == 'NONE':
		remove_files('LICENSE')


if __name__ == "__main__":
    LICENSE = '{{ cookiecutter.license }}'

    setup_license(LICENSE)
