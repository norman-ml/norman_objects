from fastapi.routing import APIRoute
from fastapi import Request, HTTPException, status

def allow_anonymous(func):
    func.__allow_anonymous__ = True
    return func


class AuthenticatedRoute(APIRoute):
    async def _check_and_call(self, request: Request, original_handler):
        if getattr(self.endpoint, "__allow_anonymous__", False):
            return await original_handler(request)

        if not getattr(request.state, "user", None):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")

        return await original_handler(request)

    def get_route_handler(self):
        original = super().get_route_handler()

        async def wrapper(request: Request):
            return await self._check_and_call(request, original)

        return wrapper
