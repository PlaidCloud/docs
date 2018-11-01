Dates and Time Expressions
===========================

.. toctree::
   :maxdepth: 2
   :includehidden:


+-----------------------+----------------+----------------+------------+-----------+
| Analyze Expression    | Return Type    | Description    | Example    | Result    |
+=======================+================+================+============+===========+
| func.age(timestamp,   | interval       | Subtract       | age (timest| 43 years  |
| timestamp)            |                | arguments,     | amp        | 9 months  |
|                       |                | producing a    | '2001-04-1 | 27 days   |
|                       |                | "symbolic"     | 0',        |           |
|                       |                | result that    | timestamp  |           |
|                       |                | uses years and | '1957-06-1 |           |
|                       |                | months         | 3')        |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.age(timestamp)   | interval       | Subtract from  | age(timest | 43 years  |
|                       |                | current\_date  | amp        | 8 months  |
|                       |                |                | '1957-06-1 | 3 days    |
|                       |                |                | 3')        |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.clock\_timestamp | timestamp with | Current date   |            |           |
| ()                    | time zone      | and time       |            |           |
|                       |                | (changes       |            |           |
|                       |                | during         |            |           |
|                       |                | statement      |            |           |
|                       |                | execution)     |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.current\_date    | date           | Current date   |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.current\_time    | time with time | Current time   |            |           |
|                       | zone           | of day         |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.current\_timesta | timestamp with | Current date   |            |           |
| mp                    | time zone      | and time       |            |           |
|                       |                | (start of      |            |           |
|                       |                | current        |            |           |
|                       |                | transaction)   |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.date\_part(text, | double         | Get subfield   | date\_part | 20        |
| timestamp)            | precision      | (equivalent to | ('hour',   |           |
|                       |                | extract)       | timestamp  |           |
|                       |                |                | '2001-02-1 |           |
|                       |                |                | 6          |           |
|                       |                |                | 20:38:40') |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.date\_part(text, | double         | Get subfield   | date\_part | 3         |
| interval)             | precision      | (equivalent to | ('month',  |           |
|                       |                | extract)       | interval   |           |
|                       |                |                | '2 years 3 |           |
|                       |                |                | months')   |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.date\_trunc(text | timestamp      | Truncate to    | date\_trun | 36938.833 |
| ,                     |                | specified      | c('hour',  | 3333333   |
| timestamp)            |                | precision      | timestamp  |           |
|                       |                |                | '2001-02-1 |           |
|                       |                |                | 6          |           |
|                       |                |                | 20:38:40') |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.extract(field    | double         | Get subfield   | extract(ho | 20        |
| from timestamp)       | precision      |                | ur         |           |
|                       |                |                | from       |           |
|                       |                |                | timestamp  |           |
|                       |                |                | '2001-02-1 |           |
|                       |                |                | 6          |           |
|                       |                |                | 20:38:40') |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.extract(field    | double         | Get subfield   | extract(mo | 3         |
| from interval)        | precision      |                | nth        |           |
|                       |                |                | from       |           |
|                       |                |                | interval   |           |
|                       |                |                | '2 years 3 |           |
|                       |                |                | months')   |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.isfinite(timesta | boolean        | Test for       | isfinite(t | TRUE      |
| mp)                   |                | finite time    | imestamp   |           |
|                       |                | stamp (not     | '2001-02-1 |           |
|                       |                | equal to       | 6          |           |
|                       |                | infinity)      | 21:28:30') |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.isfinite(interva | boolean        | Test for       | isfinite(i | TRUE      |
| l)                    |                | finite         | nterval    |           |
|                       |                | interval       | '4 hours') |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.justify\_days(in | interval       | Adjust         | justify\_d | 1 month   |
| terval)               |                | interval so    | ays(interv |           |
|                       |                | 30-day time    | al         |           |
|                       |                | periods are    | '30 days') |           |
|                       |                | represented as |            |           |
|                       |                | months         |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.justify\_hours(i | interval       | Adjust         | justify\_h | 1 day     |
| nterval)              |                | interval so    | ours(inter |           |
|                       |                | 24-hour time   | val        |           |
|                       |                | periods are    | '24        |           |
|                       |                | represented as | hours')    |           |
|                       |                | days           |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.justify\_interva | interval       | Adjust         | justify\_i | 29 days   |
| l(interval)           |                | interval using | nterval(in | 23:00:00  |
|                       |                | justify\_days  | terval     |           |
|                       |                | and            | '1 mon -1  |           |
|                       |                | justify\_hours | hour')     |           |
|                       |                | ,              |            |           |
|                       |                | with           |            |           |
|                       |                | additional     |            |           |
|                       |                | sign           |            |           |
|                       |                | adjustments    |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.now()            | timestamp with | Current date   |            |           |
|                       | time zone      | and time       |            |           |
|                       |                | (start of      |            |           |
|                       |                | current        |            |           |
|                       |                | transaction)   |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.statement\_times | timestamp with | Current date   |            |           |
| tamp()                | time zone      | and time       |            |           |
|                       |                | (start of      |            |           |
|                       |                | current        |            |           |
|                       |                | statement)     |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.timeofday()      | text           | Current date   |            |           |
|                       |                | and time (like |            |           |
|                       |                | clock\_timesta |            |           |
|                       |                | mp,            |            |           |
|                       |                | but as a text  |            |           |
|                       |                | string)        |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.transaction\_tim | timestamp with | Current date   |            |           |
| estamp()              | time zone      | and time       |            |           |
|                       |                | (start of      |            |           |
|                       |                | current        |            |           |
|                       |                | transaction)   |            |           |
+-----------------------+----------------+----------------+------------+-----------+

Date and Time Formatting Directives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+----------------+
| Pattern    | Description    |
+============+================+
| HH         | hour of day    |
|            | (01-12)        |
+------------+----------------+
| HH12       | hour of day    |
|            | (01-12)        |
+------------+----------------+
| HH24       | hour of day    |
|            | (00-23)        |
+------------+----------------+
| MI         | minute (00-59) |
+------------+----------------+
| SS         | second (00-59) |
+------------+----------------+
| MS         | millisecond    |
|            | (000-999)      |
+------------+----------------+
| US         | microsecond    |
|            | (000000-999999 |
|            | )              |
+------------+----------------+
| SSSS       | seconds past   |
|            | midnight       |
|            | (0-86399)      |
+------------+----------------+
| AM or A.M. | meridian       |
| or PM or   | indicator      |
| P.M.       | (uppercase)    |
+------------+----------------+
| am or a.m. | meridian       |
| or pm or   | indicator      |
| p.m.       | (lowercase)    |
+------------+----------------+
| Y,YYY      | year (4 and    |
|            | more digits)   |
|            | with comma     |
+------------+----------------+
| YYYY       | year (4 and    |
|            | more digits)   |
+------------+----------------+
| YYY        | last 3 digits  |
|            | of year        |
+------------+----------------+
| YY         | last 2 digits  |
|            | of year        |
+------------+----------------+
| Y          | last digit of  |
|            | year           |
+------------+----------------+
| IYYY       | ISO year (4    |
|            | and more       |
|            | digits)        |
+------------+----------------+
| IYY        | last 3 digits  |
|            | of ISO year    |
+------------+----------------+
| IY         | last 2 digits  |
|            | of ISO year    |
+------------+----------------+
| I          | last digits of |
|            | ISO year       |
+------------+----------------+
| BC or B.C. | era indicator  |
| or AD or   | (uppercase)    |
| A.D.       |                |
+------------+----------------+
| bc or b.c. | era indicator  |
| or ad or   | (lowercase)    |
| a.d.       |                |
+------------+----------------+
| MONTH      | full uppercase |
|            | month name     |
|            | (blank-padded  |
|            | to 9 chars)    |
+------------+----------------+
| Month      | full           |
|            | mixed-case     |
|            | month name     |
|            | (blank-padded  |
|            | to 9 chars)    |
+------------+----------------+
| month      | full lowercase |
|            | month name     |
|            | (blank-padded  |
|            | to 9 chars)    |
+------------+----------------+
| MON        | abbreviated    |
|            | uppercase      |
|            | month name (3  |
|            | chars)         |
+------------+----------------+
| Mon        | abbreviated    |
|            | mixed-case     |
|            | month name (3  |
|            | chars)         |
+------------+----------------+
| mon        | abbreviated    |
|            | lowercase      |
|            | month name (3  |
|            | chars)         |
+------------+----------------+
| MM         | month number   |
|            | (01-12)        |
+------------+----------------+
| DAY        | full uppercase |
|            | day name       |
|            | (blank-padded  |
|            | to 9 chars)    |
+------------+----------------+
| Day        | full           |
|            | mixed-case day |
|            | name           |
|            | (blank-padded  |
|            | to 9 chars)    |
+------------+----------------+
| day        | full lowercase |
|            | day name       |
|            | (blank-padded  |
|            | to 9 chars)    |
+------------+----------------+
| DY         | abbreviated    |
|            | uppercase day  |
|            | name (3 chars) |
+------------+----------------+
| Dy         | abbreviated    |
|            | mixed-case day |
|            | name (3 chars) |
+------------+----------------+
| dy         | abbreviated    |
|            | lowercase day  |
|            | name (3 chars) |
+------------+----------------+
| DDD        | day of year    |
|            | (001-366)      |
+------------+----------------+
| DD         | day of month   |
|            | (01-31)        |
+------------+----------------+
| D          | day of week    |
|            | (1-7; Sunday   |
|            | is 1)          |
+------------+----------------+
| W          | week in month  |
|            | (1-5) (The     |
|            | first week     |
|            | starts on the  |
|            | first day of   |
|            | the month.)    |
+------------+----------------+
| WW         | week number in |
|            | year (1-53)    |
|            | (The first     |
|            | week starts on |
|            | the first day  |
|            | of the year.)  |
+------------+----------------+
| IW         | ISO week       |
|            | number of year |
|            | (The first     |
|            | Thursday of    |
|            | the new year   |
|            | is in week 1.) |
+------------+----------------+
| CC         | century (2     |
|            | digits)        |
+------------+----------------+
| J          | Julian Day     |
|            | (days since    |
|            | January 1,     |
|            | 4712 BC)       |
+------------+----------------+
| Q          | quarter        |
+------------+----------------+
| RM         | month in Roman |
|            | numerals       |
|            | (I-XII;        |
|            | I=January)     |
|            | (uppercase)    |
+------------+----------------+
| rm         | month in Roman |
|            | numerals       |
|            | (i-xii;        |
|            | i=January)     |
|            | (lowercase)    |
+------------+----------------+
| TZ         | time-zone name |
|            | (uppercase)    |
+------------+----------------+
| tz         | time-zone name |
|            | (lowercase)    |
+------------+----------------+

.. todo:: Add screenshots
