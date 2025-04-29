import Customer_Table_operation
import Product_Table_operation
import Bill_Table_operation
import QR_code_scanner
from Customer_Table_operation import connect_obj

name=input("Name: ")
phone=input("phone: ")
total_amount=0
data=Customer_Table_operation.existing_customer_retriv(phone)
if data:
    while True:
        choice = input("Do u want yo go on..?\nif no then press 'n' if yes press then press any key\n")
        if choice.lower()=='n':
            break
        else:
            stream_url = "http://192.168.0.101:8080/video"
            details1=QR_code_scanner.scan_qr_once(stream_url)
            details_list=details1.split("-")
            details=Product_Table_operation.product_details(details_list[0])

            # pro_id = input("Product id: ")
            # details = Product_table_operations.product_details(pro_id)
            if details:
                print(details)
                price = details[2]
                stock = details[3]
                quantity = int(input("Amount: "))
                cost = price * quantity
                total_amount = total_amount + cost
                updated_stock = stock - quantity
                Product_Table_operation.product_details_update(updated_stock,details_list[0])
                # Product_table_operations.product_details_update(updated_stock, pro_id)
            else:
                print("Invalid product_id")
    print("Total Amount:",total_amount)
    Bill_Table_operation.bill_details(name,phone,total_amount)
else:
    print("New Customer")
    address=input("Address: ")
    Customer_Table_operation.new_customer_entry(name,phone,address)


connect_obj.close()
