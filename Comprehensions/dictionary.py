tea_prices_inr={
    "Ginger Chai":40,
    "Green Tea":50,
    "Lemon Tea":70
}
print(tea_prices_inr)

tea_price_usd= {tea :(price/ 80) for (tea, price) in tea_prices_inr.items()}

print(tea_price_usd)