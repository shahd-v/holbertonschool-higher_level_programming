# SQL - Introduction

This directory contains introductory MySQL scripts covering database and table
creation, data insertion and modification, filtering, sorting, and aggregate
functions.

## Files

- `0-list_databases.sql`: list all databases.
- `1-create_database_if_missing.sql`: create `hbtn_0c_0`.
- `2-remove_database.sql`: remove `hbtn_0c_0`.
- `3-list_tables.sql`: list tables in the selected database.
- `4-first_table.sql`: create `first_table`.
- `5-full_table.sql`: display the definition of `first_table`.
- `6-list_values.sql`: list all rows in `first_table`.
- `7-insert_value.sql`: insert a row into `first_table`.
- `8-count_89.sql`: count rows whose `id` is 89.
- `9-full_creation.sql`: create and populate `second_table`.
- `10-top_score.sql`: list records ordered by score.
- `11-best_score.sql`: list records with a score of at least 10.
- `12-no_cheating.sql`: update Bob's score.
- `13-change_class.sql`: remove records with a score of 5 or less.
- `14-average.sql`: calculate the average score.
- `15-groups.sql`: count records in each score group.
- `16-no_link.sql`: list records that have a name.

## Usage

Run a script by piping it to MySQL. Scripts that operate on tables require a
database name:

```sh
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```
