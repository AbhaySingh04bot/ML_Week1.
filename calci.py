

total = 0
while True :
    try:
        n = int(input("How many items? "))
        break
    except ValueError:
        print("please enter a valid price of item")

for i in range(n):
    
    while True:
        try:
            price = float(input("Enter price of item ₹: "))
            break
        except ValueError:
            print("please enter a valid price of item")



    quantity = int(input("Enter quantity: "))
    total += price * quantity

gst = total * 0.18
final_total = total + gst

print("\n------ BILL ------")
print("Total without GST: ₹", round(total, 2))
print("GST (18%): ₹", round(gst, 2))
print("Final Total: ₹", round(final_total, 2))

