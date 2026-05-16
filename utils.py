def print_number_table(
    grid: list[list[int | float]],
    *,
    row_start: int = 0,
    col_start: int = 0,
) -> None:
    """
    Print a 2D array of numbers with aligned columns (each column as wide as
    its widest entry). Rows are joined with single spaces.

    A header row shows column indices (default col_start + j); each line is
    prefixed with its row index (default row_start + i) for debugging.
    A vertical bar and rule separate indices from cell values.
    """
    if not grid:
        return

    nrows = len(grid)
    str_rows = [[str(cell) for cell in row] for row in grid]
    ncols = max(len(r) for r in str_rows)
    widths = [0] * ncols

    for row in str_rows:
        for j in range(ncols):
            if j < len(row):
                widths[j] = max(widths[j], len(row[j]))

    for j in range(ncols):
        widths[j] = max(widths[j], len(str(col_start + j)))

    row_label_w = max(len(str(row_start + i)) for i in range(nrows))

    bar = " | "
    header_pad = " " * row_label_w
    header_nums = " ".join(str(col_start + j).rjust(widths[j]) for j in range(ncols))
    print(f"{header_pad}{bar}{header_nums}")

    rule = f"{'-' * row_label_w}-+-{'-' * len(header_nums)}"
    print(rule)

    for i, row in enumerate(str_rows):
        label = str(row_start + i).rjust(row_label_w)
        parts = []
        for j in range(ncols):
            cell = row[j] if j < len(row) else ""
            parts.append(cell.rjust(widths[j]))
        print(f"{label}{bar}{' '.join(parts)}")
