jsonformater_function = {
    "name": "extract_products",
    "description": "extract list of products from provided html page",
    "parameters": 
    {
        "type": "object",
        "properties": 
        {
            "products": 
            {
                "type": "array",
                "items": 
                {
                    "type": "object",
                    "properties": 
                    {
                        "product_name": 
                        {
                            "type": "string",
                            "description": "product's title (name)",
                        },
                        "product_price" :
                        {
                            "type": "string",
                            "description": "product's price",
                        },
                    },
                    "description": "product's properties"
                },
                "description": "List of prodocts' details from website content"
            }
        },
        "required": ["products"]
    }
}
