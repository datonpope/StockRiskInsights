import openai
import os


api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")
openai.api_key = api_key


def query_gpt3(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


def generate_risk_factor_prompts(stock_symbol):
    prompts = [
        f"What are the main financial risk factors for {stock_symbol}?",
        f"What are the main operational risk factors for {stock_symbol}?",
        f"What are the main regulatory risk factors for {stock_symbol}?",
        f"What are the main competitive risk factors for {stock_symbol}?",
        f"What are the main market risk factors for {stock_symbol}?",
    ]
    return prompts


def analyze_stock_risk(stock_symbols):
    for symbol in stock_symbols:
        print(f"Risk factors for {symbol}:")
        prompts = generate_risk_factor_prompts(symbol)
        for prompt in prompts:
            insight = query_gpt3(prompt)
            print(f"- {insight}")
        print("\n")


if __name__ == "__main__":
    stock_symbols = ["AAPL", "GOOGL", "AMZN"]
    analyze_stock_risk(stock_symbols)

