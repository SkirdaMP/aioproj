create TABLE post (
    id serial,
    title VARCHAR(255) not NULL,
    g_url VARCHAR(400),
    save_url varchar(255)
);
 INSERT into post (title, g_url, save_url) values ('1', '2', '3');