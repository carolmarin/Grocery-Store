#Carol Marin

create table store (
	store_id int(4) not null,
	state_id varchar(6) not null,
	state_name varchar(100) not null,
	primary key (store_id, state_id));
create table customers (
	customer_id int(6) not null auto_increment,
	customer_first varchar(50) not null,
	customer_last varchar(50) not null,
	balance numeric(8,2) default 0,
	primary key (customer_id));
create table customers_delv_address (
	delv_addr_id int(6) not null auto_increment,
	customer_id int(6) not null,
	delv_street varchar(100) not null,
	delv_street2 varchar(100) default null,
	delv_city varchar(100) not null,
	delv_state varchar(100) not null,
	delv_zipcode varchar(15) not null,
	primary key (delv_addr_id),
	foreign key (customer_id) references customers(customer_id));
create table customers_bill_address (
	bill_addr_id int(6) not null auto_increment,
	customer_id int(6) not null,
	bill_street varchar(100) not null,
	bill_street2 varchar(100) default null,
	bill_city varchar(100) not null,
	bill_state varchar(100) not null,
	bill_zipcode varchar(15) not null,
	primary key (bill_addr_id),
	foreign key (customer_id) references customers(customer_id));
create table customer_payment (
	payment_id int(6) not null auto_increment,
	customer_id int(6) not null,
	bill_addr_id int(6) not null,
	card_number int(16) not null,
	exp_date date() not null,
	cvv int(3) not null,
	primary key (payment_id),
	foreign key (customer_id) references customers(customer_id),
	foreign key (bill_addr_id) references customers_bill_address(bill_addr_id));
create table staff (
	staff_id int(6) not null auto_increment,
	staff_first varchar(50) not null,
	staff_last varchar(50) not null,
	salary numeric(8,2) default 0,
	job_title varchar(25) not null,
	primary key (staff_id));
create table staff_address (
	staff_addr_id int(6) not null auto_increment,
	staff_id int(6) not null,
	staff_street varchar(100) not null,
	staff_street2 varchar(100) default null,
	staff_city varchar(100) not null,
	staff_state varchar(100) not null,
	staff_zipcode varchar(15) not null,
	primary key (staff_addr_id),
	foreign key (staff_id) references staff(staff_id));
create table product (
	product_id int(10) not null auto_increment,
	product_name varchar(100) not null,
	product_type varchar(20) not null,
	product_information varchar(250) not null,
	check (product_type in ('Dairy', 'Meat', 'Fruit', 'Vegetables', 'Grain', 'Drinks', 'Alcohol'))
	primary key (product_id));
create table attributes (
	product_id int(10) not null,
	product_color varchar(90),
	product_size varchar(100),
	primary key (product_id),
	foreign key (product_id) references product(product_id));
create table warehouse (
	warehouse_id int(10) not null auto_increment,
	store_id int(6) not null,
	capacity varchar(100) not null,
	primary key (warehouse_id)
	foreign key (store_id) references store(store_id));
create table warehouse_addresses (
	wh_addr_id int(6) not null auto_increment,
	wh_id int(6) not null,
	wh_street varchar(100) not null,
	wh_street2 varchar(100) default null,
	wh_city varchar(100) not null,
	wh_state varchar(100) not null,
	wh_zipcode varchar(15) not null,
	primary key (wh_addr_id),
	foreign key (wh_id) references warehouse(warehouse_id)
	foreign key (wh_state) references store(state_name));
create table inventory (
	product_id int(6) not null,
	warehouse_id int(10) not null,
	stock int(12) not null,
	primary key (product_id),
	foreign key (product_id) references product(product_id),
	foreign key (warehouse_id) references warehouse(warehouse_id));
create table pricing (
	product_id int(6) not null,
	addr_state varchar(100) not null,
	price numeric(6,2) not null,
	primary key (product_id),
	foreign key (product_id) references product(product_id),
	foreign key (addr_state) references customers_delv_addr(delv_state));
create table orders (
	customer_id int(6) not null,
	product_id int(6) not null,
	payment_id int(6) not null,
	quantity int(3) not null,
	time_placed timestamp(null) default current_timestamp,
	status varchar(8) not null,
	primary key (customer_id, time_placed),
	foreign key (customer_id) references customers(customer_id),
	foreign key (product_id) references product(product_id),
	foreign key (payment_id) references customer_payment(payment_id)
	check (status in ('issued', 'received', 'sent')));