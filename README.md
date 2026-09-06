# GPT-4 Boilerplate

Minimal **Python chat sketch** against OpenAI’s chat API — one prompt, one system preheader, print the reply.

Part of the [Initial Visuals](https://github.com/initialvisuals) toolkit / game lab.

### Status

**Archive / teaching stub.** Uses the older `openai.ChatCompletion` style. Prefer a current OpenAI SDK example for new work. Kept as a tiny reference for “how we started.”

### What’s in the box

| Path | What |
|------|------|
| `gpt_example.py` | Single-file prompt → response |
| `LICENSE` | License |

### Quick start

```bash
pip install openai   # version compatible with the script era, or adapt to the new SDK
export OPENAI_API_KEY=your_api_key
python gpt_example.py
```

Use an environment variable for the key. Do not hardcode secrets in the file.

### Related

Richer CLI experiment: [`GPT_Terminal`](https://github.com/initialvisuals/GPT_Terminal).

### License

See [LICENSE](LICENSE).

---

**Initial Visuals** — tools, sims, games, and experiments.
