from menu import products


def calculate_tab(tab: list):
    sub_total = 0

    for table in tab:
        for product in products:
            if product["_id"] == table["_id"]:
                sub_total += product["price"] * table["amount"]

    return {"subtotal": f"${round(sub_total, 2)}"}
