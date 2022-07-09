select album_name, release_year from albums 
where release_year = '2018-01-01';

select track_name, lenght from tracks 
order by lenght desc 
limit 1;

select track_name from tracks 
where lenght >= '00:03:30';

select collection_name from collections
where release_year between '2018-01-01' and '2020-01-01';

select artist_name from artists
where artist_name not like '% %';

select track_name from tracks 
where track_name like '%My%' or track_name like '%мой%';