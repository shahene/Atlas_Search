import json
from pathlib import Path
from database import get_connection

DATA_PATH = Path(__file__).parent / "data" / "startups.json"

def load_documents() -> list[dict]:
    with DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)

SOURCE_NAME = "atlas_seed_dataset"

'''
upsert = insert or update
cursor = the thing Python uses to send SQL commands to Postgres

so calling upsert_company(cursor, first_document)
means use this database connection (cursor) to store the JSON startup record 
(first_document) as a company
'''

# take one startup record
# -- insert its title/body into companies
# -- if that company name already exists, update its description instead
# -- return the company's database ID
def upsert_company(cursor, document: dict) -> int:
    cursor.execute(
        """
        INSERT INTO companies (name, description)
        VALUES (%s, %s)
        ON CONFLICT (name) DO UPDATE
        SET description = EXCLUDED.description
        RETURNING id;
        """,
        (document["title"], document["body"]),
    )
    return cursor.fetchone()[0]

def upsert_document(cursor, company_id: int, document: dict) -> None:
    cursor.execute(
        """
        INSERT INTO documents (
            company_id,
            source,
            external_id,
            title,
            body
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (source, external_id) DO UPDATE
        SET
            company_id = EXCLUDED.company_id,
            title = EXCLUDED.title,
            body = EXCLUDED.body;
        """,
        (
            company_id,
            SOURCE_NAME,
            str(document["id"]),
            document["title"],
            document["body"]
        )
    )  
def upsert_tag(cursor, raw_tag_name: str) -> int:
    tag_name = raw_tag_name.strip().lower()
    cursor.execute(
        """
        INSERT INTO tags (name)
        VALUES (%s)
        ON CONFLICT (name) DO UPDATE
        SET name = EXCLUDED.name
        RETURNING id;
        """,
        (tag_name,),
    ) 
    return cursor.fetchone()[0]

def link_company_to_tag(cursor, company_id: int, tag_id: int) -> None:
    cursor.execute(
        """
        INSERT INTO company_tags (company_id, tag_id)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;
        """,
        (company_id, tag_id),
    )

if __name__ == "__main__":
    documents = load_documents()
    with get_connection() as connection:
        with connection.cursor() as cursor:
            for document in documents:
                company_id = upsert_company(cursor, document)
                upsert_document(cursor, company_id, document)
                for raw_tag_name in document["tags"]:
                    tag_id = upsert_tag(cursor, raw_tag_name)
                    link_company_to_tag(cursor, company_id, tag_id)
    print(f"Ingested {len(documents)} documents.")



    