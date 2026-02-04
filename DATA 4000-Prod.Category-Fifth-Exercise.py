# Prompt for product name
product = input("What's the product name? ")

# Clean the input: remove extra spaces and convert to lowercase
clean_product = product.strip().lower()

# Determine category using match-case
match clean_product:
    case "electronics" | "gadget":
        category = "High Margin"
    case name if name.startswith("tech"):
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    case _:
        category = "Uncategorized - Review Needed"

# Print the result
print(f"Product: {clean_product} | Category: {category}")