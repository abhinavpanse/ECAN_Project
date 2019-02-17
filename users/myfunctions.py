import requests
import shopify
import datetime


API_KEY = '201ed3bdaf70da2b586304331a8ca37d' #fake
PASSWORD = '77d6fcc4a105dfce3c68efe85a4c8041'	#fake
SHOP_NAME = 'lastgrey'		#fake

shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()

print("shopify shop connected ",SHOP_NAME)


def gendisc(strcode ):
	strcode = strcode.upper()
	price_rule = shopify.PriceRule()
	new_discount = shopify.DiscountCode()
	price_rule.title = strcode
	price_rule.target_type = "line_item"
	price_rule.target_selection = "all"
	price_rule.allocation_method = "across"
	price_rule.value_type = "percentage"
	price_rule.value = -20.0
	price_rule.customer_selection = "all"
	price_rule.starts_at = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
	price_rule.save()
	dc = new_discount.create( {
		'price_rule_id': price_rule.id,
		'code': strcode,
		'value_type':'percentage',
		'value': -20.0
	})
	return (dc.is_valid())  #returns status if valid or not


def send_success_message(useremail):
    return requests.post(
        "https://api.mailgun.net/v3/groinstagram.com/messages",
        auth=("api", "key-f1f5dee51f2f40f9b4fd24f5a53a3f42"),
        data={"from": "Excited User <abhinav@groinstagram.com>",
              "to": [useremail],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

def send_fail_message(useremail):
    return requests.post(
        "https://api.mailgun.net/v3/groinstagram.com/messages",
        auth=("api", "key-f1f5dee51f2f40f9b4fd24f5a53a3f42"),
        data={"from": "Excited User <abhinav@groinstagram.com>",
              "to": [useremail],
              "subject": "fail",
              "text": "failed"})
