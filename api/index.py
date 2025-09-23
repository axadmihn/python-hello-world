from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>NorthProt | Adaptive Cybersecurity &amp; Infrastructure Protection</title>
    <style>
        :root {
            --primary: #0b3d91;
            --primary-light: #1f61c2;
            --accent: #69f0ae;
            --dark: #0f172a;
            --muted: #e2e8f0;
            --text: #0b1220;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
            color: var(--text);
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.92) 0%, rgba(15, 23, 42, 0.98) 65%, rgba(11, 61, 145, 0.95) 100%);
            min-height: 100vh;
        }

        header {
            background: linear-gradient(135deg, rgba(11, 61, 145, 0.95), rgba(31, 97, 194, 0.85)),
                url('https://images.unsplash.com/photo-1517430816045-df4b7de11d1d?auto=format&fit=crop&w=1500&q=80') center/cover;
            color: white;
            padding: 4rem 1.5rem 6rem;
            position: relative;
            overflow: hidden;
        }

        header::after {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(120deg, rgba(11, 61, 145, 0.75), rgba(15, 23, 42, 0.9));
            z-index: 0;
        }

        .hero-content {
            max-width: 1100px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 4rem;
        }

        nav .brand {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        nav .brand span {
            display: inline-block;
            background: rgba(105, 240, 174, 0.2);
            color: var(--accent);
            padding: 0.5rem 0.75rem;
            border-radius: 9999px;
            font-weight: 600;
            letter-spacing: 0.08em;
        }

        nav .brand h1 {
            font-size: 1.75rem;
            margin: 0;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }

        nav ul {
            list-style: none;
            display: flex;
            gap: 1.5rem;
            margin: 0;
            padding: 0;
        }

        nav a {
            color: rgba(255, 255, 255, 0.85);
            text-decoration: none;
            font-weight: 500;
            letter-spacing: 0.05em;
        }

        nav a:hover,
        nav a:focus {
            color: white;
        }

        .headline {
            max-width: 720px;
        }

        .headline h2 {
            font-size: clamp(2.5rem, 4vw, 3.5rem);
            margin: 0 0 1rem;
            line-height: 1.2;
        }

        .headline p {
            font-size: 1.1rem;
            color: rgba(255, 255, 255, 0.85);
            line-height: 1.7;
            margin-bottom: 2rem;
        }

        .cta-group {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            align-items: center;
        }

        .btn-primary,
        .btn-secondary {
            padding: 0.9rem 1.6rem;
            border-radius: 9999px;
            font-weight: 600;
            text-decoration: none;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .btn-primary {
            background: var(--accent);
            color: var(--dark);
            box-shadow: 0 10px 20px rgba(105, 240, 174, 0.35);
        }

        .btn-secondary {
            background: transparent;
            border: 1px solid rgba(255, 255, 255, 0.35);
            color: white;
        }

        .btn-primary:hover,
        .btn-secondary:hover {
            transform: translateY(-2px);
        }

        main {
            margin-top: -3.5rem;
            padding: 0 1.5rem 4rem;
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
        }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1.5rem;
        }

        .card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 20px 45px rgba(15, 23, 42, 0.3);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.6);
        }

        .card h3 {
            margin-top: 0;
            font-size: 1.35rem;
            color: var(--primary);
        }

        .card p {
            margin-bottom: 0;
            color: #334155;
            line-height: 1.6;
        }

        section {
            margin: 4rem 0;
        }

        section h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: white;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        section p.section-intro {
            color: var(--muted);
            max-width: 720px;
            line-height: 1.7;
        }

        .pill-list {
            list-style: none;
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
            padding: 0;
            margin: 1.5rem 0 0;
        }

        .pill-list li {
            padding: 0.6rem 1rem;
            border-radius: 9999px;
            background: rgba(148, 163, 184, 0.25);
            color: white;
            font-weight: 500;
        }

        .contact-panel {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .contact-card {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(105, 240, 174, 0.5);
            border-radius: 18px;
            padding: 1.75rem;
            color: white;
        }

        .contact-card h3 {
            margin-top: 0;
            color: var(--accent);
        }

        .contact-card a {
            color: white;
            text-decoration: none;
            font-weight: 600;
        }

        footer {
            border-top: 1px solid rgba(148, 163, 184, 0.25);
            color: rgba(226, 232, 240, 0.85);
            padding: 2rem 1.5rem 3rem;
        }

        footer .container {
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
        }

        footer small {
            color: rgba(148, 163, 184, 0.85);
        }

        @media (max-width: 640px) {
            nav ul {
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: flex-start;
            }

            .cta-group {
                flex-direction: column;
                align-items: flex-start;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class=\"hero-content\">
            <nav>
                <div class=\"brand\">
                    <span>NorthProt</span>
                    <h1>Security Without the Guesswork</h1>
                </div>
                <ul>
                    <li><a href=\"#services\">Services</a></li>
                    <li><a href=\"#approach\">Approach</a></li>
                    <li><a href=\"#process\">Engagement</a></li>
                    <li><a href=\"#contact\">Contact</a></li>
                </ul>
            </nav>
            <div class=\"headline\">
                <h2>Defend your digital frontier with an adaptive protection partner.</h2>
                <p>NorthProt brings enterprise-grade cybersecurity, infrastructure resilience, and incident readiness to
                    ambitious teams moving to <strong>northprot.com</strong>. We simplify the path from risk discovery to
                    confident operations so you can focus on delivering value.</p>
                <div class=\"cta-group\">
                    <a class=\"btn-primary\" href=\"mailto:admin@northprot.com\">Schedule a consultation</a>
                    <a class=\"btn-secondary\" href=\"#services\">Explore capabilities</a>
                </div>
            </div>
        </div>
    </header>

    <main>
        <div class=\"container\">
            <section id=\"services\">
                <h2>Core Services</h2>
                <p class=\"section-intro\">From proactive defense to real-time incident response, NorthProt provides a
                    full stack of protection tailored to growing organizations that need to earn trust fast.</p>
                <div class=\"card-grid\">
                    <article class=\"card\">
                        <h3>Managed Cybersecurity</h3>
                        <p>Threat hunting, security monitoring, and tailored controls aligned to your regulatory and
                            operational requirements.</p>
                    </article>
                    <article class=\"card\">
                        <h3>Infrastructure Hardening</h3>
                        <p>Resilient cloud, network, and endpoint architectures designed to scale with your expansion to
                            northprot.com and beyond.</p>
                    </article>
                    <article class=\"card\">
                        <h3>Incident Preparedness</h3>
                        <p>Response runbooks, tabletop exercises, and on-call expertise to contain threats before they
                            disrupt your business.</p>
                    </article>
                    <article class=\"card\">
                        <h3>Compliance Enablement</h3>
                        <p>Gap assessments, policy development, and executive-ready reporting across SOC 2, ISO 27001, and
                            industry-specific benchmarks.</p>
                    </article>
                </div>
            </section>

            <section id=\"approach\">
                <h2>Why NorthProt</h2>
                <p class=\"section-intro\">Your security partner should evolve with every release, sprint, and go-to-market
                    push. NorthProt blends automation with human insight to keep pace with dynamic teams.</p>
                <ul class=\"pill-list\">
                    <li>Adversary-informed monitoring</li>
                    <li>Infrastructure observability</li>
                    <li>Clear communication &amp; executive briefings</li>
                    <li>Business-aligned security roadmaps</li>
                    <li>Embedded incident response specialists</li>
                    <li>Data governance frameworks</li>
                </ul>
            </section>

            <section id=\"process\">
                <h2>Engagement Roadmap</h2>
                <p class=\"section-intro\">We guide you from first conversation to ongoing optimization with transparent,
                    actionable milestones.</p>
                <div class=\"card-grid\">
                    <article class=\"card\">
                        <h3>1. Discover</h3>
                        <p>We assess your current footprint, review lessons learned from axnmihn.com, and map priority
                            assets across northprot.com.</p>
                    </article>
                    <article class=\"card\">
                        <h3>2. Secure</h3>
                        <p>Deploy layered controls, observability tooling, and automated guardrails matched to your
                            operational tempo.</p>
                    </article>
                    <article class=\"card\">
                        <h3>3. Respond</h3>
                        <p>Establish incident playbooks, practice scenarios, and 24/7 escalation channels so issues are
                            resolved before customers notice.</p>
                    </article>
                    <article class=\"card\">
                        <h3>4. Evolve</h3>
                        <p>Continuous improvement checkpoints ensure NorthProt stays aligned with your roadmap and risk
                            landscape.</p>
                    </article>
                </div>
            </section>

            <section id=\"cta\">
                <h2>Move Forward with Confidence</h2>
                <p class=\"section-intro\">Your brand is migrating domains; your protections should upgrade too. Let’s design
                    a defense program that fits how your team works today and where you plan to go next.</p>
                <div class=\"cta-group\">
                    <a class=\"btn-primary\" href=\"mailto:admin@northprot.com\">Plan your migration security review</a>
                    <a class=\"btn-secondary\" href=\"tel:+12025550123\">Call our advisory desk</a>
                </div>
            </section>

            <section id=\"contact\">
                <h2>Contact</h2>
                <div class=\"contact-panel\">
                    <article class=\"contact-card\">
                        <h3>Direct Support</h3>
                        <p>Email <a href=\"mailto:admin@northprot.com\">admin@northprot.com</a> to open a ticket or request
                            a tailored briefing.</p>
                    </article>
                    <article class=\"contact-card\">
                        <h3>Schedule a Session</h3>
                        <p>We host remote and on-site workshops to align your leaders and engineers around a cohesive security
                            strategy.</p>
                    </article>
                    <article class=\"contact-card\">
                        <h3>Stay Informed</h3>
                        <p>Quarterly threat reports and infrastructure advisories keep stakeholders aware of evolving
                            risks and controls.</p>
                    </article>
                </div>
            </section>
        </div>
    </main>

    <footer>
        <div class=\"container\">
            <strong>NorthProt</strong>
            <small>&copy; {year} NorthProt. All rights reserved. Operating globally from our headquarters in the Pacific
                Northwest.</small>
            <small>Transitioning from axnmihn.com to northprot.com with a renewed focus on proactive security.</small>
        </div>
    </footer>
</body>
</html>""".format(year=self._current_year())

        self.wfile.write(html.encode('utf-8'))

    def _current_year(self):
        from datetime import datetime
        return datetime.utcnow().year
