year=int(input("enter year: "))

if year<0:
    print("invalid year")
else:
    if year%100==0:
        if year%400==0:
            year_type="Leap Year"
            reason="leap year century divisible by 400"
            
        else:
            year_type="Common Year"
            reason="not a leap year century, not divisile by 4 "

    else:
        if year%4==0:
            year_type="Leap Year"
            reason="not a leap year century, divisible by 4 "

        else:
            year_type="Common Year"
            reason="not a leap year, not divisible by 4"

    if year_type=="Leap Year":
        feb_days=29
        total_days=366

    else:
        feb_days=28
        total_days=365

    print("CALENDER VERIFICATION SYSTEM")
    print(f"Year: {year}")
    print(f"Status: {year_type}")
    print(f"Reason: {reason}")
    print(f"Days in Feb: {feb_days}")
    print(f"Total Days {total_days}")