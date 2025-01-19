import os
import openai
from playwright.async_api import async_playwright

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_dynamic_css_selector(html: str, llm_model: str = "gpt-3.5-turbo") -> str:
    """
    Use OpenAI's LLM to identify the dynamic CSS selector for reviews in the HTML.
    """
    prompt = f"""
    Extract the CSS selector for the reviews section from the following HTML content.
    HTML:
    {html}
    """
    response = openai.ChatCompletion.create(
        model=llm_model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["choices"][0]["message"]["content"].strip()

async def extract_reviews(url: str) -> dict:
    """
    Extract reviews from the given URL using Playwright and OpenAI for dynamic CSS.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)

        # Get the page content
        content = await page.content()

        # Identify CSS selector dynamically
        css_selector = await get_dynamic_css_selector(content)

        # Extract reviews using the identified CSS selector
        reviews = []
        reviews_elements = await page.query_selector_all(css_selector)
        for element in reviews_elements:
            title = await element.query_selector("title-selector").inner_text()
            body = await element.query_selector("body-selector").inner_text()
            rating = await element.query_selector("rating-selector").inner_text()
            reviewer = await element.query_selector("reviewer-selector").inner_text()

            reviews.append({
                "title": title,
                "body": body,
                "rating": int(rating),
                "reviewer": reviewer,
            })

        # Handle pagination
        while await page.query_selector("pagination-next-button-selector"):
            await page.click("pagination-next-button-selector")
            await page.wait_for_load_state("networkidle")

        await browser.close()

        return {
            "reviews_count": len(reviews),
            "reviews": reviews,
        }
