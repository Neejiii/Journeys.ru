import uuid
from fastapi.responses import UJSONResponse
from services.db import DB


async def select_points() -> dict:
    query = """
        select p.id, p.loc_lat, p.loc_long, p.text
        from points p
    """
    points = await DB.conn.fetch(query)

    return {"points": points}


async def post_points(loc_lat: str, loc_long: str, text: str) -> UJSONResponse:
    query = """
        insert into points (id, loc_lat, loc_long, text)
        values ($1, $2, $3, $4)
    """
    try:
        print(query, uuid.uuid4(), loc_lat, loc_long, text)
        await DB.conn.execute(
            query, uuid.uuid4().hex, float(loc_lat), float(loc_long), text
        )
        return UJSONResponse(
            status_code=200,
            content={"message": "The points was successfully added"},
        )
    except Exception as e:
        return UJSONResponse(
            status_code=500,
            content={"message": f"Error in query: {e}"},
        )
