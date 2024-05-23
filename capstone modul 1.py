import datetime

# Definisi data variabel
input_date = []
revenue = []
gross_profit = []
new_project = []
schedule_performance_index = []
cost_performance_index = []
quality_performance_index = []

# Fungsi untuk menampilkan menu utama
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Create KPI Data")
        print("2. Read KPI Data")
        print("3. Update KPI Data")
        print("4. Delete KPI Data")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            create_kpi()
        elif choice == '2':
            read_menu()
        elif choice == '3':
            update_kpi()
        elif choice == '4':
            delete_kpi()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose again.")

# Fungsi untuk fitur create data kpi
def create_kpi():
    print("\nCreate KPI Data")
    rev = float(input("Enter Revenue: "))
    gp = float(input("Enter Gross Profit: "))
    np = int(input("Enter New Project Count: "))
    spi = float(input("Enter Schedule Performance Index: "))
    cpi = float(input("Enter Cost Performance Index: "))
    qpi = float(input("Enter Quality Performance Index: "))

    confirm = input("Do you want to save this data? (yes/no): ").strip().lower()
    if confirm == 'yes':
        today = datetime.datetime.now().strftime("%m%Y")
        input_date.append(today)
        revenue.append(rev)
        gross_profit.append(gp)
        new_project.append(np)
        schedule_performance_index.append(spi)
        cost_performance_index.append(cpi)
        quality_performance_index.append(qpi)
        print("KPI data added successfully!")
    else:
        print("Data creation canceled.")

# Fungsi untuk fitur read data kpi dengan menampilkan opsi read all atau read by date
def read_menu():
    print("\nRead KPI Data")
    print("1. Read All Data")
    print("2. Read Data by Date")
    choice = input("Choose an option (1-2): ")
    
    if choice == '1':
        read_all_data()
    elif choice == '2':
        date_choice = input("Choose an option: 1. Specific Date (mmyyyy) 2. Date Range (mmyyyy-mmyyyy): ")
        if date_choice == '1':
            date = input("Enter Date (mmyyyy): ")
            read_data_by_date(date)
        elif date_choice == '2':
            start_date = input("Enter Start Date (mmyyyy): ")
            end_date = input("Enter End Date (mmyyyy): ")
            read_data_by_date_range(start_date, end_date)
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")

# Fungsi untuk fitur read data kpi berdasarkan opsi read all data
def read_all_data():
    print("\nAll KPI Data:")
    for i in range(len(input_date)):
        print(f"Date: {input_date[i]}, Revenue: {revenue[i]}, Gross Profit: {gross_profit[i]}, New Projects: {new_project[i]}, SPI: {schedule_performance_index[i]}, CPI: {cost_performance_index[i]}, QPI: {quality_performance_index[i]}")

# Fungsi untuk fitur read data kpi berdasarkan opsi read by date secara spesifik
def read_data_by_date(date):
    if date in input_date:
        index = input_date.index(date)
        print(f"\nDate: {input_date[index]}, Revenue: {revenue[index]}, Gross Profit: {gross_profit[index]}, New Projects: {new_project[index]}, SPI: {schedule_performance_index[index]}, CPI: {cost_performance_index[index]}, QPI: {quality_performance_index[index]}")
    else:
        print("Date not found.")

# Fungsi untuk fitur read data kpi berdasarkan opsi read by date secara range
def read_data_by_date_range(start_date, end_date):
    start_index = input_date.index(start_date) if start_date in input_date else -1
    end_index = input_date.index(end_date) if end_date in input_date else -1

    if start_index != -1 and end_index != -1:
        for i in range(start_index, end_index + 1):
            print(f"Date: {input_date[i]}, Revenue: {revenue[i]}, Gross Profit: {gross_profit[i]}, New Projects: {new_project[i]}, SPI: {schedule_performance_index[i]}, CPI: {cost_performance_index[i]}, QPI: {quality_performance_index[i]}")
    else:
        print("Invalid date range.")

# Fungsi untuk fitur update data kpi
def update_kpi():
    print("\nUpdate KPI Data")
    date = input("Enter Date (mmyyyy) to update: ")
    
    if date in input_date:
        index = input_date.index(date)
        rev = float(input("Enter new Revenue: "))
        gp = float(input("Enter new Gross Profit: "))
        np = int(input("Enter new New Project Count: "))
        spi = float(input("Enter new Schedule Performance Index: "))
        cpi = float(input("Enter new Cost Performance Index: "))
        qpi = float(input("Enter new Quality Performance Index: "))

        confirm = input("Do you want to update this data? (yes/no): ").strip().lower()
        if confirm == 'yes':
            revenue[index] = rev
            gross_profit[index] = gp
            new_project[index] = np
            schedule_performance_index[index] = spi
            cost_performance_index[index] = cpi
            quality_performance_index[index] = qpi
            print("KPI data updated successfully!")
        else:
            print("Update canceled.")
    else:
        print("Date not found.")

# Fungsi untuk fitur delete data kpi
def delete_kpi():
    print("\nDelete KPI Data")
    date = input("Enter Date (mmyyyy) to delete: ")
    
    if date in input_date:
        index = input_date.index(date)
        confirm = input("Do you want to delete this data? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del input_date[index]
            del revenue[index]
            del gross_profit[index]
            del new_project[index]
            del schedule_performance_index[index]
            del cost_performance_index[index]
            del quality_performance_index[index]
            print("KPI data deleted successfully!")
        else:
            print("Deletion canceled.")
    else:
        print("Date not found.")

if __name__ == "__main__":
    main_menu()
