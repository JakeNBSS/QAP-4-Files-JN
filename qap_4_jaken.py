# imports

import datetime as dt
import FormatValues as fv
currdate = dt.datetime.now()
currdatef = currdate.strftime("%Y-%m-%d")

# constants & lists

f = open("const.dat", "r")
nextpolicynum = int(f.readline()) # 1944
basicpremium = float(f.readline()) # 869.00
additionaldardiscountrate = float(f.readline()) # .25
extraliabilityrate = float(f.readline()) # 130.00
glasscoveragerate = float(f.readline()) # 86.00
loanercarrate = float(f.readline()) # 58.00 
hstrate = float(f.readline()) # .15
monthlyprocessingfee = float(f.readline()) # 39.99
f.close()


provlist = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YK"]
paylist = ["Full", "Monthly", "Down Payment"]
previousclaim1 = [1941, dt.datetime(2020, 1, 14), 1500.00]
previousclaim2 = [1942, dt.datetime(2022, 7, 3), 1200.00]
previousclaim3 = [1943, dt.datetime(2023, 3, 30), 2000.00]

while True:
# input
    print()

    while True:
        custfirstname = input("Enter first name here: ").title() # first letter is capitalized
        if custfirstname == "":
            print("ERROR - first name cannot be blank.")
        else: 
            break
    
    while True:
        custlastname = input("Enter last name here: ").title()
        if custlastname == "":
            print("ERROR - last name cannot be blank.")
        else:
            break

    while True:
        custaddress = input("Enter address here: ")
        if custaddress == "":
            print("ERROR - address cannot be blank.")
        else:
            break
        
    while True:
        custcity = input("Enter city here: ")
        if custcity == "":
            print("ERROR - city cannot be blank")
        else:
            break
    
    while True:
        custprovince = input("Enter province here (ON, NL, AB): ").upper() # all caps
        if custprovince not in provlist:
            print("ERROR - invalid province.")
        else:
            break

    while True:
        custpostalcode = input("Enter postal code here (A1A1A1): ").upper()
        if custpostalcode == "":
            print("ERROR - postal code cannot be blank.")
        elif len(custpostalcode) != 6:
            print("ERROR - postal code must be 6 digits")
        else:
            break


    while True:
        custphone = input("Enter phone number here (1234567890): ")
        if custphone == "":
            print("ERROR - phone number cannot be blank.")
        elif len(custphone) != 10:
            print("ERROR - phone number must be 10 digits.")
        else:
            break
    
    while True:
        try:
            numcars = int(input("Enter number of cars being insured: "))
        except:
            print("ERROR - input must be an integer.")
        else:
            break
    
    while True:
        extraliability = input("Would you like extra liability up to $1,000,000? (Y/N): ").upper()
        if extraliability not in ["Y", "N"]:
            print("ERROR - input must be 'Y' or 'N'.")
        else:
            break
    
    while True:
        glasscoverage = input("Would you like glass coverage? (Y/N): ").upper()
        if glasscoverage not in ["Y", "N"]:
            print("ERROR - input must be 'Y' or 'N'.")
        else:
            break

    while True:
        loanercar = input("Would you like aloaner car? (Y/N): ").upper()
        if loanercar not in ["Y", "N"]:
            print("ERROR - input must be 'Y' or 'N'.")
        else:
            break

    while True:
        payoption = input("Would you like to pay in Full, Monthly or make a Down Payment?: ").title()
        if payoption not in paylist:
            print("ERROR - input must be 'Full', 'Monthly' or 'Down Payment'.")
        elif payoption == "Down Payment":
            try:
                downpayment = float(input("Enter the Down Payment amount: $"))
            except ValueError: 
                print("ERROR = input must be a number.")
        else:
            break

    # add smth back here when u have the answer

    # calculations
    
    if numcars > 1:
        insurancepremium = basicpremium + ((basicpremium * additionaldardiscountrate) * (numcars - 1))
    else:
        insurancepremium = basicpremium
    
    if extraliability == "Y":
        extraliabilitycost = extraliabilityrate * numcars
    else: 
        extraliabilitycost = 0

    if glasscoverage == "Y":
        glasscoveragecost = glasscoveragerate * numcars
    else:
        glasscoveragecost = 0

    if loanercar == "Y":
        loanercarcost = loanercarrate * numcars
    else:
        loanercarcost = 0

    totalextracosts = extraliabilitycost + glasscoveragecost + loanercarcost

    totalinsurancepremium = insurancepremium + totalextracosts

    hst = totalinsurancepremium * hstrate

    totalcost = totalinsurancepremium + hst

    if payoption == "Monthly":
        monthlypay = (totalcost + monthlyprocessingfee) / 8
    elif payoption == "Down Payment":
        monthlypay = (totalcost + monthlyprocessingfee - downpayment)
    else:
        monthlypay = 0

    invoicedate = currdate

    if invoicedate.month == 12:
        nextmonth = 1
        nextyear = invoicedate.year + 1
    else:
        nextmonth = invoicedate.month + 1
        nextyear = invoicedate.year
    
    nextpaydate = dt.datetime(nextyear, nextmonth, 1)


    # display

    print()
    print("            ONE STOP INSURANCE COMPANY")
    print("      --------------------------------------")
    print()
    print(f"                Policy #: {nextpolicynum}")
    print(f"                Date: {currdatef}")
    print(f"                {custfirstname} {custlastname}")
    print(f"                {custaddress}, {custcity}, {custprovince}")
    print(f"                {custpostalcode}, {custphone}")
    print()
    print("     ---------------------------------------")
    print()
    print(f"                # of cars insured: {numcars}")
    print(f"                Extra Liability: {extraliability}")
    print(f"                Glass Coverage: {glasscoverage}")
    print(f"                Loaner Car: {loanercar}")
    print(f"                Payment Option: {payoption}")
    print()
    print("     ---------------------------------------")
    print()
    print(f"                Insurance Premium Cost: {fv.FDollar2(insurancepremium)}")
    if extraliability == "Y":
        print(f"                 Extra Liability Cost: {fv.FDollar2(extraliabilitycost)}")
    if glasscoverage == "Y":
        print(f"                 Glass Coverage Cost: {fv.FDollar2(glasscoveragecost)}")
    if loanercarcost == "Y":
        print(f"                 Loaner Car Cost: {fv.FDollar2(loanercarcost)}")
    print(f"                Extra Total Cost: {fv.FDollar2(totalextracosts)}")
    print(f"                Total Insurance Premium: {fv.FDollar2(totalinsurancepremium)}")
    print(f"                HST: {fv.FDollar2(hst)}")
    print(f"                Total Cost: {fv.FDollar2(totalcost)}")
    if payoption == "Monthly":
        print(f"                 Monthly Pay: {fv.FDollar2(monthlypay)}")
        print(f"                 Next Payment Date: {nextpaydate.strftime('%Y-%m-%d')}")
    if payoption == "Down Payment":
        print(f"                 Down Payment: {fv.FDollar2(downpayment)}")
    print()
    print("     ---------------------------------------")
    print()
    



    # previous claims

    print("          PREVIOUS CLAIMS")
    print()
    print("Claim #   Claim Date         Amount")
    print("     -----------------------------------")
    print(f" {previousclaim1[0]}    {previousclaim1[1].strftime('%Y-%m-%d')}    ${fv.FComma2(previousclaim1[2]):>9}")
    print(f" {previousclaim2[0]}    {previousclaim2[1].strftime('%Y-%m-%d')}    ${fv.FComma2(previousclaim2[2]):>9}")
    print(f" {previousclaim3[0]}    {previousclaim3[1].strftime('%Y-%m-%d')}    ${fv.FComma2(previousclaim3[2]):>9}")

    Continue = input("Would you like to enter another policy (Y/N): ").upper()
    if Continue == "N":
        print("Thank you for using the One Stop Insurance Company Program!")
        break

    print()