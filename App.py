#Carol Marin
#CS 425 Final Project

import os
import sys
import psycopg2

try:
	connection = psycopg2.connect(user = "postgres", password = "Cps.50202115", host = "localhost", port = "5432", database = "Final")
	cursor = connection.cursor()
	print(connection.get_dsn_parameters(),"\n")
	cursor.execute("SELECT version();")
	record = cursor.fetchone()
	print("You are connected to PostgreSQL")
except (Exception, psycopg2.Error) as error:
	print ("Error while connecting to PostgreSQL", error)
finally:
	if connection:
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")


class Customer:
	cid = ""
	delvID = ""
	billID = ""

class Staff:
	sid = ""

def initialize():
	done = False
	print('Enter "1" to enter as customer, "2" to enter as staff, "3" to exit. ')
	while not done:
		inp = input()
		if inp == "1":
			done = True
			ret = clogin()
			return ret
		elif inp == "2":
			done = True
			ret = slogin()
			return ret
		elif inp == "3":
			return 0
		else:
			print("Error: invalid input")

def clogin():
	cust = True
	while cust:
		fname = input("Enter your first name: ")
		lname = input("Enter your last name: ")
		bal = input("Current balance: ")
		query = "INSERT INTO customers VALUES (NULL, '{}', '{}', NULL);".format(1, fname, lname, bal)
		cursor.execute(query)
		data = cursor.fetchall()
		Customer.cid = data[0][0]

def slogin():
	staff = True;
	while staff:
		fname = input("Enter your first name: ")
		lname = input("Enter your last name: ")
		salary = input("Enter your salary: ")
		job = input("Enter your job title: ")
		query = "INSERT INTO staff VALUES (NULL, '{}', '{}', NULL, '{}');".format(1, fname, lname, salary, job)
		cursor.execute(query)
		data = cursor.fetchall()
		Staff.sid = data[0][0]

def mainmenu():
	print("Choose an action: ")
	print('\n "1" = Edit Personal Information\n "2" = Place an Order\n "3" = Modify Store Data\n "4" = Modify Warehouse Stock')
	choice1 = input()
	if choice1 == "1":
		print("Choose information to change: (1) Payment Infromation or (2) Addresses")
		custChoice = input()
		if custChoice == "1":
			print("Choose an option: (1) Add Credit Card, (2) Change Credit Card, or (3) Delete Credit Card")
			payChoice = input()
			if payChoice == "1":
				AddPayment()
			elif payChoice == "2":
				ModPayment()
			elif payChoice == "3":
				DelPayment()
			else:
				print("Error: invalid input")
				pass
		elif custChoice == "2":
			print("Choose information to change: (1) Delivery Address or (2) Billing Address")
			addrChoice = input()
			if addrChoice == "1":
				print("Choose an option: (1) Add Address, (2) Change Address, or (3) Delete Address")
				delivChoice = input()
				if delivChoice == "1":
					AddDelivAddress()
				elif delivChoice == "2":
					ModDelivAddress()
				elif delivChoice == "3":
					DelDelivAddress()
				else:
					print("Error: invalid input")
					pass
			elif addrChoice == "2":
				print("Choose an option: (1) Add Address, (2) Change Address, or (3) Delete Address")
				billChoice = input()
				if billChoice == "1":
					AddBillAddress()
				elif billChoice == "2":
					ModBillAddress()
				elif billChoice == "3":
					DelBillAddress()
				else:
					print("Error: invalid input")
					pass
			else:
				print("Error: invalid input")
				pass
		else:
			print("Error: invalid input")
			pass
	elif choice1 == "2":
		buyProduct()
	elif choice1 == "3":
		modStore()
	elif choice1 == "4":
		modWarehouse()
	else:
		print("Error: invalid input")
		sysexit()

def AddPayment():
	print("Enter your credit card information: ")
	creditCardNum = input("Enter your credit card number: ")
	expDate = input("Enter the expiration date: ")
	securityCode = input("Enter the security code: ")
	query = "INSERT INTO VALUES ".format(1, Customer.cid, Customer.billID, creditCardNum, expDate, securityCode)
	cursor.execute(query)

def ModPayment():
	query = "SELECT * FROM customer_payment where customer_id = '{}'".format(Customer.cid)
	cursor.execute(query)
	data = cursor.fetchall()
	print("Choose the payment_id of the credit card you want to modify: ")
	id = input()
	query = "DELETE FROM customer_payment WHERE payment_id = {}".format(id)
	cursor.execute(query)
	print("Add new information: ")
	creditCardNum = input("Enter your credit card number: ")
	expDate = input("Enter the expiration date: ")
	securityCode = input("Enter the security code: ")
	query = "INSERT INTO VALUES ".format(id, Customer.cid, Customer.billID, creditCardNum, expDate, securityCode)
	cursor.execute(query)
	
def DelPayment():
	query = "SELECT * FROM customer_payment where customer_id = '{}'".format(Customer.cid)
	cursor.execute(query)
	data = cursor.fetchall()
	print("Choose the payment_id of the credit card you want to modify: ")
	id = input()
	query = "DELETE FROM customer_payment WHERE payment_id = {}".format(id)
	cursor.execute(query)

def AddDelivAddress():
	print("Enter your delivery address")
	street = input("Enter your street address: ")
	street2 = input("Enter your street (field 2): ")
	city = input("Enter your city: ")
	state = input("Enter your state: ")
	zip = input("Enter your zipcode: ") 
	query = "INSERT INTO customers_del_address VALUES (NULL, {}, '{}', '{}', '{}', '{}', '{}')".format(1, 1, street, street2, city, state, zip)
	cursor.execute(query)
	data = cursor.fetchall()
	Customer.delvID = data[0][0]

def ModDelivAddress():
	query = "SELECT * FROM customers_del_address WHERE customer_id = '{}'".format(Customer.cid)
	cursor.execute(query)
	data = cursor.fetchall()
	print("Choose the delv_addr_id of the address you want to modify: ")
	id = input()
	query = "DELETE FROM customers_delv_address WHERE delv_addr_id = {}".format(id)
	cursor.execute(query)
	print("Add the new information: ")
	street = input("Enter your street address: ")
	street2 = input("Enter your street (field 2): ")
	city = input("Enter your city: ")
	state = input("Enter your state: ")
	zip = input("Enter your zipcode: ")
	query = "INSERT INTO customers_del_address VALUES (NULL, {}, '{}', '{}', '{}', '{}', '{}')".format(1, id, street, street2, city, state, zip)
	cursor.execute(query)
	data = cursor.fetchall()
	Customer.delvID = data[0][0]

def DelDelivAddress():
	query = "SELECT * FROM customers_del_address WHERE customer_id = '{}'".format(Customer.cid)
	cursor.execute(query)
	data = cursor.fetchall()
	print("Choose the delv_addr_id of the address you want to remove: ")
	id = input()
	query = "DELETE FROM customers_delv_address WHERE delv_addr_id = {}".format(id)
	cursor.execute(query)

def AddBillAddress():
	print("Enter your billing address")
	street = input("Enter your street address: ")
	street2 = input("Enter your street (field 2): ")
	city = input("Enter your city: ")
	state = input("Enter your state: ")
	zip = input("Enter your zipcode: ") 
	query = "INSERT INTO customers_bill_address VALUES (NULL, {}, '{}', '{}', '{}', '{}', '{}')".format(1, 1, street, street2, city, state, zip)
	cursor.execute(query)
	data = cursor.fetchall()
	Customer.billID = data[0][0]

def ModBillAddress():
	query = "SELECT * FROM customers_bill_address WHERE customer_id = '{}'".format(Customer.cid)
	cursor.execute(query)
	data = cursor.fetchall()
	print("Choose the bill_addr_id of the address you want to modify: ")
	id = input()
	query = "DELETE FROM customers_bill_address WHERE bill_addr_id = {}".format(id)
	cursor.execute(query)
	print("Add the new information: ")
	street = input("Enter your street address: ")
	street2 = input("Enter your street (field 2): ")
	city = input("Enter your city: ")
	state = input("Enter your state: ")
	zip = input("Enter your zipcode: ") 
	query = "INSERT INTO customers_bill_address VALUES (NULL, {}, '{}', '{}', '{}', '{}', '{}')".format(1, 1, street, street2, city, state, zip)
	cursor.execute(query)
	data = cursor.fetchall()
	Customer.billID = data[0][0]

def DelBillAddress():
	query = "SELECT * FROM customers_bill_address WHERE customer_id = '{}'".format(Customer.cid)
	cursor.execute(query)
	data = cursor.fetchall()
	print("Choose the bill_addr_id of the address you want to remove: ")
	id = input()
	query = "DELETE FROM customers_bill_address WHERE bill_addr_id = {}".format(id)
	cursor.execute(query)

def buyProduct():
	ord = False
	while not ord:
		query = "SELECT * FROM product;"
		cursor.execute(query)
		print("Choose each item you want, individually, by entering the product_id: ")
		id = input()
		query = "SELECT * FROM customer_payment where customer_id = {};".format(Customer.cid)
		cursor.execute(query)
		print("Choose a payment_id for your payment method: ")
		pid = input()
		print("Enter the following: ")
		quantity = input("Enter the amount you want of this product: ")
		query = "INSERT INTO VALUES (NULL, {}, {}, {}, '{}', '{}');".format(Customer.cid, id, pid, quantity, "null", 'issued')
		cursor.execute(query)

def modStore():
	query = "SELECT * FROM staff;"
	cursor.execute(query)
	if Staff.sid in query:
		staffChoice = input("Choose something to modify: (1) Products or (2) Product Pricing ")
		if staffChoice == "1":
			prodChoice = input("Choose one: (1) Add a Product, (2) Modify a Product, or (3) Delete a Product ")
			if prodChoice == "1":
				AddProduct()
			elif prodChoice == "2":
				ModProduct()
			elif prodChoice == "3":
				DelProduct()
			else:
				print("Error: invalid input")
				pass
		elif staffChoice == "2":
			priceChocie = input("Choose one: (1) Add a Price, (2) Modify a Price, or (3) Delete a Price ")
			if priceChoice == "1":
				AddPrice()
			elif priceChoice == "2":
				ModPrice()
			elif priceChoice == "3":
				DelPrice()
			else:
				print("Error: invalid input")
				pass
		else:
			print("Error: invalid input")
			pass
	else:
		print("Authorization denied")
		pass

def AddProduct():
	print("Enter the product information ")
	name = input("Enter the product name: ")
	type = input("Enter the product type (Dairy, Meat, Fruit, Vegetables, Grain, Drinks, Alcohol): ")
	information = input("Enter any dietary information: ")
	query = "INSERT INTO product VALUES (NULL, '{}', '{}', '{}')".format(1, name, type, information)
	cursor.execute(query)

def ModProduct():
	query = "SELECT * FROM product"
	cursor.execute(query)
	data = cursor.fetchall()
	print("Choose the product_id of the product you want to modify: ")
	id = input()
	query = "DELETE FROM product WHERE product_id = {}".format(id)
	cursor.execute(query)
	print("Add the new information: ")
	name = input("Enter the product name: ")
	type = input("Enter the product type (Dairy, Meat, Fruit, Vegetables, Grain, Drinks, Alcohol): ")
	information = input("Enter any dietary information: ")
	query = "INSERT INTO product VALUES (NULL, '{}', '{}', '{}')".format(id, name, type, information)
	cursor.execute(query)

def DelProduct():
	query = "SELECT * FROM product"
	cursor.execute(query)
	data = cursor.fetchall()
	print("Choose the product_id of the product you want to remove: ")
	id = input()
	query = "DELETE FROM product WHERE product_id = {}".format(id)
	cursor.execute(query)

def AddPrice():
	query = "SELECT * FROM product;"
	cursor.execute(query)
	data = cursor.fetchall()
	print("Enter the product_id of the product you want to add a price for: ")
	id = input()
	print("Enter the pricing information ")
	state = input("Enter the state where your store is located: ")
	price = input("Enter the price: ")
	query = "INSERT INTO pricing VALUES ({}, '{}', {});".format(id, state, price)
	cursor.execute(query)

def ModPrice():
	query = "SELECT * FROM product;"
	cursor.execute(query)
	data = cursor.fetchall()
	print("Enter the product_id of the product you want to change the price for: ")
	id = input()
	query = "DELETE FROM pricing WHERE product_id = {};".format(id)
	cursor.execute(query)
	print("Add the new information: ")
	state = input("Enter the state where your store is located: ")
	price = input("Enter the price: ")
	query = "INSERT INTO pricing VALUES ({}, '{}', {});".format(id, state, price)
	cursor.execute(query)

def DelPrice():
	query = "SELECT * FROM product;"
	cursor.execute(query)
	data = cursor.fetchall()
	print("Enter the product_id of the product you want to change the price for: ")
	id = input()
	query = "DELETE FROM pricing WHERE product_id = {};".format(id)
	cursor.execute(query)

def modWarehouse():
	query = "SELECT * FROM staff;"
	cursor.execute(query)
	if Staff.sid in query:
		query = "SELECT * FROM product;"
		cursor.execute(query)
		query = "SELECT * FROM warehouse;"
		cursor.execute(query)
		print("Enter the product_id of the product you want to add stock information to: ")
		id = input()
		print("Enter the warehouse_id of your store's warehouse: ")
		wid = input()
		print("Enter the inventory information: ")
		stock = input("Enter the amount of the product: ")
		query = "INSERT INTO inventory VALUES ({}, {}, {});".format(id, wid, stock)
	else:
		print("Authorization denied")
		pass
