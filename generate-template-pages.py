#!/usr/bin/env python3
"""
Script to generate individual HTML pages for each template letter
"""

templates = [
    {
        "id": "decline-review",
        "num": 2,
        "title": "Declining an Exploitative Review Request",
        "when": "When declining to review for a journal with high APCs or subscription prices.",
        "customization": ["Keep it brief but principled", "The journal may contact you again if they reform their model"],
        "impact": "Medium - sends a clear signal about your values",
        "content": """Subject: Re: Invitation to Review for [JOURNAL NAME]

Dear [EDITOR NAME],

Thank you for inviting me to review the manuscript "[MANUSCRIPT TITLE]" for [JOURNAL NAME]. I appreciate your confidence in my expertise.

However, I must respectfully decline this invitation. I have adopted a policy of prioritizing my reviewing time for non-profit and Diamond Open Access journals.

After reviewing [JOURNAL NAME]'s publishing model, I note that [it charges authors £[APC AMOUNT] to publish / it charges institutions £[SUBSCRIPTION PRICE] for access / both]. Given that peer review is unpaid labour, I believe this level of commercial extraction is incompatible with the values of scholarly communication.

I would be happy to reconsider if [JOURNAL NAME] transitions to a Diamond Open Access model (free to read, free to publish). In the meantime, I recommend the manuscript be submitted to [ALTERNATIVE DIAMOND OA JOURNAL IN FIELD].

I wish you success in finding an appropriate reviewer.

Best regards,
[YOUR NAME]
[YOUR TITLE]
[YOUR INSTITUTION]

---

Optional addition:

P.S. If you're interested in learning more about Diamond Open Access alternatives in [FIELD], I recommend visiting [DOAJ.org] or contacting me directly. Many of us are working to build better infrastructure for scholarly publishing.""",
        "examples": None
    },
    # I'll add the rest in follow-up calls
]

def create_template_page(template_data):
    """Generate HTML for a single template page"""

    customization_list = "\n                    ".join([f"<li>{item}</li>" for item in template_data["customization"]])

    examples_section = ""
    if template_data.get("examples"):
        examples_list = "\n                    ".join([f"<li>{item}</li>" for item in template_data["examples"]])
        examples_section = f"""
            <div style="background: var(--bg-light); padding: 1.5rem; border-radius: 8px; margin: 2rem 0;">
                <h3>Successful Examples / Context</h3>
                <ul>
                    {examples_list}
                </ul>
            </div>"""

    # Process content to highlight placeholders
    import re
    highlighted_content = re.sub(r'\[([^\]]+)\]', r'<span class="placeholder">[\1]</span>', template_data["content"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Template letter: {template_data['title']}">
    <title>Template: {template_data['title']} | The Revolution Won't Be Paywalled</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        .template-container {{
            background: var(--bg-light);
            padding: 2rem;
            border-radius: 8px;
            margin: 2rem 0;
            border-left: 4px solid var(--primary-red);
        }}
        .template-header {{
            background: var(--text-dark);
            color: var(--text-light);
            padding: 1.5rem;
            border-radius: 8px 8px 0 0;
            margin: -2rem -2rem 1.5rem -2rem;
        }}
        .template-header h2 {{
            margin: 0 0 0.5rem 0;
            color: var(--accent-gold);
        }}
        .template-header p {{
            margin: 0;
            opacity: 0.9;
        }}
        .template-content {{
            background: white;
            padding: 2rem;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
            line-height: 1.8;
            white-space: pre-wrap;
            overflow-x: auto;
        }}
        .template-meta {{
            background: #fff3cd;
            border-left: 4px solid var(--accent-gold);
            padding: 1rem 1.5rem;
            margin: 1.5rem 0;
            border-radius: 4px;
        }}
        .template-meta h4 {{
            margin-top: 0;
            color: var(--text-dark);
        }}
        .btn-group {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            margin: 2rem 0;
        }}
        .placeholder {{
            color: var(--primary-red);
            font-weight: 600;
        }}
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="container">
                <div class="logo">
                    <a href="index.html"><img src="assets/trwbp_logo.svg" alt="The Revolution Won't Be Paywalled" class="logo-img"></a>
                </div>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="manifesto.html">Manifesto</a></li>
                    <li><a href="action.html">Take Action</a></li>
                    <li><a href="resources.html">Resources</a></li>
                    <li><a href="about.html">About</a></li>
                </ul>
                <div class="mobile-menu-toggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </nav>
    </header>

    <main>
        <div class="page-content">
            <p><a href="templates.html">← Back to All Templates</a></p>

            <h1>Template {template_data['num']}: {template_data['title']}</h1>

            <div class="template-meta">
                <h4>📋 When to Use This Template</h4>
                <p>{template_data['when']}</p>

                <h4 style="margin-top: 1.5rem;">✏️ Customization Notes</h4>
                <ul style="margin: 0.5rem 0;">
                    {customization_list}
                    <li>Replace all <span class="placeholder">[BRACKETED]</span> text with your specific information</li>
                </ul>

                <h4 style="margin-top: 1.5rem;">💪 Impact Level</h4>
                <p><strong>{template_data['impact']}</strong></p>
            </div>

            <div class="btn-group">
                <button onclick="copyTemplate()" class="btn btn-primary">📋 Copy Template</button>
                <a href="assets/TRWBP_Template_Letters.md" download class="btn btn-secondary">⬇️ Download All Templates</a>
            </div>

            <div class="template-container">
                <div class="template-header">
                    <h2>Email Template</h2>
                    <p>Copy and customize the text below</p>
                </div>
                <div class="template-content" id="templateText">{highlighted_content}</div>
            </div>

            <div class="btn-group">
                <button onclick="copyTemplate()" class="btn btn-primary">📋 Copy Template</button>
            </div>
{examples_section}
            <div style="text-align: center; margin: 3rem 0;">
                <p><a href="templates.html" class="btn btn-secondary">← View All Templates</a></p>
            </div>
        </div>
    </main>

    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>The Movement</h4>
                    <ul>
                        <li><a href="manifesto.html">Manifesto</a></li>
                        <li><a href="action.html">Take Action</a></li>
                        <li><a href="resources.html">Resources</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Connect</h4>
                    <ul>
                        <li><a href="about.html">About</a></li>
                        <li><a href="mailto:adam@fairresconman.com">Contact</a></li>
                        <li><a href="https://www.fairresconman.com" target="_blank">FAIR-Res-ConMan</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Share</h4>
                    <div class="hashtags">
                        <span>#ScholarlyCommons</span>
                        <span>#TRWBP</span>
                        <span>#DiamondOA</span>
                    </div>
                    <p style="margin-top: 1rem; font-weight: 600;">
                        <a href="https://bit.ly/_TRWBP_" target="_blank" style="color: var(--accent-gold);">🔗 bit.ly/_TRWBP_</a>
                    </p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 The Revolution Won't Be Paywalled | Initiated by Dr Adam Vials Moore</p>
                <p class="footer-license">Content licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">CC-BY 4.0</a> | Share freely with attribution</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
    <script>
        function copyTemplate() {{
            const templateText = document.getElementById('templateText').innerText;
            navigator.clipboard.writeText(templateText).then(function() {{
                alert('Template copied to clipboard! You can now paste it into your email client and customize the [BRACKETED] sections.');
            }}, function(err) {{
                alert('Failed to copy template. Please select and copy the text manually.');
            }});
        }}
    </script>
</body>
</html>"""

    return html


if __name__ == "__main__":
    # Generate the decline-review template as example
    html = create_template_page(templates[0])
    with open(f"template-{templates[0]['id']}.html", "w") as f:
        f.write(html)
    print(f"Created template-{templates[0]['id']}.html")
