ALTER TABLE documents
ADD COLUMN external_id TEXT NOT NULL;

ALTER TABLE documents
ADD CONSTRAINT documents_source_external_id_key
UNIQUE (source, external_id)

