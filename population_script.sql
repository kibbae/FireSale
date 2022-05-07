
INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES ('bla', '2022-05-06 23:45:47','False', 'Ernabla', 'Erna', 'Bla', 'erna@gmail.com', 'False', 'False', '2022-05-06 23:45:47')
INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES ('bla', '2022-05-06 23:45:47','False', 'Stephanbla', 'Stephan', 'Bla', 'stephan@gmail.com', 'False', 'False', '2022-05-06 23:45:47')
INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES ('bla', '2022-05-06 23:45:47','False', 'Bryndisbla', 'Bryndis', 'Bla', 'bryndis@gmail.com', 'False', 'False', '2022-05-06 23:45:47')

INSERT INTO user_profile(profile_image, user_id) VALUES ('https://www.jeancoutu.com/catalog-images/888729/viewer/0/ferrero-canada-limited-ferrero-rocher-200-g.png', '6')
INSERT INTO user_profile(profile_image, user_id) VALUES ('https://www.haribo.com/fileadmin/upload/USA/Startpage/products/cola_pack.png', '1')
INSERT INTO user_profile(profile_image, user_id) VALUES ('https://cdn.shopify.com/s/files/1/0972/7116/products/haribo-happy-cola-bulk.png?v=1459346724', '3')
INSERT INTO user_profile(profile_image, user_id) VALUES ('https://www.tictacuk.com/image/journal/article?img_id=18506308&t=1536579236701', '4')
INSERT INTO user_profile(profile_image, user_id) VALUES ('https://www.tictacuk.com/image/journal/article?img_id=18506308&t=1536579236701', '7')

INSERT INTO product_product (name,description,long_description,product_category,seller,condition,on_sale,price) VALUES('Shoe', 'Nike','this is the beginning of something', 'clothes', 'kibba', 'good', 'True', '500');
INSERT INTO product_product (name,description,long_description,product_category,seller,condition,on_sale,price) VALUES('Sweater', 'Puma', 'this is the beginning of something', 'clothes', 'kibba', 'good', 'True', '500');
INSERT INTO product_product (name,description,long_description,product_category,seller,condition,on_sale,price) VALUES('Top', 'Zara', 'this is the beginning of something', 'clothes', 'kibba', 'good', 'True', '500');
INSERT INTO product_product (name,description,long_description,product_category,seller,condition,on_sale,price) VALUES('Blanket', 'H&M home', 'this is the beginning of something', 'home', 'kibba', 'bad', 'True', '500');
INSERT INTO product_product (name,description,long_description,product_category,seller,condition,on_sale,price) VALUES('Toy car', 'Cars', 'this is the beginning of something', 'toys', 'kibba', 'good', 'True', '500');
INSERT INTO product_product (name,description,long_description,product_category,seller,condition,on_sale,price) VALUES('Shoe', 'this is the beginning of something');
INSERT INTO product_product (name,description,long_description,product_category,seller,condition,on_sale,price) VALUES('Shoe', 'this is the beginning of something');
INSERT INTO product_product (name,description,long_description,product_category,seller,condition,on_sale,price) VALUES('Shoe', 'this is the beginning of something');

INSERT INTO product_productcategory (name) VALUES('clothes');
INSERT INTO product_productcategory (name) VALUES('toys');
INSERT INTO product_productcategory (name) VALUES('home');


INSERT INTO product_productimage (image, product_id) VALUES('https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/skwgyqrbfzhu6uyeh0gg/air-max-270-mens-shoes-KkLcGR.png', 1);
INSERT INTO product_productimage (image, product_id) VALUES('https://n.nordstrommedia.com/id/sr3/d067f8a3-2429-4561-86bd-a28bafd07379.jpeg?crop=pad&pad_color=FFF&format=jpeg&w=780&h=1196&dpr=2', 2);
INSERT INTO product_productimage (image, product_id) VALUES('https://static.zara.net/photos///2022/V/0/1/p/2320/453/250/2/w/1126/2320453250_6_1_1.jpg?ts=1651051703912', 3);
INSERT INTO product_productimage (image, product_id) VALUES('https://design-milk.com/images/2022/02/cozythrowsroundup-featuredimage-studiovariously-salviathrow-designmilkshop.jpg', 4);
INSERT INTO product_productimage (image, product_id) VALUES('https://m.media-amazon.com/images/I/71Phdb+rknL._AC_SL1500_.jpg', 5);
INSERT INTO product_productimage (image, product_id) VALUES('https://talenthouse-res.cloudinary.com/image/upload/c_limit,h_1280,q_90,w_480/v1/invites/kv4pahmpydnmidlzroaj.png', 3);
INSERT INTO product_productimage (image, product_id) VALUES('https://www.haribo.com/fileadmin/upload/USA/Startpage/products/cola_pack.png', 4);
INSERT INTO product_productimage (image, product_id) VALUES('https://cdn.shopify.com/s/files/1/0972/7116/products/haribo-happy-cola-bulk.png?v=1459346724', 4);
INSERT INTO product_productimage (image, product_id) VALUES('https://www.haribo.com/fileadmin/upload/USA/Startpage/products/gb_pack.png', 5);
INSERT INTO product_productimage (image, product_id) VALUES('https://cdn.shopify.com/s/files/1/0972/7116/products/haribo-original-gold-bear-gummies.png?v=1482867150', 5);
INSERT INTO product_productimage (image, product_id) VALUES('https://www.haribo.com/enUS/world/fileadmin/_processed_/4/6/csm_fizzcola-h_8c4e625740.png', 6);
INSERT INTO product_productimage (image, product_id) VALUES('https://www.haribo.com/enUS/world/fileadmin/user_upload/USA/top_products/fizzy_Cola/fizzycola-pieces.jpg', 6);
INSERT INTO product_productimage (image, product_id) VALUES('http://paradisealacarte.com/wp-content/uploads/2016/10/0030.png',7);



