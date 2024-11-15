def read_file_permissions():

    n = int(input())

    permissions = {}

    for _ in range(n):
        file_info = input().split()
        filename = file_info[0]
        permissions[filename] = set(file_info[1:])

    return permissions


def process_requests(permissions):
    m = int(input())

    results = []
    for _ in range(m):
        operation, filename = input().split()

        if filename not in permissions:
            results.append("Access denied")
            continue

        if operation == "read" and "R" in permissions[filename]:
            results.append("OK")
        elif operation == "write" and "W" in permissions[filename]:
            results.append("OK")
        elif operation == "execute" and "X" in permissions[filename]:
            results.append("OK")
        else:
            results.append("Access denied")

    return results

permissions = read_file_permissions()
results = process_requests(permissions)
for result in results:
    print(result)
