#Author: Shrutirupa Banerjiee
#crackme link: https://crackmes.one/crackme/6804f9718f555589f3530d92

def validate_license_number(number: int) -> bool:
    condition1 = (number % 59) == 12
    condition2 = (number % 113) == 12
    condition3 = (number & 0xff) == 0x55
    return condition1 and condition2 and condition3

def find_valid_license_keys():
    valid_keys = []
    for num in range(0, 100_000_000):  # 8-digit numbers
        if validate_license_number(num):
            key = f"CTF-{num:08d}"  # Format with leading zeros
            valid_keys.append(key)
    return valid_keys

if __name__ == "__main__":
    keys = find_valid_license_keys()

    print("Valid License Keys Found:\n")
    for k in keys:
        print(k)

    print(f"\nTotal valid keys found: {len(keys)}")
