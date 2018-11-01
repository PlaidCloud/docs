.. toctree::
   :maxdepth: 2
   :includehidden:

Text Expressions
~~~~~~~~~~~~~~~~~

+-----------------------+----------------+----------------+------------+-----------+
| Analyze Expression    | Return Type    | Description    | Example    | Result    |
+=======================+================+================+============+===========+
| func.concat(string,   | text           | String         | concat('Po | PostgreSQ |
| string)               |                | concatenation  | st',       | L         |
|                       |                |                | 'greSQL')  |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.bit\_length(stri | int            | Number of bits | bit\_lengt | 32        |
| ng)                   |                | in string      | h('jose')  |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.char\_length(str | int            | Number of      | char\_leng | 4         |
| ing)                  |                | characters in  | th('jose') |           |
| or                    |                | string         |            |           |
| func.character\_lengt |                |                |            |           |
| h(string)             |                |                |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.convert(string   | text           | Change         | convert('P | PostgreSQ |
| using                 |                | encoding using | ostgreSQL' | L'        |
| conversion\_name)     |                | specified      | using      | in UTF8   |
|                       |                | conversion     | iso\_8859\ | (Unicode, |
|                       |                | name.          | _1\_to\_ut | 8-bit)    |
|                       |                | Conversions    | f8)        | encoding  |
|                       |                | can be defined |            |           |
|                       |                | by CREATE      |            |           |
|                       |                | CONVERSION.    |            |           |
|                       |                | Also there are |            |           |
|                       |                | some           |            |           |
|                       |                | pre-defined    |            |           |
|                       |                | conversion     |            |           |
|                       |                | names.         |            |           |
|                       |                | SeeTable       |            |           |
|                       |                | 9-7for         |            |           |
|                       |                | available      |            |           |
|                       |                | conversion     |            |           |
|                       |                | names.         |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.lower(string)    | text           | Convert string | lower('TOM | tom       |
|                       |                | to lower case  | ')         |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.octet\_length(st | int            | Number of      | octet\_len | 4         |
| ring)                 |                | bytes in       | gth('jose' |           |
|                       |                | string         | )          |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.overlay(string   | text           | Replace        | overlay('T | Thomas    |
| placing string from   |                | substring      | xxxxas'    |           |
| int [forint])         |                |                | placing    |           |
|                       |                |                | 'hom' from |           |
|                       |                |                | 2 for 4)   |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.position(substri | int            | Location of    | position(' | 3         |
| ng                    |                | specified      | om'        |           |
| in string)            |                | substring      | in         |           |
|                       |                |                | 'Thomas')  |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.substring(string | text           | Extract        | substring( | hom       |
| [from int] [for int]) |                | substring      | 'Thomas'   |           |
|                       |                |                | from 2 for |           |
|                       |                |                | 3)         |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.substring(string | text           | Extract        | substring( | mas       |
| frompattern)          |                | substring      | 'Thomas'   |           |
|                       |                | matching POSIX | from       |           |
|                       |                | regular        | '...$')    |           |
|                       |                | expression.    |            |           |
|                       |                | SeeSection     |            |           |
|                       |                | 9.7for more    |            |           |
|                       |                | information on |            |           |
|                       |                | pattern        |            |           |
|                       |                | matching.      |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.substring(string | text           | Extract        | substring( | oma       |
| frompatternforescape) |                | substring      | 'Thomas'   |           |
|                       |                | matching SQL   | from       |           |
|                       |                | regular        | '%#"o\_a#" |           |
|                       |                | expression.    | \_'        |           |
|                       |                | SeeSection     | for '#')   |           |
|                       |                | 9.7for more    |            |           |
|                       |                | information on |            |           |
|                       |                | pattern        |            |           |
|                       |                | matching.      |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.trim([leading,   | text           | Remove the     | trim(both  | Tom       |
| trailing, both]       |                | longest string | 'x' from   |           |
| [characters] from     |                | containing     | 'xTomxx')  |           |
| string)               |                | only the       |            |           |
|                       |                | characters (a  |            |           |
|                       |                | space by       |            |           |
|                       |                | default) from  |            |           |
|                       |                | the            |            |           |
|                       |                | start/end/both |            |           |
|                       |                | ends of the    |            |           |
|                       |                | string         |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.upper(string)    | text           | Convert string | upper('tom | TOM       |
|                       |                | to uppercase   | ')         |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.ascii(string)    | int            | ASCII code of  | ascii('x') | 120       |
|                       |                | the first byte |            |           |
|                       |                | of the         |            |           |
|                       |                | argument       |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.btrim(string     | text           | Remove the     | btrim('xyx | trim      |
| text [, characters    |                | longest string | trimyyx',  |           |
| text])                |                | consisting     | 'xy')      |           |
|                       |                | only of        |            |           |
|                       |                | characters in  |            |           |
|                       |                | characters (a  |            |           |
|                       |                | space by       |            |           |
|                       |                | default) from  |            |           |
|                       |                | the start and  |            |           |
|                       |                | end of string  |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.chr(int)         | text           | Character with | chr(65)    | A         |
|                       |                | the given      |            |           |
|                       |                | ASCII code     |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.convert(string   | text           | Convert string | convert(   | text\_in\ |
| text, [src\_encoding  |                | to             | 'text\_in\ | _utf8     |
| name,]dest\_encoding  |                | dest\_encoding | _utf8',    | represent |
| name)                 |                | .              | 'UTF8',    | ed        |
|                       |                | The original   | 'LATIN1')  | in ISO    |
|                       |                | encoding is    |            | 8859-1    |
|                       |                | specified by   |            | encoding  |
|                       |                | src\_encoding. |            |           |
|                       |                | If             |            |           |
|                       |                | src\_encoding  |            |           |
|                       |                | is omitted,    |            |           |
|                       |                | database       |            |           |
|                       |                | encoding is    |            |           |
|                       |                | assumed.       |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.decode(string    |                | Decode binary  |            |           |
| text, type text)      |                | data from      |            |           |
|                       |                | string         |            |           |
|                       |                | previously     |            |           |
|                       |                | encoded with   |            |           |
|                       |                | encode.        |            |           |
|                       |                | Parameter type |            |           |
|                       |                | is same as in  |            |           |
|                       |                | encode.        |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.decode(string    | bytea          | Decode binary  |            |           |
| text, type text)      |                | data from      |            |           |
|                       |                | string         |            |           |
|                       |                | previously     |            |           |
|                       |                | encoded with   |            |           |
|                       |                | encode.        |            |           |
|                       |                | Parameter type |            |           |
|                       |                | is same as in  |            |           |
|                       |                | encode.        |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.initcap(string)  | text           | Convert the    | initcap('h | Hi Thomas |
|                       |                | first letter   | i          |           |
|                       |                | of each word   | THOMAS')   |           |
|                       |                | to uppercase   |            |           |
|                       |                | and the rest   |            |           |
|                       |                | to lowercase.  |            |           |
|                       |                | Words are      |            |           |
|                       |                | sequences of   |            |           |
|                       |                | alphanumeric   |            |           |
|                       |                | characters     |            |           |
|                       |                | separated by   |            |           |
|                       |                | non-alphanumer |            |           |
|                       |                | ic             |            |           |
|                       |                | characters.    |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.length(string)   | int            | Number of      | length('jo | 4         |
|                       |                | characters in  | se')       |           |
|                       |                | string         |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.lpad(string      | text           | Fill up the    | lpad('hi', | xyxhi     |
| text, length int [,   |                | string to      | 5, 'xy')   |           |
| fill text])           |                | length length  |            |           |
|                       |                | by prepending  |            |           |
|                       |                | the characters |            |           |
|                       |                | fill (a space  |            |           |
|                       |                | by default).   |            |           |
|                       |                | If the string  |            |           |
|                       |                | is already     |            |           |
|                       |                | longer than    |            |           |
|                       |                | length then it |            |           |
|                       |                | is truncated   |            |           |
|                       |                | (on the        |            |           |
|                       |                | right).        |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.ltrim(string     | text           | Remove the     | ltrim('zzz | trim      |
| text [, characters    |                | longest string | ytrim',    |           |
| text])                |                | containing     | 'xyz')     |           |
|                       |                | only           |            |           |
|                       |                | characters     |            |           |
|                       |                | from           |            |           |
|                       |                | characters (a  |            |           |
|                       |                | space by       |            |           |
|                       |                | default) from  |            |           |
|                       |                | the start of   |            |           |
|                       |                | string         |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.md5(string)      | text           | Calculates the | md5('abc') | 900150983 |
|                       |                | MD5 hash of    |            | cd24fb0   |
|                       |                | string,        |            | d6963f7d2 |
|                       |                | returning the  |            | 8e17f72   |
|                       |                | result in      |            |           |
|                       |                | hexadecimal    |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.quote\_literal(s | text           | Return the     | quote\_lit | O''Reilly |
| tring)                |                | given string   | eral(      | '         |
|                       |                | suitably       | 'O'Reilly' |           |
|                       |                | quoted to be   | )          |           |
|                       |                | used as a      |            |           |
|                       |                | string literal |            |           |
|                       |                | in an SQL      |            |           |
|                       |                | statement      |            |           |
|                       |                | string.        |            |           |
|                       |                | Embedded       |            |           |
|                       |                | single-quotes  |            |           |
|                       |                | and            |            |           |
|                       |                | backslashes    |            |           |
|                       |                | are properly   |            |           |
|                       |                | doubled.       |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.regexp\_replace( | text           | Replace        | regexp\_re | ThM       |
| string                |                | substring      | place('Tho |           |
| text, pattern         |                | matching POSIX | mas',      |           |
| text,replacement text |                | regular        | '.[mN]a.', |           |
| [,flags text])        |                | expression.    | 'M')       |           |
|                       |                | SeeSection     |            |           |
|                       |                | 9.7for more    |            |           |
|                       |                | information on |            |           |
|                       |                | pattern        |            |           |
|                       |                | matching.      |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.repeat(string    | text           | Repeat string  | repeat('Pg | PgPgPgPg  |
| text, number int)     |                | the specified  | ',         |           |
|                       |                | number of      | 4)         |           |
|                       |                | times          |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.replace(string   | text           | Replace all    | replace(   | abXXefabX |
| text, from text, to   |                | occurrences in | 'abcdefabc | Xef       |
| text)                 |                | string of      | def',      |           |
|                       |                | substring from | 'cd',      |           |
|                       |                | with substring | 'XX')      |           |
|                       |                | to             |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.rpad(string      | text           | Fill up the    | rpad('hi', | hixyx     |
| text, length int [,   |                | string to      | 5, 'xy')   |           |
| fill text])           |                | length length  |            |           |
|                       |                | by appending   |            |           |
|                       |                | the characters |            |           |
|                       |                | fill (a space  |            |           |
|                       |                | by default).   |            |           |
|                       |                | If the string  |            |           |
|                       |                | is already     |            |           |
|                       |                | longer than    |            |           |
|                       |                | length then it |            |           |
|                       |                | is truncated.  |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.rtrim(string     | text           | Remove the     | rtrim('tri | trim      |
| text [, characters    |                | longest string | mxxxx',    |           |
| text])                |                | containing     | 'x')       |           |
|                       |                | only           |            |           |
|                       |                | characters     |            |           |
|                       |                | from           |            |           |
|                       |                | characters (a  |            |           |
|                       |                | space by       |            |           |
|                       |                | default) from  |            |           |
|                       |                | the end of     |            |           |
|                       |                | string         |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.split\_part(stri | text           | Split string   | split\_par | def       |
| ng                    |                | on delimiter   | t('abc\ :s |           |
| text, delimiter text, |                | and return the | ub:`@`\ de |           |
| field int)            |                | given field    | f\ :sub:`@ |           |
|                       |                | (counting from | `\ ghi',   |           |
|                       |                | one)           | ':sub:`@`' |           |
|                       |                |                | ,          |           |
|                       |                |                | 2)         |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.strpos(string,   | int            | Location of    | strpos('hi | 2         |
| substring)            |                | specified      | gh',       |           |
|                       |                | substring      | 'ig')      |           |
|                       |                | (same as       |            |           |
|                       |                | position(subst |            |           |
|                       |                | ring           |            |           |
|                       |                | in string),    |            |           |
|                       |                | but note the   |            |           |
|                       |                | reversed       |            |           |
|                       |                | argument       |            |           |
|                       |                | order)         |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.substr(string,   | text           | Extract        | substr('al | ph        |
| from [, count])       |                | substring      | phabet',   |           |
|                       |                | (same as       | 3, 2)      |           |
|                       |                | substring(stri |            |           |
|                       |                | ng             |            |           |
|                       |                | from from for  |            |           |
|                       |                | count))        |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.to\_ascii(string | text           | Convert string | to\_ascii( | Karel     |
| text [, encoding      |                | to ASCII from  | 'Karel')   |           |
| text])                |                | another        |            |           |
|                       |                | encoding (only |            |           |
|                       |                | supports       |            |           |
|                       |                | conversion     |            |           |
|                       |                | from LATIN1,   |            |           |
|                       |                | LATIN2,        |            |           |
|                       |                | LATIN9, and    |            |           |
|                       |                | WIN1250        |            |           |
|                       |                | encodings)     |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.to\_hex(number   | text           | Convert number | to\_hex(21 | 7fffffff  |
| int or bigint)        |                | to its         | 47483647)  |           |
|                       |                | equivalent     |            |           |
|                       |                | hexadecimal    |            |           |
|                       |                | representation |            |           |
+-----------------------+----------------+----------------+------------+-----------+
| func.translate(string | text           | Any character  | translate( | a23x5     |
| text, from text, to   |                | in string that | '12345',   |           |
| text)                 |                | matches a      | '14',      |           |
|                       |                | character in   | 'ax')      |           |
|                       |                | the from set   |            |           |
|                       |                | is replaced by |            |           |
|                       |                | the            |            |           |
|                       |                | corresponding  |            |           |
|                       |                | character in   |            |           |
|                       |                | the to set     |            |           |
+-----------------------+----------------+----------------+------------+-----------+

.. todo:: fix function.encode function.decode.  

.. todo:: Add screenshots