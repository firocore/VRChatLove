import httpx
import json
import pydantic
from enum import StrEnum


class LovenceAction(StrEnum):
    vibrate="Vibrate"
    rotate="Rotate"
    pump="Pump"
    thrusting="Thrusting"
    fingering="Fingering"
    suction="Suction"
    depth="Depth"
    stroke="Stroke"
    oscillate="Oscillate"
    all="All"


class LovenseController:
    def __init__(self):
        self._url = "https://127-0-0-1.lovense.club:30010/command"
        self._headers = {"X-platform": "VRCLove"}
        
        self._toys: list[LovenceToy] = []

    async def get_remote_toys(self):
        async with httpx.AsyncClient(verify=False) as client:
            try:
                response = await client.post(self._url, headers=self._headers, json={"command": "GetToys"})
                response.raise_for_status()

                # Response Status Code Alvays 200
                # Internal Locense Code
                data = response.json()
                code = data.get("code")

                match code:
                    case 200:
                        await self.__parse_toys(data)
                    
                    case 402:
                        pass

                    case 502:
                        pass

                    case _:
                        pass

            except Exception as e:
                print("Lovense GetToys error:", e)

    async def __parse_toys(self, data: dict):
        try:
            toys_dict = json.loads(data["data"]["toys"])

            print(toys_dict)

            for toy_id, toy_data in toys_dict.items():
                actions = [
                    LovenceAction(action)
                    for action in toy_data.get("fullFunctionsNames", [])
                    if action in LovenceAction.__members__.values() or action in LovenceAction._value2member_map_
                ]
                toy = LovenceToy(
                    id=toy_id,
                    name=toy_data.get("name", ""),
                    nickname=toy_data.get("nickName", None),
                    version=toy_data.get("version", None),
                    actions=actions
                )

                print(f"New toy found {toy._toy_id}, {toy._name} {toy._toy_version}")

                self._toys.append(toy)

                await toy.send_vibrate()

        except Exception as e:
            print("Toys parsing error:", e)


class LovenceToy(LovenseController):
    def __init__(self, id: str, name: str, nickname: str | None = None, version: int | None = None, actions: list[LovenceAction] = []):
        super().__init__()

        self._toy_id: str = id
        self._name: str = name
        self._nickname: str | None = nickname
        self._toy_version: int | None = version
        self._actions: list[LovenceAction] = actions


    async def send_vibrate(self):
        power = 0

        payload = {
            "command": "Function",
            "action": f"All:{power}",
            "timeSec": 0,
            "toy": self._toy_id,
            "apiVer": 1
        }

        async with httpx.AsyncClient(verify=False) as client:
            try:
                print(f"Set lovense vibration power: {power}")
                response = await client.post(self._url, headers=self._headers, json=payload)
                response.raise_for_status()
                print(f"Toy response: {response.json()}")
            except Exception as e:
                print(f"Lovense vibration error: {e}")