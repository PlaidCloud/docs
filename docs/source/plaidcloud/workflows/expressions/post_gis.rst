.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

PostGIS
============

.. toctree::
   :maxdepth: 2
   :includehidden:

.. sidebar:: This Page

   .. contents::
      :local: 

Analyze provides access to the powerful PostGIS library of functions for
geospatial analysis. The functions available are shown in the following
table and link to instructions on the PostGIS site.

.. Important:: To specify the use of PostGIS functions in expressions,
   prefix the name with func. For example, using ST\_GeogFromText would
   use func.ST\_GeogFromText()

Geometry Constructors
~~~~~~~~~~~~~~~~~~~~~

+-----------------------+-----------------------------+
| Function              | Description                 |
+=======================+=============================+
| ST\_BdPolyFromText <  | Construct a Polygon given   |
| http://postgis.net/do | an arbitrary collection of  |
| cs/manual-2.2/ST_BdPo | closed linestrings as a     |
| lyFromText.html>_     | MultiLineString Well-Known  |
|                       | text representation.        |
+-----------------------+-----------------------------+
| ST\_BdMPolyFromText   | Construct a MultiPolygon    |
| <http://postgis.net/d | given an arbitrary          |
| ocs/manual-2.2/ST_BdM | collection of closed        |
| PolyFromText.html>_   | linestrings as a            |
|                       | MultiLineString text        |
|                       | representation Well-Known   |
|                       | text representation.        |
+-----------------------+-----------------------------+
| ST\_Box2dFromGeoHash  | Return a BOX2D from a       |
| <http://postgis.net/  | GeoHash string.             |
| docs/manual-2.2/ST_Bo |                             |
| x2dFromGeoHash.html>  |                             |
| __                    |                             |
+-----------------------+-----------------------------+
| ST\_GeogFromText <ht  | Return a specified          |
| tp://postgis.net/docs | geography value from        |
| /manual-2.2/ST_GeogFr | Well-Known Text             |
| omText.html>__        | representation or extended  |
|                       | (WKT).                      |
+-----------------------+-----------------------------+
| ST\_GeographyFromTex  | Return a specified          |
| t <http://postgis.net | geography value from        |
| /docs/manual-2.2/ST_G | Well-Known Text             |
| eographyFromText.html | representation or extended  |
| >__                   | (WKT).                      |
+-----------------------+-----------------------------+
| ST\_GeogFromWKB <htt  | Creates a geography         |
| p://postgis.net/docs/ | instance from a Well-Known  |
| manual-2.2/ST_GeogFro | Binary geometry             |
| mWKB.html>__          | representation (WKB) or     |
|                       | extended Well Known Binary  |
|                       | (EWKB).                     |
+-----------------------+-----------------------------+
| ST\_GeomCollFromText  | Makes a collection Geometry |
| <http://postgis.net/  | from collection WKT with    |
| docs/manual-2.2/ST_Ge | the given SRID. If SRID is  |
| omCollFromText.html>  | not give, it defaults to 0. |
| __                    |                             |
+-----------------------+-----------------------------+
| ST\_GeomFromEWKB <ht  | Return a specified          |
| tp://postgis.net/docs | ST\_Geometry value from     |
| /manual-2.2/ST_GeomFr | Extended Well-Known Binary  |
| omEWKB.html>__        | representation (EWKB).      |
+-----------------------+-----------------------------+
| ST\_GeomFromEWKT <ht  | Return a specified          |
| tp://postgis.net/docs | ST\_Geometry value from     |
| /manual-2.2/ST_GeomFr | Extended Well-Known Text    |
| omEWKT.html>__        | representation (EWKT).      |
+-----------------------+-----------------------------+
| ST\_GeometryFromText  | Return a specified          |
| <http://postgis.net/  | ST\_Geometry value from     |
| docs/manual-2.2/ST_Ge | Well-Known Text             |
| ometryFromText.html>  | representation (WKT). This  |
| __                    | is an alias name for        |
|                       | ST\_GeomFromText            |
+-----------------------+-----------------------------+
| ST\_GeomFromGeoHash   | Return a geometry from a    |
| <http://postgis.net/d | GeoHash string.             |
| ocs/manual-2.2/ST_Geo |                             |
| mFromGeoHash.html>__  |                             |
+-----------------------+-----------------------------+
| ST\_GeomFromGML <htt  | Takes as input GML          |
| p://postgis.net/docs/ | representation of geometry  |
| manual-2.2/ST_GeomFro | and outputs a PostGIS       |
| mGML.html>__          | geometry object             |
+-----------------------+-----------------------------+
| ST\_GeomFromGeoJSON   | Takes as input a geojson    |
| <http://postgis.net/d | representation of a         |
| ocs/manual-2.2/ST_Geo | geometry and outputs a      |
| mFromGeoJSON.html>__  | PostGIS geometry object     |
+-----------------------+-----------------------------+
| ST\_GeomFromKML <htt  | Takes as input KML          |
| p://postgis.net/docs/ | representation of geometry  |
| manual-2.2/ST_GeomFro | and outputs a PostGIS       |
| mKML.html>__          | geometry object             |
+-----------------------+-----------------------------+
| ST\_GMLToSQL <http:/  | Return a specified          |
| /postgis.net/docs/man | ST\_Geometry value from GML |
| ual-2.2/ST_GMLToSQL.h | representation. This is an  |
| tml>__                | alias name for              |
|                       | ST\_GeomFromGML             |
+-----------------------+-----------------------------+
| ST\_GeomFromText <ht  | Return a specified          |
| tp://postgis.net/docs | ST\_Geometry value from     |
| /manual-2.2/ST_GeomFr | Well-Known Text             |
| omText.html>__        | representation (WKT).       |
+-----------------------+-----------------------------+
| ST\_GeomFromWKB <htt  | Creates a geometry instance |
| p://postgis.net/docs/ | from a Well-Known Binary    |
| manual-2.2/ST_GeomFro | geometry representation     |
| mWKB.html>__          | (WKB) and optional SRID.    |
+-----------------------+-----------------------------+
| ST\_LineFromEncodedP  | Creates a LineString from   |
| olyline <http://postg | an Encoded Polyline.        |
| is.net/docs/manual-2. |                             |
| 2/ST_LineFromEncodedP |                             |
| olyline.html>__       |                             |
+-----------------------+-----------------------------+
| ST\_LineFromMultiPoi  | Creates a LineString from a |
| nt <http://postgis.ne | MultiPoint geometry.        |
| t/docs/manual-2.2/    |                             |
| ST_LineFromMultiPoint |                             |
| .html>__              |                             |
+-----------------------+-----------------------------+
| ST\_LineFromText <ht  | Makes a Geometry from WKT   |
| tp://postgis.net/docs | representation with the     |
| /manual-2.2/ST_LineFr | given SRID. If SRID is not  |
| omText.html>__        | given, it defaults to 0.    |
+-----------------------+-----------------------------+
| ST\_LineFromWKB <htt  | Makes a LINESTRING from WKB |
| p://postgis.net/docs/ | with the given SRID         |
| manual-2.2/ST_LineFro |                             |
| mWKB.html>__          |                             |
+-----------------------+-----------------------------+
| ST\_LinestringFromWK  | Makes a geometry from WKB   |
| B <http://postgis.net | with the given SRID.        |
| /docs/manual-2.2/ST_L |                             |
| inestringFromWKB.html |                             |
| >__                   |                             |
+-----------------------+-----------------------------+
| ST\_MakeBox2D <http:  | Creates a BOX2D defined by  |
| //postgis.net/docs/ma | the given point geometries. |
| nual-2.2/ST_MakeBox2D |                             |
| .html>__              |                             |
+-----------------------+-----------------------------+
| ST\_3DMakeBox <http:  | Creates a BOX3D defined by  |
| //postgis.net/docs/ma | the given 3d point          |
| nual-2.2/ST_3DMakeBox | geometries.                 |
| .html>__              |                             |
+-----------------------+-----------------------------+
| ST\_MakeLine <http:/  | Creates a Linestring from   |
| /postgis.net/docs/man | point or line geometries.   |
| ual-2.2/ST_MakeLine.h |                             |
| tml>__                |                             |
+-----------------------+-----------------------------+
| ST\_MakeEnvelope <ht  | Creates a rectangular       |
| tp://postgis.net/docs | Polygon formed from the     |
| /manual-2.2/ST_MakeEn | given minimums and          |
| velope.html>__        | maximums. Input values must |
|                       | be in SRS specified by the  |
|                       | SRID                        |
+-----------------------+-----------------------------+
| ST\_MakePolygon <htt  | Creates a Polygon formed by |
| p://postgis.net/docs/ | the given shell. Input      |
| manual-2.2/ST_MakePol | geometries must be closed   |
| ygon.html>__          | LINESTRINGS.                |
+-----------------------+-----------------------------+
| ST\_MakePoint <http:  | Creates a 2D,3DZ or 4D      |
| //postgis.net/docs/ma | point geometry.             |
| nual-2.2/ST_MakePoint |                             |
| .html>__              |                             |
+-----------------------+-----------------------------+
| ST\_MakePointM <http  | Creates a point geometry    |
| ://postgis.net/docs/m | with an x, y, and m         |
| anual-2.2/ST_MakePoin | coordinate.                 |
| tM.html>__            |                             |
+-----------------------+-----------------------------+
| ST\_MLineFromText <h  | Return a specified          |
| ttp://postgis.net/doc | ST\_MultiLineString value   |
| s/manual-2.2/ST_MLine | from WKT representation.    |
| FromText.html>__      |                             |
+-----------------------+-----------------------------+
| ST\_MPointFromText <  | Makes a Geometry from WKT   |
| http://postgis.net/do | with the given SRID. If     |
| cs/manual-2.2/ST_MPoi | SRID is not give, it        |
| ntFromText.html>__    | defaults to 0.              |
+-----------------------+-----------------------------+
| ST\_MPolyFromText <h  | Makes a MultiPolygon        |
| ttp://postgis.net/doc | Geometry from WKT with the  |
| s/manual-2.2/ST_MPoly | given SRID. If SRID is not  |
| FromText.html>__      | give, it defaults to 0.     |
+-----------------------+-----------------------------+
| ST\_Point <http://po  | Returns an ST\_Point with   |
| stgis.net/docs/manual | the given coordinate        |
| -2.2/ST_Point.html>_  | values. OGC alias for       |
| _                     | ST\_MakePoint.              |
+-----------------------+-----------------------------+
| ST\_PointFromGeoHash  | Return a point from a       |
| <http://postgis.net/  | GeoHash string.             |
| docs/manual-2.2/ST_Po |                             |
| intFromGeoHash.html>  |                             |
| __                    |                             |
+-----------------------+-----------------------------+
| ST\_PointFromText <h  | Makes a point Geometry from |
| ttp://postgis.net/doc | WKT with the given SRID. If |
| s/manual-2.2/ST_Point | SRID is not given, it       |
| FromText.html>__      | defaults to unknown.        |
+-----------------------+-----------------------------+
| ST\_PointFromWKB <ht  | Makes a geometry from WKB   |
| tp://postgis.net/docs | with the given SRID         |
| /manual-2.2/ST_PointF |                             |
| romWKB.html>__        |                             |
+-----------------------+-----------------------------+
| ST\_Polygon <http://  | Returns a polygon built     |
| postgis.net/docs/manu | from the specified          |
| al-2.2/ST_Polygon.htm | linestring and SRID.        |
| l>__                  |                             |
+-----------------------+-----------------------------+
| ST\_PolygonFromText   | Makes a Geometry from WKT   |
| <http://postgis.net/d | with the given SRID. If     |
| ocs/manual-2.2/ST_Pol | SRID is not give, it        |
| ygonFromText.html>__  | defaults to 0.              |
+-----------------------+-----------------------------+
| ST\_WKBToSQL <http:/  | Return a specified          |
| /postgis.net/docs/man | ST\_Geometry value from     |
| ual-2.2/ST_WKBToSQL.h | Well-Known Binary           |
| tml>__                | representation (WKB). This  |
|                       | is an alias name for        |
|                       | ST\_GeomFromWKB that takes  |
|                       | no srid                     |
+-----------------------+-----------------------------+
| ST\_WKTToSQL <http:/  | Return a specified          |
| /postgis.net/docs/man | ST\_Geometry value from     |
| ual-2.2/ST_WKTToSQL.h | Well-Known Text             |
| tml>__                | representation (WKT). This  |
|                       | is an alias name for        |
|                       | ST\_GeomFromText            |
+-----------------------+-----------------------------+
