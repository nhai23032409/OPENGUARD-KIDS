from pydantic import BaseModel

class HeartbeatCreate(BaseModel):
    device_id: str
    status: str
    policy_version: int

class HeartbeatResponse(BaseModel):
    status: str
    policy_version: int
    commands: list[str] = []
