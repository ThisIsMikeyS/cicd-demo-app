
# 🚀 CI/CD Demo App (Python)

![CI](https://github.com/ThisIsMikeyS/cicd-demo-app/actions/workflows/python-app.yml/badge.svg)
![Last Commit](https://img.shields.io/github/last-commit/ThisIsMikeyS/cicd-demo-app)

A minimal Python project to demonstrate continuous integration with GitHub Actions using `unittest`. Built for simplicity and clarity, this is ideal for learning and portfolio use.

---

## ✨ Features

- ✅ Simple Python calculator module (`add`, `subtract`, `multiply`, `divide`)
- 🧪 Unit-tested using built-in `unittest` framework
- 🔁 GitHub Actions workflow for CI on push and pull requests
- 🛠 Compatible with Visual Studio 2022 on Windows 11
- 📁 Clean folder structure for code and tests

---

## 📁 Project Structure

```
CICDDemoApp/
├── src/
│   └── calculator.py            # Application logic
├── tests/
│   └── test_calculator.py       # Unit tests
├── .github/
│   └── workflows/
│       └── python-app.yml       # GitHub Actions CI workflow
├── requirements.txt             # (Optional) Dependencies
├── README.md                    # Project documentation
├── LICENSE                      # MIT License
```

---

## 🧪 Running the Tests Locally

From your project root, run:

```bash
python -m unittest discover -s tests
```

All tests should pass.

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

This repo includes a GitHub Actions workflow that:
- Runs on `push` and `pull_request` to the `main` branch
- Sets up Python 3.10
- Installs dependencies (if any)
- Runs unit tests

You can find the workflow in:

```
.github/workflows/python-app.yml
```

---

## 🚀 Getting Started (Development)

### Prerequisites
- Python 3.10+
- Git & GitHub account
- (Optional) Visual Studio 2022 with Python tools

### Run Locally

```bash
git clone https://github.com/ThisIsMikeyS/cicd-demo-app.git
cd cicd-demo-app
python src/calculator.py
```

---

## 🧑‍💻 Author

**Michael Saunders**  
Freelance Software & Systems Developer | Technical Writer  
[LinkedIn](https://www.linkedin.com/in/michael-saunders-805785128/) · [GitHub](https://github.com/ThisIsMikeyS)

---

## 📚 License

This project is licensed under the MIT License – see the `LICENSE` file for details.
