from fastapi.responses import JSONResponse


async def generic_error(request, ex):
    return JSONResponse(
        {"message": ex.args[0].get("message"), "error_code": ex.args[0].get("error_code")},
        status_code=ex.args[0].get("code"),
    )
