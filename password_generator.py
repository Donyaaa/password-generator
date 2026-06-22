# Password Generator
import string
import secrets
def str_check(message):
    while True:
        answer = input(message).lower()
        if answer == "y" or answer == "n":
            return answer
        else:
            print("Invalid input! Please enter 'y' or 'n'.")
def check_number(message, error_message):
    while True:
        try:
            num1 = int(input(message))
            if 1 <= num1 <= 100:
                return num1
            print(error_message)
        except ValueError:
            print("Please enter a valid integer!")
def menu_check(message):
    while True:
        try:
            answer = int(input(message))
            if answer == 1 or answer == 2:
                return answer
            print("Invalid input! Please enter '1' or '2'.")
        except ValueError:
            print("Please enter a valid integer!")
def password_strength(password):

         strength=0
         reason=[]

         if len(password)>= 8:
             strength+=1
         else:
             reason.append("Password is too short")
         if any(c in string.punctuation for c in password):
             strength += 1
         else:
             reason.append("No symbols")
         if any(c.isupper() for c in password):
             strength += 1
         else:
             reason.append("No Uppercase letters")

         if any(c in string.ascii_lowercase for c in password):
             strength += 1
         else:
             reason.append("No Lowercase letters")
         if any(c in string.digits for c in password):
             strength += 1
         else:
             reason.append("No Numbers")
         if strength == 0 or strength == 1:
             level= "very weak"
         elif strength == 2 or strength == 3:
             level= "weak"
         elif strength == 4:
             level= "medium"
         else:
             level= "strong"

         return level,reason

while True:
    # ===== MAIN MENU =====
    print("\n===== PASSWORD GENERATOR MENU =====")
    print("1. Generate passwords")
    print("2. Exit")

    choice = menu_check("Choose an option: (1/2) ")

    # خروج از برنامه
    if choice == 2:
        print("Thank you for using Password Generator!")
        break
    # ===== PASSWORD SETTINGS =====

    while True:

        # دریافت طول پسورد
        char_leng = check_number(
                "Enter password length:",
                "Password length must be between 1 and 100 characters!")

        characters = ""  # تمام کاراکترهای مجاز
        force_char = []  # حداقل یک کاراکتر از هر نوع انتخاب شده
        selected_option = []  # لیست گزینه‌های انتخاب شده
        # دریافت تنظیمات کاربر
        p_upper = str_check("Include uppercase letters? (y/n)")
        p_lower = str_check("Include lowercase letters? (y/n)")
        p_number = str_check("Include numbers? (y/n)")
        p_symbol = str_check("Include symbols? (y/n)")

        # حروف بزرگ
        if p_upper == "y":
            characters += string.ascii_uppercase
            selected_option.append("Uppercase")
            force_char.append(secrets.choice(string.ascii_uppercase))

        # حروف کوچک
        if p_lower == "y":
            characters += string.ascii_lowercase
            selected_option.append("Lowercase")
            force_char.append(secrets.choice(string.ascii_lowercase))

        # اعداد
        if p_number == "y":
            characters += string.digits
            selected_option.append("Numbers")
            force_char.append(secrets.choice(string.digits))

        # سمبل‌ها
        if p_symbol == "y":
            characters += string.punctuation
            selected_option.append("Symbols")
            force_char.append(secrets.choice(string.punctuation))

        # اگر هیچ گزینه‌ای انتخاب نشده باشد
        if characters == "":
            print("Error: At least one character type must be selected!")
            continue

        # نمایش گزینه‌های انتخاب شده
        print("\nSelected:")
        for item in selected_option:
            print(f"✓ {item}")

        # اگر طول پسورد کمتر از تعداد انواع کاراکتر باشد
        if char_leng < len(force_char):
            print("Password length too small for selected options!")
            continue
        # همه چیز درست است
        break
        # ===== PASSWORD COUNT =====

    pass_count = check_number(
            "How many passwords do you want to generate? ",
            "Max 100 and Min 1 password allowed!")

    pass_dic = {}
    # نمایش یا مخفی کردن پسوردها
    show_hide = str_check("Show passwords? (y/n):")
    # ===== GENERATE PASSWORDS =====

    for c in range(pass_count):

         while True:
             p_name = input(f"Enter a name for password {c + 1}:")

             if p_name in pass_dic or p_name == "":
                 print("Name is empty or already exists!")
                 continue

             password = []

             # اضافه کردن کاراکترهای اجباری
             password.extend(force_char)

             # تکمیل بقیه پسورد

             leng = char_leng - len(force_char)
             for i in range(leng):
                password.append(secrets.choice(characters))

             # مخلوط کردن ترتیب کاراکترها
             secrets.SystemRandom().shuffle(password)

             # تبدیل لیست به رشته
             password = "".join(password)

             # بررسی قدرت پسورد
             level, reasons = password_strength(password)

             # نمایش پسورد
             if show_hide == "y":
                print(f"\n✓ Password Generated Successfully")
                print(f"Account: {p_name}")
                print(f"Password: {password}")
             print(f"Strength: {level}")

             for item in reasons:
                print(f"[- {item}]")
             # ذخیره در دیکشنری
             pass_dic[p_name] = password
             break

         # ===== SAVE PASSWORDS =====
    pass_save=str_check("Would you like to save all passwords? (y/n)")
    if pass_save == "y":
        with open("passwords.txt", "w", encoding="utf-8", errors="ignore") as pass_file:
            pass_file.write("========== GENERATED PASSWORDS ==========\n")
            for c, d in pass_dic.items():
                pass_file.write(f"{c}: {d}\n")
        print("Password saved!")
    else:
        print("Passwords not saved.!")






