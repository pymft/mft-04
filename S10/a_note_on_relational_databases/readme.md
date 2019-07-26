# A Note On Relational Database

## `sqlite3`

* [online sqlite editor](https://sqliteonline.com/)
* [download sample database](http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip)
* [sqlite tutorialspoint](https://www.tutorialspoint.com/sqlite/)


longest Rock track 

```sql 
SELECT tracks.name, tracks.composer, artists.name, albums.title, genres.name, tracks.milliseconds/60000 as mins FROM tracks 
JOIN albums ON tracks.albumid = albums.albumid
JOIN artists ON artists.artistid = albums.artistid
JOIN genres ON tracks.genreid = genres.genreid
WHERE genres.name = 'Rock'
ORDER BY tracks.milliseconds DESC
; 
```