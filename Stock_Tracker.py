stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3300
}

total = 0

print("📈 Stock Portfolio Tracker")

while True:
    name = input("Enter stock name (or 'done'): ").upper()

    if name == "DONE":
        break

    if name in stocks:
        qty = int(input("Enter quantity: "))
        value = stocks[name] * qty
        total += value
        print(f"Added {name}: {value}")
    else:
        print("⚠ Stock not available!")

print("\n💰 Total Investment:", total)

# Save result
with open("portfolio.txt", "w") as f:
    f.write("Total Investment: " + str(total))