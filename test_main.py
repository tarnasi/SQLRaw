from SQLRaw.commands.pg_raw import PG_SELECT_ALL_ROWS

print(PG_SELECT_ALL_ROWS.format(
    table="user",
    order='id',
    ordering='DESC'
))
