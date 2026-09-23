from database import get_connection

def search_companies(query: str) -> list[dict]:
    normalized_query = query.strip()
    if not normalized_query: return []

    search_pattern = f"%{normalized_query}%"

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT DISTINCT 
                    c.id,
                    c.name,
                    c.description
                FROM companies AS c
                JOIN documents AS d ON d.company_id = c.id
                WHERE
                    c.name ILIKE %s
                    OR c.description ILIKE %s
                    OR d.title ILIKE %s
                    OR d.body ILIKE %s
                ORDER BY c.name;
                """,
                (
                    search_pattern,
                    search_pattern,
                    search_pattern,
                    search_pattern
                ),
            )
            rows = cursor.fetchall()
    return [
        {
            "id": row[0],
            "title":  row[1],
            "body": row[2],
            "tags": []
        }
        for row in rows
    ]