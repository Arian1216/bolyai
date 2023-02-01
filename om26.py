countries = {}

first_country = None
longest_name = ""
k_capital_city = None
four_letters_capital = None
country = ""
while True:
    if country == "":
        break
    input("Country:")
    input("Capital")
    input("EU")

for country in countries:#??????????????????????????????
    if not first_country or country["EU_accession"] < first_country["EU_accession"]:
        first_country = country
    if len(country["name"]) > len(longest_name):
        longest_name = country["name"]
    if country["capital"][0] == "K":
        k_capital_city = country
    if len(country["capital"]) == 4:
        four_letters_capital = country

result = (
    first_country
    if longest_name == first_country["name"] and k_capital_city == first_country
    else k_capital_city
    if longest_name == k_capital_city["name"] and four_letters_capital == k_capital_city
    else four_letters_capital
)

print("Az ország neve:", result["name"])
print("Fővárosa:", result["capital"])
print("EU csatlakozás éve:", result["EU_accession"])