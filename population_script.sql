
INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES ('bla', '2022-05-06 23:45:47','False', 'Ernabla', 'Erna', 'Bla', 'erna@gmail.com', 'False', 'False', '2022-05-06 23:45:47')
INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES ('bla', '2022-05-06 23:45:47','False', 'Stephanbla', 'Stephan', 'Bla', 'stephan@gmail.com', 'False', 'False', '2022-05-06 23:45:47')
INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES ('bla', '2022-05-06 23:45:47','False', 'Bryndisbla', 'Bryndis', 'Bla', 'bryndis@gmail.com', 'False', 'False', '2022-05-06 23:45:47')

INSERT INTO user_userprofile(profile_image, user_id) VALUES ('https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/newscms/2021_07/2233721/171120-smile-stock-njs-333p.jpg', '1')
INSERT INTO user_userprofile(profile_image, user_id) VALUES ('https://img.freepik.com/free-photo/handsome-smiling-young-african-man_171337-9650.jpg?t=st=1652093747~exp=1652094347~hmac=118a4679faea8692112ddb6b1a1e63f7b45acaa60b4f0b58bec9482b4436d7bf&w=1800', '2')
INSERT INTO user_userprofile(profile_image, user_id) VALUES ('https://img.freepik.com/free-photo/beautiful-young-woman-face-closeup-portrait-studio-background-white_100800-8529.jpg?w=826', '3')

INSERT INTO user_profile(profile_image, user_id) VALUES



INSERT INTO product_product (name,description,long_description,condition,on_sale,price,product_category_id,seller_id) VALUES('Shoe', 'Nike','Running shoes', 'good', 'True', '500', '1', '1');
INSERT INTO product_product (name,description,long_description,condition,on_sale,price,product_category_id,seller_id) VALUES('Sweater', 'Puma', 'góð peysa', 'good', 'True', '500', '1', '2');
INSERT INTO product_product (name,description,long_description,condition,on_sale,price,product_category_id,seller_id) VALUES('Top', 'Zara', 'summer vibes', 'good', 'True', '500', '1', '3');
INSERT INTO product_product (name,description,long_description,condition,on_sale,price,product_category_id,seller_id) VALUES('Blanket', 'H&M home', 'kósy', 'bad', 'True', '500', '3', '1');
INSERT INTO product_product (name,description,long_description,condition,on_sale,price,product_category_id,seller_id) VALUES('Toy car', 'Cars', 'bíll', 'good', 'True', '500', '2', '3');


INSERT INTO product_productcategory (name_category) VALUES('clothes');
INSERT INTO product_productcategory (name_category) VALUES('toys');
INSERT INTO product_productcategory (name_category) VALUES('home');


INSERT INTO product_productimage (image, product_id) VALUES('https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/skwgyqrbfzhu6uyeh0gg/air-max-270-mens-shoes-KkLcGR.png', 1);
INSERT INTO product_productimage (image, product_id) VALUES('https://n.nordstrommedia.com/id/sr3/d067f8a3-2429-4561-86bd-a28bafd07379.jpeg?crop=pad&pad_color=FFF&format=jpeg&w=780&h=1196&dpr=2', 2);
INSERT INTO product_productimage (image, product_id) VALUES('https://static.zara.net/photos///2022/V/0/1/p/2320/453/250/2/w/1126/2320453250_6_1_1.jpg?ts=1651051703912', 3);
INSERT INTO product_productimage (image, product_id) VALUES('https://design-milk.com/images/2022/02/cozythrowsroundup-featuredimage-studiovariously-salviathrow-designmilkshop.jpg', 4);
INSERT INTO product_productimage (image, product_id) VALUES('https://m.media-amazon.com/images/I/71Phdb+rknL._AC_SL1500_.jpg', 5);
