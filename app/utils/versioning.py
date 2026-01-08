import re

import httpx
from PySide6.QtCore import QThread, Signal, QObject

from app.core import constants


class VersionChecker(QObject):
    versionChecked = Signal(str)

    def check_version(self):
        import asyncio
        asyncio.run(self._check_version_async())

    async def _check_version_async(self):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(constants.URL_README, timeout=5)
                content = response.text
                match = re.search(r"\*\*Version:\*\*\s*([0-9]+\.[0-9]+\.[0-9]+)", content)
                version = match.group(1) if match else ""
                self.versionChecked.emit(version)
            except Exception as e:
                print(f"Error retrieving version: {e}")
                self.versionChecked.emit("")
