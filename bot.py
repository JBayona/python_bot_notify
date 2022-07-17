from wsgiref.headers import Headers
import requests
import time


GRAPHIC_CARD_3060 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402&intl=nosplash"
GO_PRO_4K = "https://www.bestbuy.com/site/gopro-hero10-black-action-camera/6474501.p?skuId=6474501&intl=nosplash"
GRAPHIC_CARD_3070 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789&intl=nosplash"
SAMSUNG_QLED_4K = "https://www.bestbuy.com/site/samsung-65-class-q80b-qled-4k-smart-tizen-tv/6503080.p?skuId=6503080&intl=nosplash"

CART_CLASS = "c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"

# Step 1: Fetch the page from the products.
# Step 2: Verify if we have the inventory.
# Step 3: Notify when products are available

PRODUCTS = [
  ("RTX 3060", GRAPHIC_CARD_3060),
  ("GO PRO", GO_PRO_4K),
  ("RTX 3070", GRAPHIC_CARD_3070),
  ("SAMSUNG QLED 4K", SAMSUNG_QLED_4K)
]

HEADERS = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
  "Accept" :"*/*"
}

def save(content: str, name: str = "response.html") -> None:
  with open(name, "w") as f:
    f.write(content)

def fetch_page(url: str) -> str:
  res = requests.get(url, headers=HEADERS)
  return res.text

def item_does_exist(html: str) -> bool:
  return CART_CLASS in html

html = fetch_page(GRAPHIC_CARD_3060)
# save(html)

def main() -> None:
  # Check constantly until we are done
  while(True):
    for name, url in PRODUCTS:
      html = fetch_page(url)
      if item_does_exist(html):
        print(f"RUN! There's {name} in stock! Buy it right away: {url}")
      else:
        print(f"{name} is not in stock right now :(")
    time.sleep(5)
      
# Run the main module
if __name__ == "__main__":
  main()
