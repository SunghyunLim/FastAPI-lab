from fastapi import APIRouter

from blog import schemas
from .. import schemas
router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:schemas.Login):
    return 'login'