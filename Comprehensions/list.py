tea_list = [
    "Green Tea",
    "Iced Green Tea",
    "Iced Vanilla Tea",
    "Ginger Tea"
];

# extract Iced teas only
iced_tea= [tea for tea in tea_list if "Iced" in tea];
print(f'Available Iced Teas are {", ".join(iced_tea)}')
