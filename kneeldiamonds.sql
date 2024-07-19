CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE 'Styles'
(
    'id' INTEGER NOT NULL PRIMARY KEY auto_increment,
    'style' NVARCHAR(100) NOT NULL,
    'price' NUMERIC(5,2) NOT NULL
);

CREATE TABLE 'Sizes'
(
    'id' INTEGER NOT NULL PRIMARY KEY auto_increment,
    'carets' INTEGER NOT NULL,
    'pricce' NUMERIC(5,2) NOT NULL
);

CREATE TABLE Orders
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    metal_id INTEGER NOT NULL,
    size_id INTEGER NOT NULL,
    style_id INTEGER NOT NULL,
    FOREIGN KEY (metal_id) REFERENCES Metals(id),
    FOREIGN KEY (size_id) REFERENCES Sizes(id),
    FOREIGN KEY (style_id) REFERENCES Styles(id)
);


INSERT INTO 'Metals' VALUES (null, 'Sterling Sliver', 12.00);
INSERT INTO 'Metals' VALUES (null, '14K Gold', 700.00);
INSERT INTO 'Metals' VALUES (null, '24K Gold', 1200.00);
INSERT INTO 'Metals' VALUES (null, 'Platinum', 790.00);
INSERT INTO 'Metals' VALUES (null, 'Palladium', 1300.00);

INSERT INTO 'Styles' VALUES (null, 'Classic', 500);
INSERT INTO 'Styles' VALUES (null, 'Modern', 710);
INSERT INTO 'Styles' VALUES (null, 'Vintage', 965);

INSERT INTO 'Sizes' VALUES (null, 1, 200);
INSERT INTO 'Sizes' VALUES (null, 2, 400);
INSERT INTO 'Sizes' VALUES (null, 3, 600);
INSERT INTO 'Sizes' VALUES (null, 6, 1000);


INSERT INTO 'Orders' VALUES (null, 1,3,2);
INSERT INTO 'Orders' VALUES (null, 2,1,3);
INSERT INTO 'Orders' VALUES (null, 4,3,6);

