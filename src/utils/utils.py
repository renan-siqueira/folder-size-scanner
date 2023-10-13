def convert_size_to_bytes(size_str):
    size_value = float(size_str[:-2])
    unit = size_str[-2:].lower()

    if unit == "kb":
        return size_value * 1024
    elif unit == "mb":
        return size_value * (1024 ** 2)
    elif unit == "gb":
        return size_value * (1024 ** 3)
    elif unit == "tb":
        return size_value * (1024 ** 4)
    else:
        raise ValueError(f"Invalid unit {unit}. Use KB, MB, GB, or TB.")
