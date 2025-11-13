# Password Cracking Techniques and How to Stay Safe

**Feraidon AbdulRahimzai**  
CS338 - Computer Security

---

## Main Deliverable

The main deliverable is in the form of a blog which is accessible through the "Medium" blogging platform:

**Link:** https://medium.com/@feraidon.a.rahimzai/think-your-password-is-strong-hackers-would-disagree-879de9391486

**Github Link:** https://github.com/fabdul-rah/Password-Generator-and-Tester


---

## Refined Project Proposal

For my project, I'm planning to do a deep dive into the world of password cracking. I want to figure out all the different ways hackers actually break passwords, like brute-force attacks, dictionary attacks, and other common methods. To go with the research, I'm going to build a hands-on tool: a web app that serves as a password strength meter that instantly tells you how good (or bad) your password is. I want to make it super responsive and have it give you real-time feedback on why it's strong or weak, based on the cracking methods I researched.

To wrap it all up, I'll write a blog post sharing everything I learned. In the post, I'll link the app through codepen and drop the source code so anyone can check it out through my github page.

---

## Research Foundation

Following the professor's guidance, the password strength meter will be grounded in existing standards and research rather than creating an arbitrary system. The tool will be based on:

### Primary Standard: NIST Guidelines

The **NIST SP 800-63B Digital Identity Guidelines** (2017) will serve as the foundational framework for the password strength meter. These guidelines are widely respected in the security industry and provide evidence-based recommendations including:

- Minimum password length requirements (8+ characters, with 12+ recommended)
- Emphasis on password length over complexity requirements
- Protection against common passwords and dictionary words
- Entropy-based strength measurement

### Additional Research Basis

The strength meter will also incorporate findings from:

- Academic research on password strength estimation and adversarial machine learning
- Studies on password creation policies and real-world password datasets
- Research on how password strength meters influence user behavior
- Information theory (Shannon entropy) for objective strength measurement

This research-based approach ensures the tool provides genuine security insights rather than just an illusion of security.