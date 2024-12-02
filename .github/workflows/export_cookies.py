import browser_cookie3

# Export cookies for YouTube
cookies = browser_cookie3.load(domain_name='youtube.com')
with open('cookies.txt', 'w') as f:
    for cookie in cookies:
        f.write(
            f"{cookie.domain}\t"
            f"{'TRUE' if cookie.domain.startswith('.') else 'FALSE'}\t"
            f"{cookie.path}\t"
            f"{'TRUE' if cookie.secure else 'FALSE'}\t"
            f"{cookie.expires if cookie.expires else 0}\t"
            f"{cookie.name}\t"
            f"{cookie.value}\n"
        )
