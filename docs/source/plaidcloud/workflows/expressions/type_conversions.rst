Data Type Expressions
======================

.. toctree::
   :maxdepth: 2
   :includehidden:

.. sidebar:: This Page

   .. contents::
      :local: 

      

Analyze offers a wide variety of standard data types (dtypes) to support your
requirements. As datasets become larger, determining smaller size
dtypes for value storage can shrink the size of the table and improve
performance. The following dtypes are available:

-  Boolean
-  Text
-  Numbers

   -  Small Float (6 Digits)
   -  Float (15 Digits)
   -  Small Integer (16 bit) (-32768 to 32767)
   -  Integer (32 bit) (-2147483648 to 2147483647)
   -  Big Integer (64 bit) (-9223372036854775808 to 9223372036854775807)
   -  Numeric

-  Dates and Times

   -  Date
   -  Timestamp
   -  Time Interval

It is also possible to convert from one dtype to another using the
func.cast() process.

.. note:: Casting to an incompatible dtype may cause errors. For
          example, casting 'hello' to an integer will not work.

func.cast() Type Conversions
----------------------------

+----------------------+--------------+-----------+
| Analyze Expression   | Description  | Result    |
+======================+==============+===========+
| func.cast(123, Text) | Integer to   | '123'     |
|                      | Text         |           |
+----------------------+--------------+-----------+
| func.cast('123',     | Text to      | 123       |
| Integer)             | Integer      |           |
+----------------------+--------------+-----------+
| func.cast('78.69',   | Text to      | 78.69     |
| Float)               | Float        |           |
+----------------------+--------------+-----------+
| func.cast('78.69',   | Text to      | 78.69     |
| SmallFloat)          | Small Float  |           |
+----------------------+--------------+-----------+
| func.cast('78.69',   | Text to      | 78        |
| Integer)             | Integer      |           |
|                      | (Truncate    |           |
|                      | decimals)    |           |
+----------------------+--------------+-----------+
| func.cast('78.69',   | Text to      | 78        |
| SmallInteger)        | Small        |           |
|                      | Integer      |           |
|                      | (Truncate    |           |
|                      | decimals)    |           |
+----------------------+--------------+-----------+
| func.cast('78.69',   | Text to Big  | 78        |
| BigInteger)          | Integer      |           |
|                      | (Truncate    |           |
|                      | decimals)    |           |
+----------------------+--------------+-----------+
| func.cast(1,         | Integer to   | True      |
| Boolean)             | Boolean      |           |
+----------------------+--------------+-----------+


func.to() Data Type Conversions
-------------------------------

+-----------------------+----------------+----------------+------------+
| Analyze Expression    | Return Type    | Description    | Example    |
+=======================+================+================+============+
| func.to\_char(timesta | text           | convert time   | to\_char(c |
| mp,                   |                | stamp to       | urrent\_ti |
| text)                 |                | string         | mestamp,   |
|                       |                |                | 'HH12:MI:S |
|                       |                |                | S')        |
+-----------------------+----------------+----------------+------------+
| func.to\_char(interva | text           | convert        | to\_char(i |
| l,                    |                | interval to    | nterval    |
| text)                 |                | string         | '15h 2m    |
|                       |                |                | 12s',      |
|                       |                |                | 'HH24:MI:S |
|                       |                |                | S')        |
+-----------------------+----------------+----------------+------------+
| func.to\_char(integer | text           | convert        | to\_char(1 |
| ,                     |                | integer to     | 25,        |
| text)                 |                | string         | '999')     |
+-----------------------+----------------+----------------+------------+
| func.to\_char(big     | text           | convert        | to\_char(1 |
| float, text)          |                | real/double    | 25.8::real |
|                       |                | precision to   | ,          |
|                       |                | string         | '999D9')   |
+-----------------------+----------------+----------------+------------+
| func.to\_char(numeric | text           | convert        | to\_char(- |
| ,                     |                | numeric to     | 125.8,     |
| text)                 |                | string         | '999D99S') |
+-----------------------+----------------+----------------+------------+
| func.to\_date(text,   | date           | convert string | to\_date(' |
| text)                 |                | to date        | 05         |
|                       |                |                | Dec 2000', |
|                       |                |                | 'DD Mon    |
|                       |                |                | YYYY')     |
+-----------------------+----------------+----------------+------------+
| func.to\_number(text, | numeric        | convert string | to\_number |
| text)                 |                | to numeric     | ('12,454.8 |
|                       |                |                | -',        |
|                       |                |                | '99G999D9S |
|                       |                |                | ')         |
+-----------------------+----------------+----------------+------------+
| func.to\_timestamp(te | timestamp with | convert string | to\_timest |
| xt,                   | time zone      | to time stamp  | amp('05    |
| text)                 |                |                | Dec 2000', |
|                       |                |                | 'DD Mon    |
|                       |                |                | YYYY')     |
+-----------------------+----------------+----------------+------------+
| func.to\_timestamp(bi | timestamp with | convert UNIX   | to\_timest |
| g                     | time zone      | epoch to time  | amp(200120 |
| float)                |                | stamp          | 400)       |
+-----------------------+----------------+----------------+------------+

.. todo:: Add screenshots