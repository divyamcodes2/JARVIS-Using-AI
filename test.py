from together import Together


def ai(prompt):
    


# auth defaults to os.environ.get("TOGETHER_API_KEY")
    client = Together(
        api_key="9de8a07254aa3162a37a46f2b91e9673d0ef0c4bb82ad7851975db0c9b14106a")

    response = client.chat.completions.create(
        model="Qwen/Qwen3-235B-A22B-fp8-tput",
        messages=[
            {"role": "user", "content": prompt}]
    )
    print(response.choices[0].message.content)
