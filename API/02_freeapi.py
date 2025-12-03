import requests

def fetch_random_products_freeapi():
    url= "https://api.freeapi.app/api/v1/public/randomproducts"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        product_data = data["data"]
        id = product_data["data"][0]["id"]
        title = product_data["data"][0]["title"]
        description = product_data["data"][0]["description"]
        price = product_data["data"][0]["price"]
        brand = product_data["data"][0]["brand"]
        return id, title,description,price, brand
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        id, title,description,price,brand = fetch_random_products_freeapi()
        print(f"id: {id}\nproduct name: {title}\ndescription: {description}\nprice: {price}\nbrand: {brand}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()