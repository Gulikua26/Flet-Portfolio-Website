import flet as ft
import os

# This finds the exact folder your portfolio.py is running in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "photo_b64.txt")

# Use 'file_path' instead of just the filename string
with open(file_path, "r") as f:
    photo_data = f.read()
    photo_data = f.read().strip().replace("\n", "").replace("\r", "")

photo_src = f"data:image/jpeg;base64,{photo_data}"
def main(page: ft.Page):
    page.title = "Ndapandula Gulikua | Web Portfolio"
    page.bgcolor = "#0f172a"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0
    page.fonts = {
        "Poppins": "https://fonts.gstatic.com/s/poppins/v20/pxiEyp8kv8JHgFVrJJfecg.woff2"
    }
    page.theme = ft.Theme(font_family="Poppins")

    PRIMARY = "#38bdf8"
    SECONDARY = "#818cf8"
    BG_CARD = "#1e293b"
    BG_BORDER = "#334155"
    TEXT_MAIN = "#f1f5f9"
    TEXT_SUB = "#94a3b8"
    SUCCESS = "#4ade80"

    def section_title(icon, text):
        return ft.Row([
            ft.Text(icon, size=22),
            ft.Text(text, size=22, weight=ft.FontWeight.BOLD, color=TEXT_MAIN),
        ], spacing=10)

    def card(content):
        return ft.Container(
            content=content,
            bgcolor=BG_CARD,
            border_radius=14,
            padding=20,
            margin=ft.margin.only(bottom=14),
            border=ft.border.all(1, BG_BORDER),
        )

    def badge(text, color=PRIMARY):
        return ft.Container(
            content=ft.Text(text, size=11, color=color,
                            weight=ft.FontWeight.BOLD),
            bgcolor=f"{color}22",
            border_radius=20,
            padding=ft.padding.symmetric(horizontal=10, vertical=4),
        )

    def nav_button(label, icon, on_click=None):
        return ft.TextButton(
            content=ft.Row([
                ft.Icon(icon, color=PRIMARY, size=16),
                ft.Text(label, color=TEXT_MAIN, size=13,
                        weight=ft.FontWeight.W_500),
            ], spacing=6),
            style=ft.ButtonStyle(
                overlay_color="#38bdf822",
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
            on_click=on_click,
        )

    navbar = ft.Container(
        content=ft.Row([
            ft.Text("NG", size=18, weight=ft.FontWeight.BOLD, color=PRIMARY),
            ft.Row([
                nav_button("Timeline", ft.Icons.CALENDAR_TODAY),
nav_button("MATLAB", ft.Icons.SCHOOL),
nav_button("Blog", ft.Icons.ARTICLE),
nav_button("GitHub", ft.Icons.CODE),
nav_button("Contact", ft.Icons.MAIL_OUTLINE),
            ], spacing=4),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        bgcolor=BG_CARD,
        padding=ft.padding.symmetric(horizontal=40, vertical=14),
        border=ft.border.only(bottom=ft.BorderSide(1, BG_BORDER)),
    )

    header = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Container(
                    content=ft.Image(
                        src=photo_src,
                        width=110,
                        height=110,
                        fit="cover",
                        border_radius=ft.border_radius.all(55),
                    
                    ),
                    border_radius=ft.border_radius.all(58),
                    border=ft.border.all(3, PRIMARY),
                    padding=3,
                ),
                ft.Column([
                    ft.Text("Ndapandula Gulikua",
                            size=38, weight=ft.FontWeight.BOLD,
                            color=TEXT_MAIN),
                    ft.Text("Computer Programming I • Semester 1, 2026",
                            size=15, color=TEXT_SUB),
                    ft.Row([
                        badge("Python Developer"),
                        badge("Flet Framework", PRIMARY),
                        badge("GitHub", SUCCESS),
                    ], spacing=8),
                ], spacing=10, expand=True),
            ], spacing=24),
        ], spacing=10),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#1e293b", "#0f172a"]
        ),
        padding=ft.padding.symmetric(horizontal=40, vertical=40),
        border=ft.border.only(bottom=ft.BorderSide(1, BG_BORDER)),
    )

    timeline_entries = [
            ("Weeks 1–2", "Team formation and role allocation. Set up GitHub, Expo, React Native, and Firebase environments. Brainstormed and selected the MineOps project idea as a group."),
            ("Weeks 3–4", "Developed project concepts and features. Presented the project proposal to the lecturer and received approval and registration of the final project idea."),
            ("Weeks 5–6", "Gathered and documented system requirements. Identified functional and non-functional requirements. Completed initial Firestore database design."),
            ("Weeks 7–8", "Created use case diagrams and system workflows. Reviewed and refined project requirements. Completed and submitted the SRS document."),
            ("Weeks 9–10", "Designed application screens in Figma. Created navigation structure and user flows. Developed the interactive prototype."),
            ("Final Week", "Developed the mobile application using React Native and Expo. Integrated Firebase Authentication and Firestore. Completed testing, generated APK with EAS Build, and submitted the final project."),
        ]

    timeline_section = ft.Column([
        section_title("🗓", "Project Timeline"),
        ft.Text("Weekly log of your specific contributions to the group project.",
                color=TEXT_SUB, size=13),
        ft.Column([
            card(ft.Row([
                ft.Container(
                    content=ft.Text(week, color=PRIMARY,
                                    weight=ft.FontWeight.BOLD, size=13),
                    width=80,
                ),
                ft.Container(width=1, height=40, bgcolor=BG_BORDER),
                ft.Text(detail, color=TEXT_SUB, size=13, expand=True),
            ], spacing=16))
            for week, detail in timeline_entries
        ])
    ], spacing=12)

    matlab_courses = [
    ("MATLAB Onramp", "20 March 2026", "https://drive.google.com/file/d/1aIoL_r--hNk1bESx7i58AAG8Tzn7aGFt/view?usp=sharing"),
    ("Simulink Onramp", "11 April 2026", "https://drive.google.com/file/d/1lr9q8MIu58UNLD24Pn40xSNGtV_Lintg/view?usp=sharing"),
    ("Calculations with Vectors and Matrices", "24 April 2026", "https://drive.google.com/file/d/1vcWIcMQLzteuMdKchVq4gvLsNnG1QgVG/view?usp=sharing"),
    ("Core MATLAB Skills (Learning Path)", "24 April 2026", "https://drive.google.com/file/d/1MPR48tT_zmDszczUOEDk5yCm4yW5KcrY/view?usp=sharing"),
    ("Explore Data with MATLAB Plots", "23 April 2026", "https://drive.google.com/file/d/1bK72vvQC82vRtPJNK0YOCJcjD7JU2xmT/view?usp=sharing"),
    ("Make and Manipulate Matrices", "24 April 2026", "https://drive.google.com/file/d/1ammWF8qd_dDGAwudHL9wvsE9Qu5T0Xmf/view?usp=sharing"),
    ("Programming Constructs", "29 April 2026", "https://drive.google.com/file/d/1lm5ijR9-AOfVA2-G76l6u-BGEWkLU8bJ/view?usp=sharing"),
]

    matlab_section = ft.Column([
        section_title("🎓", "MATLAB Achievement Hub"),
        ft.Text("Proof of completion for 7 short self-paced courses — MathWorks Learning Center.",
                color=TEXT_SUB, size=13),
        card(ft.Column([
            ft.Row([
                ft.Text("Progress", color=TEXT_SUB, size=13),
                ft.Text("7 / 7 Completed", color=PRIMARY, size=13,
                        weight=ft.FontWeight.BOLD),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.ProgressBar(value=1, bgcolor=BG_BORDER, color=PRIMARY),
            ft.Divider(color=BG_BORDER),
            *[ft.Row([
                ft.Icon(ft.Icons.CHECK_CIRCLE, color=SUCCESS, size=16),
                ft.Text(course, color=TEXT_MAIN, size=13, expand=True),
                ft.Text(date, color=TEXT_SUB, size=12),
                ft.Container(
                    content=ft.Text(
                        "View Certificate",
                        color=PRIMARY,
                        size=12,
                        weight=ft.FontWeight.BOLD,
                    ),
                    url=filename,
  
                ),
            ], spacing=10) for course, date, filename in matlab_courses]
        ], spacing=10))
    ], spacing=12)

    blog_posts = [
        ("What is a While Loop?",
         "Placeholder — write your technical explanation here. Embed a video link once ready."),
        ("Understanding f-strings in Python",
         "Placeholder — write your technical explanation here. Embed a video link once ready."),
        ("How Functions Work",
         "Placeholder — write your technical explanation here. Embed a video link once ready."),
    ]

    blog_section = ft.Column([
        section_title("📝", "Semester Project Reflection"),
        ft.Text("A personal video reflection detailing individual contributions to the SyntaxCrew MineOps project.",
                color=TEXT_SUB, size=13),
        card(ft.Column([
            ft.Text("Semester Reflection Video", weight=ft.FontWeight.BOLD,
                    color=TEXT_MAIN, size=15),
            ft.Text("Watch my individual contribution summary for the MineOps group project — covering my role as Firebase Lead, environment setup, research, and final deliverables.",
                    color=TEXT_SUB, size=13),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.PLAY_CIRCLE, color=PRIMARY, size=60),
                    ft.Text("Click to Play Reflection Video", color=PRIMARY,
                            size=14, weight=ft.FontWeight.BOLD),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                url="https://drive.google.com/file/d/1hBYer8hat_JDcggX1YWY7F7xVcrbODYP/preview",
                bgcolor=BG_BORDER,
                border_radius=12,
                padding=ft.padding.symmetric(horizontal=20, vertical=40),
            ),
        ], spacing=12))
    ], spacing=12)

    

    commits = [
        ("Add files via upload", "Uploaded core context files — ThemeContext.js, AuthContext.js, HazardContext.js, ShiftContext.js, LocalizationContext.js — providing the app's theme and state management foundation.", "https://github.com/makotajr006/UNAM-I3691CP-SyntaxCrew-MineOps/commit/f92b14e1afce3288b00c7b3c04a7e87be7f5af2a"),
        ("Add files via upload", "Second upload commit reinforcing context structure for the MineOps scaffold.", "https://github.com/makotajr006/UNAM-I3691CP-SyntaxCrew-MineOps/commit/9a905c2057a3fc022d208201e51b8c8286a4e8a3"),
        ("Update Group_14_data.txt", "Registered personal details (name, student number, GitHub username) in the group data file.", "https://github.com/makotajr006/UNAM-I3691CP-SyntaxCrew-MineOps/commit/fc30af149cb8fff76dadd29dc76d7be03c25360e"),
        ("Update Group_14_data.txt", "Final update to Group_14_data.txt confirming SyntaxCrew membership and portfolio URL.", "https://github.com/makotajr006/UNAM-I3691CP-SyntaxCrew-MineOps/commit/f80652d14c4199b45b6090cab15eadbfde86fc7e"),
    ]

    github_section = ft.Column([
        section_title("💻", "GitHub Evidence & Documentation"),
        ft.Text("Verifiable proof of individual contributions to the group repository.",
                color=TEXT_SUB, size=13),
        card(ft.Column([
            ft.Row([
                ft.Icon(ft.Icons.HISTORY, color=PRIMARY, size=18),
                ft.Text("Commit History", weight=ft.FontWeight.BOLD,
                        color=TEXT_MAIN, size=15),
            ], spacing=8),
            ft.Divider(color=BG_BORDER),
            *[ft.Column([
                ft.Row([
                    ft.Icon(ft.Icons.COMMIT, color=SECONDARY, size=14),
                    ft.Text(msg, color=TEXT_MAIN, size=13,
                            weight=ft.FontWeight.W_500, expand=True),
                    ft.Container(
                        content=ft.Text("View Commit", color=PRIMARY, size=11,
                                        weight=ft.FontWeight.BOLD),
                        url=url,
                    ),
                ], spacing=8),
                ft.Text(desc, color=TEXT_SUB, size=12),
                ft.Divider(color=BG_BORDER),
            ], spacing=6) for msg, desc, url in commits]
        ], spacing=8)),
        card(ft.Column([
            ft.Row([
                ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, color=SUCCESS, size=18),
                ft.Text("Impact Summary", weight=ft.FontWeight.BOLD,
                        color=TEXT_MAIN, size=15),
            ], spacing=8),
            ft.Text(
                "Contributed the full context layer of the MineOps app — "
                "ThemeContext.js enables dynamic theming across all screens, "
                "while AuthContext.js, HazardContext.js, ShiftContext.js, and "
                "LocalizationContext.js provide centralised state for authentication, "
                "hazard tracking, shift management, and localization respectively. "
                "Also registered as an official SyntaxCrew member in the group data file.",
                color=TEXT_SUB, size=13),
        ], spacing=8)),
    ], spacing=12)

    # ── Contact Me Section ──────────────────────────────────────────────
    def contact_row(icon, label, value, url=None):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(icon, color=PRIMARY, size=20),
                    bgcolor=f"{PRIMARY}22",
                    border_radius=8,
                    padding=8,
                ),
                ft.Column([
                    ft.Text(label, color=TEXT_SUB, size=11),
                    ft.Text(value, color=TEXT_MAIN, size=13,
                            weight=ft.FontWeight.W_500),
                ], spacing=2, expand=True),
                ft.Icon(ft.Icons.OPEN_IN_NEW, color=PRIMARY, size=16) if url else ft.Container(),
            ], spacing=14),
            url=url if url else None,
        )               

               

    contact_section = ft.Column([
        section_title("📬", "Contact Me"),
        ft.Text("Feel free to reach out — always open to collaboration and feedback.",
                color=TEXT_SUB, size=13),
        card(ft.Column([
            contact_row(
                ft.Icons.EMAIL_OUTLINED,
                "Email",
                "ngulikua@gmail.com",
                "mailto:gulikua@gmail.com",
            ),
            ft.Divider(color=BG_BORDER),
            contact_row(
                ft.Icons.CODE,
                "GitHub",
                "github.com/Gulikua26",
                "https://github.com/Gulikua26",
            ),
            ft.Divider(color=BG_BORDER),
            contact_row(
                ft.Icons.BUSINESS_CENTER_OUTLINED,
                "LinkedIn",
                "linkedin.com/in/ndapandula-gulikua-2769923b8",
                "https://www.linkedin.com/in/ndapandula-gulikua-2769923b8", 
            ),
        ], spacing=12))
    ], spacing=12)

    footer = ft.Container(
        content=ft.Column([
            ft.Divider(color=BG_BORDER),
            ft.Text("© 2026 Ndapandula Gulikua — Computer Programming I",
                    color=TEXT_SUB, size=12,
                    text_align=ft.TextAlign.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
        padding=ft.padding.symmetric(horizontal=40, vertical=20),
    )

    timeline_section.key = "timeline"
    matlab_section.key = "matlab"
    blog_section.key = "blog"
    github_section.key = "github"
    contact_section.key = "contact"

    

    page.add(
        navbar,
        header,
        ft.Container(
            content=ft.Column([
                timeline_section,
                ft.Divider(color=BG_BORDER, height=40),
                matlab_section,
                ft.Divider(color=BG_BORDER, height=40),
                blog_section,
                ft.Divider(color=BG_BORDER, height=40),
                github_section,
                ft.Divider(color=BG_BORDER, height=40),
                contact_section,
            ], spacing=32),
            padding=ft.padding.symmetric(horizontal=40, vertical=30)
        ),
        footer,
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
