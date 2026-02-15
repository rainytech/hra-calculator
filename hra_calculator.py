"""
🌿 HRA EXEMPTION CALCULATOR 🌿
For Indian Income Tax - Section 10(13A)

Created by: Goodwill Tuition Centre, Ernakulam
Purpose: Calculate HRA exemption for salaried employees

"Knowledge shared is knowledge multiplied!" - Goodwill Centre
"""

# ============================================
# FUNCTION TO CALCULATE HRA EXEMPTION
# ============================================

def calculate_hra_exemption():
    """
    This function calculates HRA exemption based on Income Tax Act Section 10(13A)
    
    The exemption is the MINIMUM of these three:
    1. Actual HRA received from employer
    2. Rent paid minus 10% of salary
    3. 50% of salary (metro cities) OR 40% of salary (non-metro)
    """
    
    print("=" * 60)
    print("         🏠 HRA EXEMPTION CALCULATOR 🏠")
    print("      Section 10(13A) - Income Tax Act, 1961")
    print("=" * 60)
    print()
    
    # ============================================
    # STEP 1: GET INPUT FROM USER
    # ============================================
    
    try:
        # Get Basic Salary
        print("📊 Enter the following details:")
        print("-" * 60)
        basic_salary = float(input("1. Basic Salary (₹ per annum): "))
        
        # Get Dearness Allowance (if any)
        # IMPORTANT: DA is included ONLY if it enters retirement benefits
        da_choice = input("2. Do you receive Dearness Allowance (DA) that enters retirement benefits? (Y/N): ").upper()
        if da_choice == 'Y':
            da = float(input("   Enter DA amount (₹ per annum): "))
        else:
            da = 0
        
        # Get Commission on turnover (if any)
        commission_choice = input("3. Do you receive Commission on turnover basis? (Y/N): ").upper()
        if commission_choice == 'Y':
            commission = float(input("   Enter Commission amount (₹ per annum): "))
        else:
            commission = 0
        
        # Calculate total salary for HRA calculation
        # Salary = Basic + DA (if enters retirement) + Commission (on turnover)
        total_salary = basic_salary + da + commission
        
        # Get HRA received
        hra_received = float(input("4. HRA Received (₹ per annum): "))
        
        # Get Rent Paid
        rent_paid = float(input("5. Rent Paid (₹ per annum): "))
        
        # Get City Type
        print("\n6. City Type:")
        print("   M - Metro City (Mumbai, Delhi, Kolkata, Chennai)")
        print("   N - Non-Metro City")
        city_type = input("   Enter your choice (M/N): ").upper()
        
        # ============================================
        # STEP 2: VALIDATE INPUTS
        # ============================================
        
        # Check for negative values
        if basic_salary < 0 or da < 0 or commission < 0 or hra_received < 0 or rent_paid < 0:
            print("\n❌ Error: Amounts cannot be negative!")
            return
        
        # Check if city type is valid
        if city_type not in ['M', 'N']:
            print("\n❌ Error: Please enter M for Metro or N for Non-Metro!")
            return
        
        # ============================================
        # SPECIAL CASE: NO RENT PAID
        # ============================================
        
        # If person receives HRA but pays NO rent, entire HRA is taxable
        if rent_paid == 0:
            print("\n" + "=" * 60)
            print("⚠️  IMPORTANT NOTICE")
            print("=" * 60)
            print("\nYou have not paid any rent.")
            print("As per Income Tax rules:")
            print("If NO rent is paid, entire HRA is FULLY TAXABLE!")
            print("\n" + "=" * 60)
            print("🎯 FINAL RESULTS")
            print("=" * 60)
            print(f"\n💰 Total HRA Received        : ₹{hra_received:,.2f}")
            print(f"✅ HRA Exemption (Tax Free) : ₹0.00")
            print(f"📊 Taxable HRA              : ₹{hra_received:,.2f}")
            print("\n" + "=" * 60)
            print("✨ Calculation completed!")
            print("=" * 60)
            return
        
        # ============================================
        # STEP 3: CALCULATE THREE CONDITIONS
        # ============================================
        
        print("\n" + "=" * 60)
        print("📈 CALCULATING HRA EXEMPTION...")
        print("=" * 60)
        
        # Condition 1: Actual HRA received
        condition1 = hra_received
        print(f"\n✓ Condition 1: Actual HRA Received = ₹{condition1:,.2f}")
        
        # Condition 2: Rent paid minus 10% of salary
        ten_percent_salary = total_salary * 0.10
        condition2 = rent_paid - ten_percent_salary
        # If rent is less than 10% of salary, exemption is 0
        if condition2 < 0:
            condition2 = 0
        print(f"✓ Condition 2: Rent Paid - 10% of Salary")
        print(f"               = ₹{rent_paid:,.2f} - ₹{ten_percent_salary:,.2f}")
        print(f"               = ₹{condition2:,.2f}")
        
        # Condition 3: 50% of salary (metro) or 40% (non-metro)
        if city_type == 'M':
            percentage = 50
            condition3 = total_salary * 0.50
        else:
            percentage = 40
            condition3 = total_salary * 0.40
        
        print(f"✓ Condition 3: {percentage}% of Salary (Basic + DA* + Commission*)")
        print(f"               *Only if DA enters retirement & Commission on turnover")
        print(f"               = {percentage}% of ₹{total_salary:,.2f}")
        print(f"               = ₹{condition3:,.2f}")
        
        # ============================================
        # STEP 4: FIND MINIMUM (EXEMPTION AMOUNT)
        # ============================================
        
        # The exemption is the MINIMUM of all three conditions
        hra_exemption = min(condition1, condition2, condition3)
        
        # Calculate taxable HRA
        taxable_hra = hra_received - hra_exemption
        
        # ============================================
        # STEP 5: DISPLAY RESULTS
        # ============================================
        
        print("\n" + "=" * 60)
        print("🎯 FINAL RESULTS")
        print("=" * 60)
        print(f"\n💰 Total HRA Received        : ₹{hra_received:,.2f}")
        print(f"✅ HRA Exemption (Tax Free) : ₹{hra_exemption:,.2f}")
        print(f"📊 Taxable HRA              : ₹{taxable_hra:,.2f}")
        print("\n" + "=" * 60)
        print("✨ Calculation completed successfully!")
        print("=" * 60)
        
        # Show which condition gave minimum
        if hra_exemption == condition1:
            print("\n📌 Exemption based on: Actual HRA Received")
        elif hra_exemption == condition2:
            print("\n📌 Exemption based on: Rent Paid - 10% of Salary")
        else:
            print(f"\n📌 Exemption based on: {percentage}% of Salary")
        
    except ValueError:
        # This handles if user enters text instead of numbers
        print("\n❌ Error: Please enter valid numbers only!")
        return
    except Exception as e:
        # This handles any other unexpected errors
        print(f"\n❌ An error occurred: {e}")
        return


# ============================================
# MAIN PROGRAM STARTS HERE
# ============================================

if __name__ == "__main__":
    """
    This is where the program starts running
    """
    
    # Run the calculator
    calculate_hra_exemption()
    
    # Ask if user wants to calculate again
    print("\n" + "=" * 60)
    calculate_again = input("\n🔄 Calculate for another employee? (Y/N): ").upper()
    
    while calculate_again == 'Y':
        print("\n")
        calculate_hra_exemption()
        calculate_again = input("\n🔄 Calculate for another employee? (Y/N): ").upper()
    
    # Closing message
    print("\n" + "=" * 60)
    print("      Thank you for using HRA Calculator! 🙏")
    print("       Goodwill Tuition Centre, Ernakulam")
    print("              Saving Time 🌍 Saving Planet")
    print("=" * 60)
    print('\n"Education is the most powerful weapon" - Nelson Mandela 🌿\n')


"""
========================================
HOW TO USE THIS PROGRAM:
========================================

1. Save this file as: hra_calculator.py
2. Open Command Prompt or Terminal
3. Navigate to the folder where you saved this file
4. Type: python hra_calculator.py
5. Press Enter
6. Follow the instructions on screen!

========================================
NOTES FOR TEACHERS:
========================================

- This calculator follows Income Tax Act Section 10(13A)
- Metro cities: Mumbai, Delhi, Kolkata, Chennai
- Formula is: Minimum of (Actual HRA, Rent-10% Salary, 50%/40% Salary)
- "Salary" includes: Basic + DA (only if enters retirement) + Commission (on turnover)
- IMPORTANT: If no rent paid, entire HRA is fully taxable!
- Students often forget the "minimum" rule - teach this carefully!
- You can modify this code to add more features

🌿 Keep learning, keep growing! 🌿
"""
