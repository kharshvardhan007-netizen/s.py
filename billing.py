inventory = {
    "p101": {"name": "tata salt 1kg", "price": 28, "stock": 50, "gst": 5},
    "p102": {"name": "parle g 800g", "price": 80, "stock": 8, "gst": 5},
    "p103": {"name": "amul butter", "price": 285, "stock": 20, "gst": 12},
    "p104": {"name": "maggie masala", "price": 28, "stock": 50, "gst": 12}
}


def add_product(inventory, pid, qty, name, price, stock, gst):
    """Add a new product after validating its ID, price and stock."""

    if pid in inventory:
        return False

    if price < 0 or stock < 0:
        return False

    inventory[pid] = {
        "name": name,
        "price": price,
        "stock": stock,
        "gst": gst
    }

    return True


def update_stock(inventory, pid, qty):
    """Increase or decrease product stock without allowing negative stock."""

    if pid not in inventory:
        return False

    new_stock = inventory[pid]["stock"] + qty

    if new_stock < 0:
        return False

    inventory[pid]["stock"] = new_stock

    return True


def calculate_bill(inventory, cart):
    """Calculate subtotal, GST and total without modifying inventory."""

    items = []
    subtotal = 0
    gst_amount = 0

    for pid, qty in cart.items():

        if pid not in inventory:
            return None

        if qty <= 0:
            return None

        product = inventory[pid]

        if product["stock"] < qty:
            return None

        item_subtotal = product["price"] * qty
        item_gst = item_subtotal * product["gst"] / 100
        item_total = item_subtotal + item_gst

        items.append({
            "pid": pid,
            "name": product["name"],
            "qty": qty,
            "price": product["price"],
            "gst": product["gst"],
            "subtotal": item_subtotal,
            "gst_amount": item_gst,
            "total": item_total
        })

        subtotal += item_subtotal
        gst_amount += item_gst

    return {
        "items": items,
        "subtotal": subtotal,
        "gst_amount": gst_amount,
        "total": subtotal + gst_amount
    }


def print_invoice(bill):
    """Print a formatted invoice containing items, GST and total."""

    if bill is None:
        print("Cannot print invoice: invalid cart or insufficient stock.")
        return

    print("\n" + "=" * 65)
    print("                 KIRANA STORE INVOICE")
    print("=" * 65)

    print(f"{'Product':20} {'Qty':>5} {'Price':>8} "
          f"{'GST':>8} {'Total':>10}")

    print("-" * 65)

    for item in bill["items"]:
        print(f"{item['name'][:20]:20} "
              f"{item['qty']:>5} "
              f"{item['price']:>8.2f} "
              f"{item['gst_amount']:>8.2f} "
              f"{item['total']:>10.2f}")

    print("-" * 65)

    print(f"{'Subtotal':>50}: ₹{bill['subtotal']:.2f}")
    print(f"{'GST Amount':>50}: ₹{bill['gst_amount']:.2f}")
    print(f"{'Grand Total':>50}: ₹{bill['total']:.2f}")

    print("=" * 65)


def checkout(inventory, cart):
    """Calculate, print and complete a bill, reducing stock only if all items are available."""

    # First calculate the bill.
    bill = calculate_bill(inventory, cart)

    # If calculation fails, don't change stock.
    if bill is None:
        print("Checkout failed: unknown product or insufficient stock.")
        return False

    # Reduce stock only after the complete cart is validated.
    for pid, qty in cart.items():
        update_stock(inventory, pid, -qty)

    # Print invoice.
    print_invoice(bill)

    return True


# -----------------------------
# Example usage
# -----------------------------

cart = {
    "p101": 2,
    "p104": 1
}

checkout(inventory, cart)

print("\nRemaining Stock:")
print(inventory)