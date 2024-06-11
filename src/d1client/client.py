from typing import Any, Dict, List

from cloudflare import Cloudflare


class D1Client:
    def __init__(self, api_token: str, account_id: str, database_id: str):
        self.client = Cloudflare(api_token=api_token)
        self.account_id = account_id
        self.database_id = database_id

    def query_database(self, sql: str) -> List[object] | None:
        result = self.client.d1.database.query(
            account_identifier=self.account_id,
            database_identifier=self.database_id,
            sql=sql,
        )

        if result is None:
            return None

        return result[0].results

    def create_record(
        self, table: str, record: Dict[str, Any]
    ) -> bool | List[object] | None:
        columns = ", ".join(record.keys())
        placeholders = ", ".join([f":{k}" for k in record.keys()])
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        result = self.client.d1.database.query(
            account_identifier=self.account_id,
            database_identifier=self.database_id,
            sql=sql,
            params=[
                record[k] for k in record
            ],  # Convert the record values to a list for params
        )

        if result is None:
            return None

        if result[0].success:
            return True
        else:
            return result[0].results

    def update_record(
        self, table: str, record_id: str, updates: Dict[str, Any]
    ) -> bool | List[object] | None:
        set_clause = ", ".join([f"{k} = :{k}" for k in updates.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE id = :id"
        updates["id"] = record_id
        result = self.client.d1.database.query(
            account_identifier=self.account_id,
            database_identifier=self.database_id,
            sql=sql,
            params=[updates[k] for k in updates],
        )

        if result is None:
            return None

        if result[0].success:
            return True
        else:
            return result[0].results
