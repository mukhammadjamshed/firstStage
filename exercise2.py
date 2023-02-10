def check_substring(main_string, substring, case_sensitive=True):
    if not case_sensitive:
        main_string = main_string.lower()
        substring = substring.lower()
    return substring in main_string

def get_user_input():
    main_string = input("Enter the string: ")
    substring = input("Input the substring to search: ")
    case_sensitive = input("Do you want a case-sensitive search? (yes/no) ").strip().lower() == "yes"
    return main_string, substring, case_sensitive

def main():
    try:
        main_string, substring, case_sensitive = get_user_input()
    except Exception as e:
        print("An error occurred:", e)
        return

    if check_substring(main_string, substring, case_sensitive):
        print("The substring exists in the string")
    else:
        print("The substring does not exist in the string")

if __name__ == "__main__":
    main()
