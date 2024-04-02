import json

data='''
[{ 
	"tamanyo": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "pepperoni", "albahaca"],
	"queso_extra": false,
	"delivery": true,
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": null,
		"correo": "janedoe@email.com"
	}
},{ 
	"tamanyo": "mediana",
	"precio": 17.50,
	"toppings": ["champinones", "pepperoni", "albahaca"],
	"queso_extra": false,
	"delivery": true,
	"cliente": {
		"nombre": "Manuel torres",
		"telefono": null,
		"correo": "manuel@email.com"
	}
}]'''

info = json.loads(data)
for item in info:
    print('Name:', item["cliente"]["nombre"], item["cliente"]["correo"])
    print('Precio:', item["precio"])
