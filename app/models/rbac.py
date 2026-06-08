from pydantic import BaseModel
from typing import List

class RoleRule(BaseModel):
    verbs: List[str]
    resources: List[str]

class KubernetesRole(BaseModel):
    name: str
    rules: List[RoleRule]
