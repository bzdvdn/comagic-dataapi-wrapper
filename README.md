# Comagic dataapi v2 wrapper

# Installation

Install using `pip`...

    pip install comagic-wrapper

#Doc
comagic doc - https://www.comagic.ru/support/api/data-api/

support full enpoints:
```python
(
    "calls_report", "communications_report", "virtual_numbers", "available_virtual_numbers",
    "sip_line_virtual_numbers", "sip_lines", "sip_line_password", "scenarios", "media_files",
    "campaigns","campaign_available_phone_numbers","campaign_available_redirection_phone_numbers",
    "campaign_parameter_weights", "sites", "site_blocks", "call_legs_report", "goals_report",
    "chats_report", "chat_messages_report", "offline_messages_report", "visitor_sessions_report",
    "financial_call_legs_report", "tags", "employees", "customers", "campaign_daily_stat",
)
```


# Usage

```python
from comagic import Comagic
client = Comagic("<login>", "<password>") # init retail api

or

client = Comagic(token="<token>")

```
# Sites
```python
# list of sites
# doc - https://www.comagic.ru/support/api/data-api/site/get_sites/
sites = client.sites.get(user_id='<user_id> if needed')

# create site
# doc - https://www.comagic.ru/support/api/data-api/site/create_sites/
data = {
   "domain_name": "string",
   "default_phone_number": "number",
   "default_scenario_id": "number",
   "user_id": "number",
   "industry_id": "number",
   "target_call_min_duration": "number",
   "track_subdomains_enabled": "boolean",
   "cookie_lifetime": "number",
   "campaign_lifetime": "number",
   "sales_enabled": "boolean",
   "second_communication_period": "number",
   "services_enabled": "boolean",
   "replacement_dynamical_block_enabled" : "boolean",
   "widget_link" : {
     "enabled": "boolean",
     "text": "string",
     "url": "string"
   },
   "show_visitor_id": {
     "enabled": "boolean",
     "element_id_value": "string",
     "message": "string",
     "length_visitor_id": "number"
   }
}
site = client.sites.create(user_id='<user_id> if needed', **data)

# delete
# doc - https://www.comagic.ru/support/api/data-api/site/delete_sites/
deleted  = client.sites.delete(user_id='<user_id> if needed', id = '<site_id>')

# update site
# doc - https://www.comagic.ru/support/api/data-api/site/update_sites/
update_site = client.sites.update(user_id='<user_id> if needed', **data)
```

# Site blocks
```python
# get site_block
# doc - https://www.comagic.ru/support/api/data-api/site/get_site_blocks/
site_blocks = client.site_blocks.get(user_id='<user_id> if needed', fields = [])

# create site block
# doc - https://www.comagic.ru/support/api/data-api/site/create_site_blocks/
site_block = client.site_blocks.create(site_id="number", name= "string", user_id='<user_id> if needed')

# update site block
# doc - https://www.comagic.ru/support/api/data-api/site/update_site_blocks/
updated_site_block = client.site_blocks.update(id='<number>', name= "string", user_id='<user_id> if needed')

# delete site block
# doc - https://www.comagic.ru/support/api/data-api/site/delete_site_blocks/
deleted = client.site_blocks.delete(user_id='<user_id> if needed', id= '<id>')
```
# Account
```python
# get account
# doc - https://www.comagic.ru/support/api/data-api/Account/
account = client.account.get()
```

# Virtual Numbers
```python
# get virtual numbers
# doc - https://www.comagic.ru/support/api/data-api/vn/get_virtual_numbers/
numbers = client.virtual_numbers.get(user_id='<user_id> if needed', limit=10, offset=0, fields=[], sort={})

# get available virtual numbers
# doc - https://www.comagic.ru/support/api/data-api/vn/get_available_virtual_numbers/
available_virtual_numbers = client.available_virtual_numbers.get(user_id='<user_id> if needed', limit=10, offset=0, fields=[], sort={})

# enable virtual number
# doc - https://www.comagic.ru/support/api/data-api/vn/enable_virtual_numbers/
enable = client.virtual_numbers.enable(user_id='<user_id> if needed', virtual_phone_number='number')

# disable virtual number
# doc - https://www.comagic.ru/support/api/data-api/vn/disable_virtual_numbers/
disable = client.virtual_numbers.disable(user_id='<user_id> if needed', virtual_phone_number='number')
```