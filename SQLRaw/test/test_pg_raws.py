from commands.pg_raw import PG_SELECT_ALL_ROWS

print(PG_SELECT_ALL_ROWS.format(table='traces', order='id', ordering='DESC'))
