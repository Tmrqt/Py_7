def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows + 1):
        result = []
        for y in range(1, num_columns + 1):
            res = operation(x, y)
            result.append(res)
        print([str(x) for x in result])

print_operation_table(lambda x, y: x * y)