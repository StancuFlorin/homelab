import sys

def replace_and_comment(file_path, old_domain, new_domain):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Replace the old domain with the new domain
        for i, line in enumerate(lines):
            if old_domain in line:
                lines[i] = line.replace(old_domain, new_domain)

        # Comment out lines containing ssl_trusted_certificate
        for i, line in enumerate(lines):
            if 'ssl_trusted_certificate' in line:
                lines[i] = '#' + line

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)

        print(f"Domain '{old_domain}' replaced with '{new_domain}' and ssl_trusted_certificate lines commented in '{file_path}'")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py file_path old_domain new_domain")
        sys.exit(1)

    file_path = sys.argv[1]
    old_domain = sys.argv[2]
    new_domain = sys.argv[3]

    replace_and_comment(file_path, old_domain, new_domain)
