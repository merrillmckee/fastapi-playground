from typing import Optional

# code from https://fastapi.tiangolo.com/python-types


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e


def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


if __name__ == "__main__":
    print(get_full_name("john", "doe"))
