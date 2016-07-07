from django.db import connection
from collections import namedtuple


def execute_raw_query(query, params, name):
    cursor = connection.cursor()
    cursor.execute(query, params)
    desc = cursor.description
    nt_result = namedtuple(name, [col[0] for col in desc])
    rows = [nt_result(*row) for row in cursor.fetchall()]
    return rows
