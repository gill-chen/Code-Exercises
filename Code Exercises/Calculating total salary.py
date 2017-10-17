def computepay(h,r):
    h = float(h)
    r = float(r)
    if h > 40:
        overtime = h -40
        overpay = overtime * 1.5 * r
        grosspay = overpay + (40 * r)
    else
        grosspay = h * r 
    return grosspay

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter rate:")
p = computepay(hrs,rate)
print "Pay",p
    
