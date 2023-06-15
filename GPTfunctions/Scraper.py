scraper_function = {
    "name": "fetch_and_scrape_website_html_content",
    "description": "fetch a website content and then scrape the html content",
    "parameters": 
    {
        "type": "object",
        "properties": {
            "website_url": {
                "type": "string",
                "description": "An url website (website link)"
            },
        },
        "required": ["website_url"],
    },
}


