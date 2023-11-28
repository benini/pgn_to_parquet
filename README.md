# Loving Parquet (Beyond PGN)

This repository explores the benefits of using the innovative Parquet file format to replace the traditional PGN (Portable Game Notation) format used for storing chess games.  
The file pgn_to_parquet.py is a simple Python script that converts a PGN to a Parquet file and with that ...

## Why Parquet is Superior to PGN

### SQL Queries on Data

With Parquet, you can use SQL language to query data. This is a significant advantage over the PGN format, as there's no need to import the entire database for analysis. Users can perform complex queries efficiently, extract specific information, and even conduct aggregate analysis directly on the Parquet file.

### Remote Access and File Merging

Parquet supports remote file access and allows merging multiple remote files into a single query. This means users can access and analyze data from various sources without needing to completely read Parquet files.

### Automatic Compression

One of the key advantages of Parquet is its ability to automatically compress data. This means Parquet files take up less disk space than PGN files while maintaining data integrity and readability. Compression not only reduces storage space requirements but also enhances data read performance.

## Example using DuckDB client

DuckDB, an SQL database management system, makes it particularly easy to work with Parquet files. Here are some examples of how it is possible to use DuckDB to query Parquet files containing chess game data:

```sql
CREATE VIEW chess_games AS SELECT * FROM read_parquet(
  ['https://github.com/benini/pgn_to_parquet/raw/main/twic1515.parquet',
   'https://github.com/benini/pgn_to_parquet/raw/main/twic1516.parquet']);
DESCRIBE chess_games;
```
```
| column_name  | column_type | null | key | default | extra |
|--------------|-------------|------|-----|---------|-------|
| Event        | VARCHAR     | YES  |     |         |       |
| Site         | VARCHAR     | YES  |     |         |       |
| Date         | TIMESTAMP   | YES  |     |         |       |
| Round        | VARCHAR     | YES  |     |         |       |
| White        | VARCHAR     | YES  |     |         |       |
| Black        | VARCHAR     | YES  |     |         |       |
| Result       | VARCHAR     | YES  |     |         |       |
| WhiteTitle   | VARCHAR     | YES  |     |         |       |
| BlackTitle   | VARCHAR     | YES  |     |         |       |
| WhiteElo     | VARCHAR     | YES  |     |         |       |
| BlackElo     | VARCHAR     | YES  |     |         |       |
| ECO          | VARCHAR     | YES  |     |         |       |
| Opening      | VARCHAR     | YES  |     |         |       |
| WhiteTeam    | VARCHAR     | YES  |     |         |       |
| BlackTeam    | VARCHAR     | YES  |     |         |       |
| WhiteFideId  | VARCHAR     | YES  |     |         |       |
| BlackFideId  | VARCHAR     | YES  |     |         |       |
| EventDate    | VARCHAR     | YES  |     |         |       |
| __movetext__ | VARCHAR     | YES  |     |         |       |
| Variation    | VARCHAR     | YES  |     |         |       |
| EventType    | VARCHAR     | YES  |     |         |       |
```

```sql
.mode json
SELECT * FROM chess_games WHERE White ilike '%vachier%' LIMIT 1;
```
```json
{"Event":"Saint Louis Rapid 2023","Site":"Saint Louis USA","Date":"2023-11-14 00:00:00","Round":"2.5","White":"Vachier Lagrave,M","Black":"Caruana,F","Result":"1/2-1/2","WhiteTitle":"GM","BlackTitle":"GM","WhiteElo":"2734","BlackElo":"2795","ECO":"C92","Opening":"Ruy Lopez","WhiteTeam":null,"BlackTeam":null,"WhiteFideId":"623539","BlackFideId":"2020009","EventDate":"2023.11.14","__movetext__":"1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3\nO-O 9. h3 Be6 10. d4 Bxb3 11. axb3 Re8 12. d5 Nb8 13. Nbd2 Qc8 14. Nf1 c6 15.\ndxc6 Qxc6 16. Ng3 h6 17. Nh4 Nbd7 18. Nhf5 Bf8 19. b4 Re6 20. Ne3 Nb6 21. Qf3\nd5 22. exd5 Nbxd5 23. Nxd5 Nxd5 24. Ne4 Rae8 25. Rd1 Nf6 26. Nxf6+ Rxf6 27.\nQxc6 Rxc6 28. Rd7 f5 29. g3 Re7 30. Rd8 Kf7 31. Be3 Re8 32. Rd7+ Re7 33. Rd5\nRee6 34. Bc5 Be7 35. Re1 Bf6 36. h4 Kg6 37. Kg2 h5 38. Kf3 Rc8 39. Red1 Rce8\n40. Rd7 e4+ 41. Ke3 Be5 42. Bd4 Bxd4+ 43. R1xd4 Kf6 44. R4d5 g5 45. hxg5+ Kxg5\n46. Rf7 Re5 47. Rg7+ Kh6 48. Rdd7 R5e6 49. Rh7+ Kg6 50. Rhg7+ Kh6 51. Rh7+ Kg6\n52. Rdg7+ Kf6 53. Ra7 Kg6 54. Rhg7+ Kh6 55. Rgd7 Kg6 56. Rd5 h4 57. gxh4 Rh8\n58. Rd1 Rxh4 59. Ra1 f4+ 60. Kd4 Kf5 61. Rf7+ Kg4 62. Re1 Kf3 63. Re3+ Kxf2 64.\nRxe4 Rxe4+ 65. Kxe4 f3+ 66. Kd3 Rg4 67. b3 Kg2 68. Ke3 Rg8 69. c4 Re8+ 70. Kd2\nf2 71. Rg7+ Kf1 72. c5 Re2+ 73. Kd1 Re6 74. Kd2 Re2+ 75. Kd1 Re3 76. c6 Rxb3\n77. c7 Rc3 78. Kd2 Rc6 79. Rf7 Kg2 80. Rg7+ Kf1 81. Rf7 Rc4 82. Rg7 Rc6 83. Rf7\n1/2-1/2","Variation":"closed, Kholmov variation","EventType":null}
```

```sql
.mode markdown
SELECT White,Black,Result,Date FROM chess_games WHERE White ilike '%vachier%';
```
```
|       White       |      Black       | Result  |        Date         |
|-------------------|------------------|---------|---------------------|
| Vachier Lagrave,M | Caruana,F        | 1/2-1/2 | 2023-11-14 00:00:00 |
| Vachier Lagrave,M | Nepomniachtchi,I | 1/2-1/2 | 2023-11-15 00:00:00 |
| Vachier Lagrave,M | Robson,R         | 1/2-1/2 | 2023-11-16 00:00:00 |
| Vachier Lagrave,M | Sevian,Samuel    | 1/2-1/2 | 2023-11-16 00:00:00 |
| Vachier Lagrave,M | Nepomniachtchi,I | 0-1     | 2023-11-17 00:00:00 |
| Vachier Lagrave,M | Giri,A           | 1-0     | 2023-11-17 00:00:00 |
| Vachier Lagrave,M | So,W             | 1-0     | 2023-11-17 00:00:00 |
| Vachier Lagrave,M | Caruana,F        | 1/2-1/2 | 2023-11-17 00:00:00 |
| Vachier Lagrave,M | Le,Quang Liem    | 0-1     | 2023-11-18 00:00:00 |
| Vachier Lagrave,M | Firouzja,Alireza | 1-0     | 2023-11-18 00:00:00 |
| Vachier Lagrave,M | Robson,R         | 1/2-1/2 | 2023-11-18 00:00:00 |
| Vachier Lagrave,M | Xiong,Jeffery    | 1/2-1/2 | 2023-11-18 00:00:00 |
| Vachier Lagrave,M | Sevian,Samuel    | 1/2-1/2 | 2023-11-18 00:00:00 |
| Vachier Lagrave,M | Aronian,L        | 1/2-1/2 | 2023-11-21 00:00:00 |
| Vachier Lagrave,M | Caruana,F        | 1/2-1/2 | 2023-11-23 00:00:00 |
| Vachier Lagrave,M | Nepomniachtchi,I | 1/2-1/2 | 2023-11-25 00:00:00 |
```
